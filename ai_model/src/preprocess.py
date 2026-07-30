import cv2
import os
import numpy as np


def preprocess_image(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Check if image loaded
    if image is None:
        return None

    # Resize image
    image = cv2.resize(image, (299, 299))

    # Normalize pixel values
    image = image / 255.0

    return image


def preprocess_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read all files in input folder
    for filename in os.listdir(input_folder):

        input_path = os.path.join(input_folder, filename)

        # Preprocess image
        image = preprocess_image(input_path)

        if image is None:
            continue

        # Convert back to 0-255 for saving
        image = (image * 255).astype(np.uint8)

        output_path = os.path.join(output_folder, filename)

        # Save processed image
        cv2.imwrite(output_path, image)

    print("Preprocessing completed.")


# Example
input_folder = "dataset/detected_faces"
output_folder = "dataset/preprocessed_faces"

preprocess_folder(input_folder, output_folder)