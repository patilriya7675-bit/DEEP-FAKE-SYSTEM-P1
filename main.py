from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI(
    title="Deepfake Detection API",
    description="Backend API for Deepfake Detection System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Deepfake Detection API",
        "status": "Running Successfully"
    }


@app.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):

    # Path where the uploaded video will be saved
    file_path = f"uploads/videos/{video.filename}"

    # Save the uploaded video
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Return response
    return {
        "filename": video.filename,
        "content_type": video.content_type,
        "saved_to": file_path,
        "message": "Video uploaded and saved successfully"
    }