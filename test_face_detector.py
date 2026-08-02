from services.face_detector import FaceDetector

detector = FaceDetector()

folder = detector.detect_faces()

print("Faces saved in:", folder)