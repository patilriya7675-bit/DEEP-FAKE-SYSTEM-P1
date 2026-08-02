import torch
from ai_models.efficientnet import DeepfakeEfficientNet

model = DeepfakeEfficientNet()

x = torch.randn(1, 3, 224, 224)

output = model(x)

print("Output Shape:", output.shape)
print(output)