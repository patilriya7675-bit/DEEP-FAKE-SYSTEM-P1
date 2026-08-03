import os
import subprocess


class AudioProcessor:
    def __init__(self, ffmpeg_path="ffmpeg"):
        self.ffmpeg_path = ffmpeg_path

    def extract_audio(self, video_path: str, output_dir: str = "uploads/audio"):
        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.splitext(os.path.basename(video_path))[0]
        audio_path = os.path.join(output_dir, f"{filename}.wav")

        command = [
            self.ffmpeg_path,
            "-y",
            "-i",
            video_path,
            "-vn",
            "-acodec",
            "pcm_s16le",
            "-ar",
            "16000",
            "-ac",
            "1",
            audio_path,
        ]

        subprocess.run(command, check=True)

        return audio_path