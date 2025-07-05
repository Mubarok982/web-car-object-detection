import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import os

# Load YOLOv8 model
model = YOLO("best.pt")

# Judul aplikasi
st.title("🚗 Deteksi Kendaraan - Tes Video Lokal dengan YOLOv8")

# Upload video
video_file = st.file_uploader("📤 Upload Video", type=["mp4", "mov", "avi"])

if video_file is not None:
    # Simpan file video sementara
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(video_file.read())
    video_path = tfile.name

    # Buka video
    cap = cv2.VideoCapture(video_path)
    frame_placeholder = st.empty()
    progress_bar = st.progress(0)  # Tambahkan progress bar

    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame is None:
            break

        frame_count += 1

        # Skip setiap 2 frame (jadi hanya proses 1 dari 3)
        if frame_count % 3 != 0:
            continue

        # Resize manual (jika perlu): agar lebih ringan
        resized_frame = cv2.resize(frame, (640, 384))

        # Deteksi dengan model YOLOv8
        results = model.predict(source=resized_frame, imgsz=640, conf=0.3)[0]

        # Plot hasil deteksi
        annotated_frame = results.plot()

        # Konversi warna ke RGB (OpenCV -> Streamlit)
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

        # Tampilkan frame ke Streamlit
        frame_placeholder.image(annotated_frame, channels="RGB", use_container_width=True)

        # Update progress
        progress_bar.progress(min(frame_count / total_frames, 1.0))
 
    # Bersihkan
    cap.release()
    os.remove(video_path)
    st.success("✅ Video selesai diproses.")
