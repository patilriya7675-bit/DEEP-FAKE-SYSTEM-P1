import cv2
import os

def extract_frames(video_path, output_folder, frame_skip=10):
    """
    Extract frames from a video.

    Args:
        video_path: Path to the input video.
        output_folder: Folder where extracted frames will be saved.
        frame_skip: Save every nth frame.
    """

    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    frame_count = 0
    saved_count = 0

    while True:
        success, frame = cap.read()

        if not success:
            break

        if frame_count % frame_skip == 0:
            frame_name = os.path.join(
                output_folder,
                f"frame_{saved_count:05d}.jpg"
            )
            cv2.imwrite(frame_name, frame)
            saved_count += 1

        frame_count += 1

    cap.release()

    print(f"Total frames read: {frame_count}")
    print(f"Frames saved: {saved_count}")