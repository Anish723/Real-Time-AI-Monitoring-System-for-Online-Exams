class CheatingDetector:
    def __init__(self):
        self.phone_frames = 0
        self.person_frames = 0
        self.no_face_frames = 0

    def analyze(self, face_count, person_count, phone_detected, gaze):
        messages = []
        score = 0

        # 📱 PHONE
        if phone_detected:
            self.phone_frames += 1
        else:
            self.phone_frames = 0

        if self.phone_frames >= 2:
            messages.append("Mobile phone detected")
            score = max(score, 85)

        # 👥 MULTIPLE PERSON
        if person_count > 1:
            self.person_frames += 1
        else:
            self.person_frames = 0

        if self.person_frames >= 2:
            messages.append("Multiple persons detected")
            score = max(score, 75)

        # 🚫 NO FACE (SAFE VERSION)
        if face_count == 0:
            self.no_face_frames += 1
        else:
            self.no_face_frames = 0

        # 👉 ONLY if 2 sec continuous (very safe)
        if self.no_face_frames >= 10:
            messages.append("Face not visible / Camera blocked")
            score = max(score, 50)

        # 👀 GAZE
        if gaze != "Looking Center":
            messages.append(gaze)
            score = max(score, 20)

        cheating = score >= 40

        return cheating, messages, score