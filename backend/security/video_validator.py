import cv2


def get_video_metadata(video_path: str):
    """
    Read basic metadata from a video file.
    Returns None if the file is not a valid video.
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return None

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    duration = 0
    if fps > 0:
        duration = frames / fps

    cap.release()

    return {
        "width": width,
        "height": height,
        "fps": round(fps, 2),
        "frames": frames,
        "duration_seconds": round(duration, 2)
    }