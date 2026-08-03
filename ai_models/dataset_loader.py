from torchvision import datasets, transforms
from torch.utils.data import DataLoader


class DatasetLoader:

    def __init__(self, batch_size=16):

        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            ),
        ])

        self.train_dataset = datasets.ImageFolder(
            "dataset/train",
            transform=transform
        )

        self.validation_dataset = datasets.ImageFolder(
            "dataset/validation",
            transform=transform
        )

        self.train_loader = DataLoader(
            self.train_dataset,
            batch_size=batch_size,
            shuffle=True
        )

        self.validation_loader = DataLoader(
            self.validation_dataset,
            batch_size=batch_size,
            shuffle=False
        )

    def get_loaders(self):
        return self.train_loader, self.validation_loader