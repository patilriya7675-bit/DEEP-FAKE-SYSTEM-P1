from services.spectrogram_generator import SpectrogramGenerator

generator = SpectrogramGenerator()

image = generator.generate("uploads/audio/sample-5s.wav")

print("Spectrogram saved at:", image)