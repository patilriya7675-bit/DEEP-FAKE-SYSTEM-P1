from fastapi import FastAPI
from api.routes.video import router as video_router

app = FastAPI(
    title="Deepfake Detection API",
    description="Backend API for Deepfake Detection System",
    version="1.0.0"
)

# Include video upload routes
app.include_router(video_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Deepfake Detection API",
        "status": "Running Successfully"
    }