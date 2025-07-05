# 🚗 Vehicle Damage & License Detection via YouTube Stream (YOLOv8 + Streamlit)

This is a Streamlit web app that performs **real-time vehicle detection and license plate identification** directly from a **YouTube Live Stream**. It uses a pre-trained [YOLOv8](https://github.com/ultralytics/ultralytics) model (`best.pt`) to identify and draw bounding boxes for multiple classes:

- License Plates
- Cars
- Motorcycles
- Trucks

---

## 📸 Features

- 🔴 Stream directly from a **YouTube Live** URL
- 🎯 Real-time detection using YOLOv8
- 📦 Deploy-ready for **Streamlit Cloud**
- 💻 No need for uploading files manually

---

## 🧠 Model

The YOLOv8 model (`best.pt`) is trained with 4 classes:

```yaml
names:
  - License_Plate
  - cars
  - motorcyle
  - truck
```

> Make sure `best.pt` is placed in the same folder as `app.py`.

---

## 🚀 How to Run (Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/Mubarok982/web-car-object-detection
cd car-damage-streamlit
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## ☁️ How to Deploy to Streamlit Cloud

1. Push this project to a GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New App"**
4. Connect your GitHub repo
5. Click **"Deploy"**

> ⚠️ Don’t forget to upload `best.pt` to the repo as well.

---

## 🔧 File Structure

```
car-damage-streamlit/
├── app.py                 # Streamlit app code
├── best.pt                # Trained YOLOv8 model
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 📺 Example YouTube Streams (for testing)

- https://youtu.be/gmDBzijaIAA?si=Ql7-uSvw4ns6BuCT


---

## 🤖 Credits

Built with:
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Streamlit](https://streamlit.io/)
- [Pytube](https://pytube.io/)

---

## 🛠 To-Do (Optional Ideas)

- Add FPS control or frame-skip options
- Add download/export results
- Support multiple models

---