from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def build_model():

    # Load pre-trained Xception model
    base_model = Xception(
        weights="imagenet",
        include_top=False,
        input_shape=(299, 299, 3)
    )

    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    output = Dense(1, activation="sigmoid")(x)

    # Create final model
    model = Model(
        inputs=base_model.input,
        outputs=output
    )

    # Compile model
    model.compile(
        optimizer=Adam(),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model