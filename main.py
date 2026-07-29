from fastapi import FastAPI, UploadFile, File, Depends
from pathlib import Path
import shutil

# Import Authentication Router
from backend.api.routes.auth import router as auth_router

# Import Authentication Dependencies
from backend.security.auth import (
    get_current_user,
    admin_required
)

app = FastAPI(
    title="Deepfake Detection API",
    description="Backend API for Deepfake Detection System",
    version="1.0.0"
)

# Register Authentication Router
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Deepfake Detection API",
        "status": "Running Successfully"
    }


@app.post("/upload-video")
async def upload_video(
    video: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    """
    Upload a video.
    Only authenticated users can access this endpoint.
    """

    # Create uploads/videos folder if it doesn't exist
    upload_dir = Path("uploads/videos")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / video.filename

    # Save uploaded video
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    return {
        "filename": video.filename,
        "content_type": video.content_type,
        "saved_to": str(file_path),
        "uploaded_by": current_user["sub"],
        "message": "Video uploaded and saved successfully"
    }


@app.get("/admin/dashboard")
def admin_dashboard(
    current_user: dict = Depends(admin_required)
):
    """
    Admin-only endpoint.
    """

    return {
        "message": "Welcome Admin",
        "user": current_user["sub"],
        "role": current_user["role"]
    }