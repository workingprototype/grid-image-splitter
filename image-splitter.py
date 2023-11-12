
from PIL import Image
import numpy as np

# Load the input image
input_image = Image.open("input-image-here.jpg")

# Convert the image to a numpy array
input_array = np.array(input_image)

# Determine the dimensions of the input image
height, width, channels = np.shape(input_array)

# Calculate the dimensions of each sub-image
sub_height = height // 3
sub_width = width // 3

# Loop through the rows and columns of the input image and extract each sub-image
for i in range(3):
    for j in range(3):
        sub_image = input_array[i*sub_height:(i+1)*sub_height, j*sub_width:(j+1)*sub_width]
        
        # Convert each sub-image to a PIL image
        sub_image = Image.fromarray(sub_image)
        
        # Save each sub-image
        sub_image.save(f"sub_image_{i}_{j}.jpg")
