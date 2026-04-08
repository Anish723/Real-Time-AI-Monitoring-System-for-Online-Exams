# Real-Time AI Monitoring System for Online Exams

## Overview

This project is an AI-based real-time monitoring system designed to detect suspicious activities during online exams.
It uses Computer Vision and Deep Learning techniques to track user behavior through a webcam and identify cheating patterns.

---

## Features

* Face Detection (Single / Multiple persons detection)
* Mobile Phone Detection using YOLO model
* Eye Tracking (Gaze Detection)
* Cheating Detection Logic
* Real-time Alert System (Sound Warning)
* Live Score Monitoring
* Event Logging System
* Auto Exam Submission after 3 Warnings

---

## Tech Stack

* Python
* Streamlit
* OpenCV
* MediaPipe
* YOLO (Ultralytics)
* Pygame

---

## Project Structure

```
├── app/
│   └── main.py
├── detection/
│   ├── face_detector.py
│   ├── object_detector.py
│   ├── cheating_logic.py
│   ├── eye_tracker.py
├── utils/
│   ├── alerts.py
│   ├── logger.py
├── models/
│   └── custom_phone.pt
├── assets/
│   └── alert.wav
├── logs/
└── .gitignore
```

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/Anish723/Real-Time-AI-Monitoring-System-for-Online-Exams.git
cd Real-Time-AI-Monitoring-System-for-Online-Exams
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install streamlit opencv-python mediapipe pygame ultralytics
```

---

### 4. Run the project

```
streamlit run app/main.py
```

---

## How It Works

* Webcam captures live video
* Face, object and eye tracking run in real-time
* AI analyzes behavior
* Alerts are triggered for suspicious actions
* Score is calculated based on cheating probability

---

## Output

* Live video monitoring
* Real-time cheating score
* Warning alerts
* Final result summary

---

## Warning System

* First Warning → Alert
* Second Warning → Alert
* Third Warning → Exam auto submitted

---

## Future Improvements

* Face Recognition for student verification
* Cloud-based monitoring system
* Advanced analytics dashboard
* Recording suspicious clips
* Improved AI model accuracy

---

## Author

Anish Kumar
