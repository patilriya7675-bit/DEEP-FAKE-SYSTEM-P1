from data_loader import load_images, create_labels
import os

folder = os.path.join(os.path.dirname(__file__), "..", "dataset", "preprocessed_faces")

images = load_images(folder)

labels = create_labels(len(images), 0)

print("Total images:", len(images))
print("Labels:", labels)
print("Shape:", images.shape)