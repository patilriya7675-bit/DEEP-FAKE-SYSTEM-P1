from data_generator import create_train_generator

train_generator = create_train_generator()

print("\nGenerator created successfully!\n")

print("Total Images :", train_generator.samples)
print("Batch Size   :", train_generator.batch_size)
print("Classes      :", train_generator.class_indices)