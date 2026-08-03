import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


class SpectrogramGenerator:
    def generate(self, audio_path: str, output_dir: str = "uploads/spectrograms"):
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Load audio file
        y, sr = librosa.load(audio_path, sr=16000)

        # Generate Short-Time Fourier Transform (STFT)
        D = librosa.stft(y)

        # Convert amplitude to decibels
        DB = librosa.amplitude_to_db(np.abs(D), ref=np.max)

        # Create figure
        plt.figure(figsize=(10, 4))

        # Display spectrogram
        librosa.display.specshow(
            DB,
            sr=sr,
            x_axis="time",
            y_axis="hz"
        )

        # Add color bar
        plt.colorbar(format="%+2.0f dB")

        # Adjust layout
        plt.tight_layout()

        # Create output filename
        filename = os.path.splitext(os.path.basename(audio_path))[0]
        image_path = os.path.join(output_dir, f"{filename}.png")

        # Save image
        plt.savefig(image_path)
        plt.close()

        return image_path