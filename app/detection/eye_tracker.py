import cv2
import mediapipe as mp

class EyeTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(refine_landmarks=True)

    def track_eyes(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        gaze = "Looking Center"

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape

                left = face_landmarks.landmark[33]
                right = face_landmarks.landmark[263]

                lx, rx = int(left.x*w), int(right.x*w)

                # simple direction logic
                if lx < w*0.25:
                    gaze = "Looking Left"
                elif rx > w*0.75:
                    gaze = "Looking Right"
                else:
                    gaze = "Looking Center"

        return frame, gaze