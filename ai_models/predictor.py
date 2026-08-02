import torch
from PIL import Image
from torchvision import transforms

from ai_models.efficientnet import DeepfakeEfficientNet


class Predictor:

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = DeepfakeEfficientNet().to(self.device)

        self.model.load_state_dict(
            torch.load(
                "ai_models/deepfake_model.pth",
                map_location=self.device
            )
        )

        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            ),
        ])

        self.classes = ["fake", "real"]

    def predict(self, image_path):

        image = Image.open(image_path).convert("RGB")

        image = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():

            output = self.model(image)

            probabilities = torch.softmax(output, dim=1)

            confidence, prediction = torch.max(probabilities, 1)

        return {
            "prediction": self.classes[prediction.item()],
            "confidence": round(confidence.item() * 100, 2)
        }