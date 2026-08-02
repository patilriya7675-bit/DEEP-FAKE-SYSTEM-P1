from fastapi import APIRouter, UploadFile, File
import shutil

from services.frame_extractor import FrameExtractor
from services.face_detector import FaceDetector
from ai_models.predictor import Predictor

router = APIRouter()

frame_extractor = FrameExtractor()
face_detector = FaceDetector()
predictor = Predictor()


@router.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):

    file_path = f"uploads/videos/{video.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Step 1: Extract Frames
    frame_dir = frame_extractor.extract_frames(file_path)

    # Step 2: Detect Faces
    faces_dir = face_detector.detect_faces(frame_dir)

    # Step 3: Predict using first detected face
    import os

    face_files = [
        os.path.join(faces_dir, f)
        for f in os.listdir(faces_dir)
        if f.endswith(".jpg")
    ]

    if len(face_files) == 0:
        return {
            "error": "No faces detected."
        }

    result = predictor.predict(face_files[0])

    return {
        "filename": video.filename,
        "prediction": result["prediction"],
        "confidence": result["confidence"]
    }