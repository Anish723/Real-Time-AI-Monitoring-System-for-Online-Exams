from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self):
        self.model = YOLO("models/custom_phone.pt")

    def detect_objects(self, frame, face_count):
        results = self.model(frame, conf=0.5, iou=0.4, verbose=False)

        phone_detected = False

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # 🔥 stricter detection
                if conf > 0.6:
                    phone_detected = True

                    cv2.rectangle(frame, (x1,y1),(x2,y2),(0,0,255),2)
                    cv2.putText(frame, f"PHONE {conf:.2f}",
                                (x1,y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

        person_count = face_count
        return frame, person_count, phone_detected