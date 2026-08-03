import torch
import torch.nn as nn
import torch.optim as optim

from ai_models.efficientnet import DeepfakeEfficientNet
from ai_models.dataset_loader import DatasetLoader


class Trainer:

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        print(f"Using Device: {self.device}")

        self.model = DeepfakeEfficientNet().to(self.device)

        loader = DatasetLoader(batch_size=16)
        self.train_loader, self.validation_loader = loader.get_loaders()

        self.criterion = nn.CrossEntropyLoss()

        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=0.0001
        )

    def train(self, epochs=5):

        best_accuracy = 0.0

        for epoch in range(epochs):

            self.model.train()

            running_loss = 0.0

            for images, labels in self.train_loader:

                images = images.to(self.device)
                labels = labels.to(self.device)

                self.optimizer.zero_grad()

                outputs = self.model(images)

                loss = self.criterion(outputs, labels)

                loss.backward()

                self.optimizer.step()

                running_loss += loss.item()

            accuracy = self.validate()

            print(
                f"Epoch {epoch + 1}/{epochs} | "
                f"Loss: {running_loss:.4f} | "
                f"Validation Accuracy: {accuracy:.2f}%"
            )

            if accuracy > best_accuracy:

                best_accuracy = accuracy

                torch.save(
                    self.model.state_dict(),
                    "ai_models/deepfake_model.pth"
                )

                print("✅ Best model saved!")

    def validate(self):

        self.model.eval()

        correct = 0
        total = 0

        with torch.no_grad():

            for images, labels in self.validation_loader:

                images = images.to(self.device)
                labels = labels.to(self.device)

                outputs = self.model(images)

                _, predicted = torch.max(outputs, 1)

                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        return (correct / total) * 100