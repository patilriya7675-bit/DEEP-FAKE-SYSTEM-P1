from tensorflow.keras.preprocessing.image import ImageDataGenerator

from constants import TRAIN_PATH


def create_train_generator():

    datagen = ImageDataGenerator(
        rescale=1.0 / 255
    )

    train_generator = datagen.flow_from_directory(
        directory=TRAIN_PATH,
        target_size=(299, 299),
        batch_size=32,
        class_mode="binary",
        shuffle=True
    )

    return train_generator