from ai_models.dataset_loader import DatasetLoader

loader = DatasetLoader()

train_loader, validation_loader = loader.get_loaders()

print("Training Images:", len(loader.train_dataset))
print("Validation Images:", len(loader.validation_dataset))

print("Classes:", loader.train_dataset.classes)

images, labels = next(iter(train_loader))

print(images.shape)
print(labels.shape)