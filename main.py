from fastapi import FastAPI, UploadFile, File, Depends, Request, HTTPException, status
from pathlib import Path
import shutil

# SlowAPI Imports
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler

# Rate Limiter
from backend.security.rate_limiter import limiter

# Security Headers Middleware
from backend.security.security_headers import SecurityHeadersMiddleware

# File Validation
from backend.security.file_validator import (
    validate_video_extension,
    validate_file_size
)

# Video Metadata Validator
from backend.security.video_validator import get_video_metadata

# Import Authentication Router
from backend.api.routes.auth import router as auth_router

# Import Authentication Dependencies
from backend.security.auth import (
    get_current_user,
    admin_required,
    analyst_required,
    user_required
)

app = FastAPI(
    title="Deepfake Detection API",
    description="Backend API for Deepfake Detection System",
    version="1.0.0"
)

# -----------------------------
# Configure Rate Limiter
# -----------------------------
app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

# Register Middlewares
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(SecurityHeadersMiddleware)

# Register Authentication Router
app.include_router(auth_router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to Deepfake Detection API",
        "status": "Running Successfully"
    }


@app.post("/upload-video", tags=["Upload"])
@limiter.limit("10/minute")
async def upload_video(
    request: Request,
    video: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    """
    Secure Video Upload
    """

    # -----------------------------
    # Validate File Extension
    # -----------------------------
    if not validate_video_extension(video.filename):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format. Only MP4, AVI, MOV and MKV files are allowed."
        )

    # -----------------------------
    # Validate File Size
    # -----------------------------
    file_bytes = await video.read()

    if not validate_file_size(len(file_bytes)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size exceeds the maximum limit of 100 MB."
        )

    # Reset file pointer
    await video.seek(0)

    # -----------------------------
    # Create Upload Folder
    # -----------------------------
    upload_dir = Path("uploads/videos")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / video.filename

    # -----------------------------
    # Save Uploaded File
    # -----------------------------
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # -----------------------------
    # Validate Uploaded Video
    # -----------------------------
    metadata = get_video_metadata(str(file_path))

    if metadata is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is not a valid video."
        )

    return {
        "filename": video.filename,
        "content_type": video.content_type,
        "saved_to": str(file_path),
        "uploaded_by": current_user["sub"],
        "video_metadata": metadata,
        "message": "Video uploaded and saved successfully"
    }


@app.get("/admin/dashboard", tags=["Admin"])
def admin_dashboard(
    current_user: dict = Depends(admin_required)
):
    return {
        "message": "Welcome Admin",
        "user": current_user["sub"],
        "role": current_user["role"]
    }


@app.get("/analyst/dashboard", tags=["Analyst"])
def analyst_dashboard(
    current_user: dict = Depends(analyst_required)
):
    return {
        "message": "Welcome Analyst",
        "user": current_user["sub"],
        "role": current_user["role"]
    }


@app.get("/user/profile", tags=["User"])
def user_profile(
    current_user: dict = Depends(user_required)
):
    return {
        "message": "Welcome User",
        "user": current_user["sub"],
        "role": current_user["role"]
    }