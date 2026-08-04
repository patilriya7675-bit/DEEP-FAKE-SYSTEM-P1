from data_loader import load_training_data

real_images, fake_images = load_training_data()

print("Real Images :", len(real_images))
print("Fake Images :", len(fake_images))

print("Real Shape :", real_images.shape)
print("Fake Shape :", fake_images.shape)