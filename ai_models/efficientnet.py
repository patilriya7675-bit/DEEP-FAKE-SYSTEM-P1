import torch
import torch.nn as nn
import timm


class DeepfakeEfficientNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.model = timm.create_model(
            "efficientnet_b0",
            pretrained=True
        )

        in_features = self.model.classifier.in_features

        self.model.classifier = nn.Linear(
            in_features,
            2
        )

    def forward(self, x):
        return self.model(x)