import streamlit as st
import cv2
import time

from detection.face_detector import FaceDetector
from detection.object_detector import ObjectDetector
from detection.cheating_logic import CheatingDetector
from detection.eye_tracker import EyeTracker
from utils.alerts import AlertSystem
from utils.logger import Logger

# INIT
face_detector = FaceDetector()
object_detector = ObjectDetector()
cheating_detector = CheatingDetector()
eye_tracker = EyeTracker()
alert_system = AlertSystem()
logger = Logger()

st.title("Real-Time AI Monitoring System for Online Exams")

# SESSION INIT
if "running" not in st.session_state:
    st.session_state.running = False
    st.session_state.paused = False
    st.session_state.warning_count = 0
    st.session_state.max_score = 0
    st.session_state.events = []

# BUTTONS
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Start Monitoring"):
        st.session_state.running = True

        # 🔥 RESET FIX
        st.session_state.max_score = 0
        st.session_state.events = []
        st.session_state.warning_count = 0
        st.session_state.paused = False

with col2:
    if st.button("Stop Monitoring"):
        st.session_state.running = False

with col3:
    if st.button("Continue"):
        st.session_state.paused = False

FRAME = st.image([])
status = st.empty()
score_box = st.empty()

cap = cv2.VideoCapture(0)

# LOOP
while st.session_state.running:

    # ⛔ PAUSE MODE
    if st.session_state.paused:
        status.warning(f"⚠️ Warning {st.session_state.warning_count}/3 - Click Continue")
        time.sleep(0.2)
        continue

    ret, frame = cap.read()
    if not ret:
        break

    # PROCESS
    frame, face_count = face_detector.detect_faces(frame)
    frame, person_count, phone_detected = object_detector.detect_objects(frame, face_count)
    frame, gaze = eye_tracker.track_eyes(frame)

    cheating, messages, score = cheating_detector.analyze(
        face_count, person_count, phone_detected, gaze
    )

    # SCORE TRACK
    if score > st.session_state.max_score:
        st.session_state.max_score = score

    # EVENTS
    for msg in messages:
        if msg not in st.session_state.events:
            st.session_state.events.append(msg)
            logger.log(msg, score)

    # ⚠️ WARNING
    if "Mobile phone detected" in messages or "Multiple persons detected" in messages:
        st.session_state.warning_count += 1
        st.session_state.paused = True

        st.session_state.events.append(
            f"Warning {st.session_state.warning_count}: " + " | ".join(messages)
        )

        status.error(f"🚨 Warning {st.session_state.warning_count}/3: " + " | ".join(messages))
        alert_system.play_alert()

    else:
        status.success("✅ Normal Behavior")

    score_box.metric("Live Score", score)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME.image(frame)

    # ⛔ AUTO STOP
    if st.session_state.warning_count >= 3:
        st.session_state.running = False
        break

    time.sleep(0.005)

# FINAL RESULT
if not st.session_state.running:

    cap.release()

    st.subheader("📊 FINAL RESULT")

    final_score = st.session_state.max_score

    # SCORE
    st.metric("Final Score", final_score)

    # EVENTS
    if st.session_state.events:
        st.write("Detected Events:")
        for e in st.session_state.events:
            st.write(f"- {e}")
    else:
        st.write("No suspicious activity detected")

    # MESSAGE
    if st.session_state.warning_count >= 3:
        st.write("❗ Exam auto-submitted due to 3 warnings")
    else:
        st.write("✔ Exam completed normally")

    # RESULT
    if final_score >= 80:
        st.error("🚨 CHEATING DETECTED")
    elif final_score >= 40:
        st.warning("⚠️ Suspicious Behavior")
    else:
        st.success("✅ No Cheating")