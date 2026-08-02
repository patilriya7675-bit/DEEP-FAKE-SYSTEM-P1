from services.frame_extractor import FrameExtractor

extractor = FrameExtractor()

folder = extractor.extract_frames(
    "uploads/videos/sample-5s.mp4"
)

print("Frames saved in:", folder)