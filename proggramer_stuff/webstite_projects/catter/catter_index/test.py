import os
import django

# Set the environment variable for the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catter.settings')

# Setup Django
django.setup()

# Now you can import your models
from catter_index.models import Cat  # Adjust the import path if needed
from django.core.files import File

# Path to your image file
image_path = 'path/to/your/cat_image.jpg'

# Open the image file and create a File object
with open(image_path, 'rb') as img_file:
    cat_image_file = File(img_file)
    
    # Create a Cat instance
    cat = Cat(cat_name='Fluffy', elo=100)

    # Assign the image to the cat_image field
    cat.cat_image.save(os.path.basename(image_path), cat_image_file, save=True)

# The Cat instance is now saved with the image
print(cat.id)  # Print the id of the saved Cat instance to confirm
