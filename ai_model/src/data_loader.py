import os
import cv2
import numpy as np

from constants import TRAIN_REAL, TRAIN_FAKE


def load_images(folder_path):
    images = []

    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)

        # Read image
        image = cv2.imread(image_path)

        # Skip if image is not loaded
        if image is None:
            continue

        # Resize image for Xception
        image = cv2.resize(image, (299, 299))

        # Normalize pixel values (0-255 → 0-1)
        image = image / 255.0

        # Store image
        images.append(image)

    return np.array(images)


def create_labels(num_images, label):
    labels = np.full(num_images, label)
    return labels


def load_training_data():

    # Load real images
    real_images = load_images(TRAIN_REAL)

    # Load fake images
    fake_images = load_images(TRAIN_FAKE)

    return real_images, fake_images