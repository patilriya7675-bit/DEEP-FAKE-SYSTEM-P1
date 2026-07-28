from fastapi import FastAPI

app = FastAPI(
    title="Deepfake Detection API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Real-Time Deepfake Detection Backend Running"
    }