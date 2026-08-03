import os

from services.frame_extractor import FrameExtractor
from services.face_detector import FaceDetector
from ai_models.predictor import Predictor


class DeepfakeDetector:
    def __init__(self):
        self.frame_extractor = FrameExtractor()
        self.face_detector = FaceDetector()
        self.predictor = Predictor()

    def detect(self, video_path):
        """
        Complete Deepfake Detection Pipeline
        """

        # Step 1: Extract frames
        frame_dir = self.frame_extractor.extract_frames(video_path)

        frame_files = [
            f for f in os.listdir(frame_dir)
            if f.lower().endswith(".jpg")
        ]
        frame_count = len(frame_files)

        # Step 2: Detect faces from all frames
        faces_dir = self.face_detector.detect_faces(frame_dir)

        face_files = [
            f for f in os.listdir(faces_dir)
            if f.lower().endswith(".jpg")
        ]
        face_count = len(face_files)

        predictions = []

        # Step 3: Predict every detected face
        for face_name in face_files:

            face_path = os.path.join(faces_dir, face_name)

            result = self.predictor.predict(face_path)

            confidence = result["confidence"] / 100

            if result["prediction"].lower() == "fake":
                score = confidence
            else:
                score = 1 - confidence

            predictions.append(score)

        # No faces detected
        if len(predictions) == 0:
            return {
                "prediction": "No face detected",
                "confidence": 0.0,
                "frames_processed": frame_count,
                "faces_detected": 0
            }

        # Average confidence
        avg_score = sum(predictions) / len(predictions)

        prediction = "Fake" if avg_score >= 0.5 else "Real"

        return {
            "prediction": prediction,
            "confidence": round(avg_score * 100, 2),
            "frames_processed": frame_count,
            "faces_detected": face_count
        }