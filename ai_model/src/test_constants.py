import os
from constants import TRAIN_REAL, TRAIN_FAKE

print("Train Real Path:")
print(TRAIN_REAL)
print("Exists:", os.path.exists(TRAIN_REAL))

print()

print("Train Fake Path:")
print(TRAIN_FAKE)
print("Exists:", os.path.exists(TRAIN_FAKE))