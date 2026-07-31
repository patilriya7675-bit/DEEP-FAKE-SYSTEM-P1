from fastapi import FastAPI, UploadFile, File, Depends, Request
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
    """
    Home Endpoint

    Check whether the API is running successfully.
    """
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
    Upload a video.

    Authentication Required:
    - Admin
    - Analyst
    - User

    Returns:
    - Uploaded filename
    - Content type
    - File location
    - Username of uploader
    """

    upload_dir = Path("uploads/videos")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / video.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    return {
        "filename": video.filename,
        "content_type": video.content_type,
        "saved_to": str(file_path),
        "uploaded_by": current_user["sub"],
        "message": "Video uploaded and saved successfully"
    }


@app.get("/admin/dashboard", tags=["Admin"])
def admin_dashboard(
    current_user: dict = Depends(admin_required)
):
    """
    Admin Dashboard

    Access:
    - Admin only

    Purpose:
    - Administrative operations
    """

    return {
        "message": "Welcome Admin",
        "user": current_user["sub"],
        "role": current_user["role"]
    }


@app.get("/analyst/dashboard", tags=["Analyst"])
def analyst_dashboard(
    current_user: dict = Depends(analyst_required)
):
    """
    Analyst Dashboard

    Access:
    - Admin
    - Analyst

    Purpose:
    - AI analysis and reporting
    """

    return {
        "message": "Welcome Analyst",
        "user": current_user["sub"],
        "role": current_user["role"]
    }


@app.get("/user/profile", tags=["User"])
def user_profile(
    current_user: dict = Depends(user_required)
):
    """
    User Profile

    Access:
    - Admin
    - Analyst
    - User

    Purpose:
    - View authenticated user information
    """

    return {
        "message": "Welcome User",
        "user": current_user["sub"],
        "role": current_user["role"]
    }