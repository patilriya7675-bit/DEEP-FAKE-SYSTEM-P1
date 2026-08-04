from model_architecture import build_model
from data_generator import create_train_generator

# Load the model
model = build_model()

# Load the training data
train_generator = create_train_generator()

print("Model loaded successfully!")
print("Training data loaded successfully!")