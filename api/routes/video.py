from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter()

@router.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):
    file_path = f"uploads/videos/{video.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    return {
        "filename": video.filename,
        "content_type": video.content_type,
        "saved_to": file_path,
        "message": "Video uploaded successfully"
    }