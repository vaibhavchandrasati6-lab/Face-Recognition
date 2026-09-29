# 👤 Real-Time Face Recognition System

A real-time **Face Recognition System** built with **Python, OpenCV, NumPy, and face_recognition**.

The application uses a webcam to detect faces and recognize known people by comparing their facial encodings with reference images stored in the project.

---

## 🚀 Features

* 🎥 Real-time webcam face detection
* 🧠 Face recognition using facial encodings
* 👥 Recognition of multiple known people
* 🏷️ Displays the recognized person's name
* ❓ Shows `Unknown` for unrecognized faces
* 🖼️ Supports `.jpg`, `.jpeg`, and `.png` images
* 🔄 Real-time processing using OpenCV
* ⚠️ Handles images where no face is detected

---

## 🛠️ Tech Stack

| Technology           | Purpose                                 |
| -------------------- | --------------------------------------- |
| **Python**           | Core programming                        |
| **OpenCV**           | Webcam & image processing               |
| **face_recognition** | Face detection & recognition            |
| **NumPy**            | Image and numerical processing          |
| **dlib**             | Backend dependency for face recognition |

---

## 📂 Project Structure

```text
Face-Recognition/
│
├── images/
│
├── main.py
└── Readme.md
└── requirements.txt
```

---


## ▶️ Run the Project

Add reference images to the `images` folder and run:

```bash
python main.py
```

The webcam will open and start recognizing faces.

Press **`M`** to exit the application.


---

## 📌 Example

When a known person is detected:

```text
┌─────────────────────────┐
│                         │
│       👤               │
│    ┌─────────┐          │
│    │         │          │
│    │  Face   │          │
│    │         │          │
│    └─────────┘          │
│      Virat              │
│                         │
└─────────────────────────┘
```

For an unrecognized person:

```text
Unknown
```

---


## 📚 What I Learned

Through this project, I worked with:

* Real-time computer vision
* OpenCV webcam handling
* Image format conversion
* Face detection
* Facial feature encoding
* Face comparison
* NumPy image processing
* File and folder handling
* Real-time video processing
