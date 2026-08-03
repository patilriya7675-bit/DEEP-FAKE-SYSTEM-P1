import torch

from ai_models.cnn_model import DeepfakeCNN

model = DeepfakeCNN()

dummy = torch.randn(1, 3, 224, 224)

output = model(dummy)

print("Output Shape:", output.shape)
print(output)