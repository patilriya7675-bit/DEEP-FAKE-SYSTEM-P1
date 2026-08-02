import os
import cv2
import numpy as np


def load_images(folder_path):
    images = []

    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)

        image = cv2.imread(image_path)

        if image is None:
            continue

        images.append(image)

    return np.array(images)


def create_labels(num_images, label):
    labels = np.full(num_images, label)
    return labels