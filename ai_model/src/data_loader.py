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

        image = image.astype(np.float32) / 255.0

        images.append(image)

    return np.array(images)