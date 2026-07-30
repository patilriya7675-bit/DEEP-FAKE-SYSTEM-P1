import cv2
from preprocess import preprocess_face

# Read image from the project-level dataset folder
image = cv2.imread("../../dataset/test.jpg")

# Check if image exists
if image is None:
    print("❌ Error: Could not find '../../dataset/test.jpg'")
    exit()

# Preprocess the image
processed = preprocess_face(image)

print("✅ Preprocessing Successful!")
print("Shape:", processed.shape)
print("Minimum Pixel Value:", processed.min())
print("Maximum Pixel Value:", processed.max())