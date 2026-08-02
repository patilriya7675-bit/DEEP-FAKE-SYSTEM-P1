import os
import cv2


class FaceDetector:
    def __init__(self):
        self.detector = cv2.CascadeClassifier(
            "models/haarcascade_frontalface_default.xml"
        )

    def detect_faces(
        self,
        frame_folder="uploads/frames",
        output_folder="uploads/faces",
    ):
        os.makedirs(output_folder, exist_ok=True)

        count = 0

        for file in os.listdir(frame_folder):

            if not file.lower().endswith(".jpg"):
                continue

            image_path = os.path.join(frame_folder, file)

            image = cv2.imread(image_path)

            if image is None:
                continue

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = self.detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(50, 50),
            )

            for (x, y, w, h) in faces:
                face = image[y:y+h, x:x+w]

                cv2.imwrite(
                    os.path.join(output_folder, f"face_{count}.jpg"),
                    face,
                )

                count += 1

        print(f"Detected {count} faces.")

        return output_folder