from extract_frames import extract_frames
from face_detector import detect_faces

video_path = "dataset/WhatsApp Video 2026-07-28 at 23.46.06.mp4"

frames_folder = "dataset/extracted_frames"
faces_folder = "dataset/detected_faces"

extract_frames(video_path, frames_folder)
detect_faces(frames_folder, faces_folder)