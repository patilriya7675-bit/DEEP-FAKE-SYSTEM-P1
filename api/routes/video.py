from fastapi import APIRouter, UploadFile, File
import shutil
import os

from services.deepfake_detector import DeepfakeDetector

router = APIRouter()

detector = DeepfakeDetector()


@router.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):
    # Create upload directory
    os.makedirs("uploads/videos", exist_ok=True)

    # Save uploaded video
    file_path = f"uploads/videos/{video.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Run complete deepfake detection pipeline
    result = detector.detect(file_path)

    return {
        "filename": video.filename,
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "frames_processed": result["frames_processed"],
        "faces_detected": result["faces_detected"]
    }