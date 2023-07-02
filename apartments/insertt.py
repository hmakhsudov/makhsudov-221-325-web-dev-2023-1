import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apartments.settings")
django.setup()

from realtyapp.models import Apartment, ApartmentImage
import random
from django.core.files import File


apartments = Apartment.objects.all()

apartment_list = list(apartments)
image_folder_path = 'D:/pythonprojects/money/artem_kursovaya/apartments/apartments/images/'

# Create a list of complete image paths by joining the folder path with the file names
image_file_names = os.listdir(image_folder_path)

# Create a list of complete image paths by joining the folder path with the file names
image_paths = [os.path.join(image_folder_path, file_name) for file_name in image_file_names]
# Shuffle the image_paths list randomly
random.shuffle(image_paths)

# Determine the number of images to add (between 3 and 5)
num_images = random.randint(3, 5)

# Select a random subset of image_paths
for apartment in apartments:
    # Shuffle the image_paths list randomly
    random.shuffle(image_paths)

    # Determine the number of images to add (between 3 and 5)
    num_images = random.randint(3, 5)

    # Select a random subset of image_paths for this apartment
    selected_images = random.sample(image_paths, num_images)

    for image_path in selected_images:
        # Create an instance of ApartmentImage and associate it with the apartment
        apartment_image = ApartmentImage(apartment=apartment)

        # Open the image file using Python's open() function or any other method you prefer
        image_file = open(image_path, 'rb')

        # Create a Django File object from the image file
        django_file = File(image_file)

        # Assign the Django File object to the 'image' field of the ApartmentImage instance
        apartment_image.image.save(os.path.basename(image_path), django_file, save=False)

        # Save the ApartmentImage instance to the database
        apartment_image.save()
# Retrieve all apartments from the database