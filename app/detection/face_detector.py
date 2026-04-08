import cv2
import mediapipe as mp

class FaceDetector:
    def __init__(self):
        self.mp_face = mp.solutions.face_detection
        self.face = self.mp_face.FaceDetection(min_detection_confidence=0.7)
        self.history = []

    def detect_faces(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face.process(rgb_frame)

        face_count = 0

        if results.detections:
            h, w, _ = frame.shape
            valid_faces = []

            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                w_box = int(bbox.width * w)
                h_box = int(bbox.height * h)

                # 🔥 ignore noise
                if w_box * h_box < (w * h) * 0.03:
                    continue

                valid_faces.append((x, y, w_box, h_box))

            face_count = len(valid_faces)

            for (x,y,w_box,h_box) in valid_faces:
                cv2.rectangle(frame, (x,y),(x+w_box,y+h_box),(0,255,0),2)

        # 🔥 stability (avoid flicker)
        self.history.append(face_count)
        if len(self.history) > 5:
            self.history.pop(0)

        if self.history:
            face_count = max(set(self.history), key=self.history.count)

        return frame, face_count