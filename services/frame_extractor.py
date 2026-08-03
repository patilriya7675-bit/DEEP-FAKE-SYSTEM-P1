import os
import cv2


class FrameExtractor:
    def extract_frames(self, video_path: str, output_dir: str = "uploads/frames"):
        os.makedirs(output_dir, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        frame_count = 0

        while True:
            success, frame = cap.read()

            if not success:
                break

            frame_path = os.path.join(
                output_dir,
                f"frame_{frame_count:04d}.jpg"
            )

            cv2.imwrite(frame_path, frame)

            frame_count += 1

        cap.release()

        print(f"Extracted {frame_count} frames.")

        return output_dir