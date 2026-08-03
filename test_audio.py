from services.audio_processor import AudioProcessor

print("Starting audio extraction...")

processor = AudioProcessor()

audio = processor.extract_audio("uploads/videos/sample-5s.mp4")

print("Audio saved at:", audio)
print("Done!")