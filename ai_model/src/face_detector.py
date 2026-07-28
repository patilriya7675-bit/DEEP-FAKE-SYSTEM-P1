import cv2
import os

# Load OpenCV's pre-trained face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_faces(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    image_files = [
        f for f in os.listdir(input_folder)
        if f.endswith(".jpg")
    ]

    for image_name in image_files:

        image_path = os.path.join(input_folder, image_name)

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        count = 0

        for (x, y, w, h) in faces:

            face = image[y:y+h, x:x+w]

            save_path = os.path.join(
                output_folder,
                f"{os.path.splitext(image_name)[0]}_face_{count}.jpg"
            )

            cv2.imwrite(save_path, face)

            count += 1

    print("Face detection completed.")