import numpy as np
from tensorflow.keras.models import load_model

# Load the trained Xception model
model = load_model("../models/model.h5")


def predict_face(face):
    """
    Predict whether the face is Real or Fake.
    """

    # Add batch dimension
    face = np.expand_dims(face, axis=0)

    # Predict
    prediction = model.predict(face)

    return prediction