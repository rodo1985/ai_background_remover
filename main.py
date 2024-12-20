import shutil
from transparent_background import Remover
from PIL import Image
import numpy as np
import cv2
import os
import tqdm

# Create remover
remover = Remover(mode='fast')

input_folder = 'images/input'
output_folder = 'images/output'

# Remove the output directory if it exists and all its contents
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

# Create the output folder
os.makedirs(output_folder, exist_ok=True)

# Walk through the input folder recursively
for root, dirs, files in os.walk(input_folder):
    for file in tqdm.tqdm(files, desc=f"Processing files in {root}"):
        if file.endswith('.jpg'):  # Process only .jpg files
            input_image_path = os.path.join(root, file)

            # Determine relative path of the current file
            relative_path = os.path.relpath(input_image_path, input_folder)

            # Construct the corresponding output path
            output_image_path = os.path.join(output_folder, relative_path)

            # Create necessary directories in the output path
            os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

            # Read image
            imagen = Image.open(input_image_path).convert('RGB')
            original_array = np.array(imagen)

            # Process image to remove background (get the mask)
            mask = np.array(remover.process(imagen, type='map'))

            # Convert mask to grayscale
            mask = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)

            # Binarize mask
            _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

            # Refine the mask using morphological closing to fill holes
            kernel = np.ones((11, 11), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            # Invert the mask for background removal
            inverted_mask = cv2.bitwise_not(mask)

            # Apply the mask to the original image
            foreground = cv2.bitwise_and(original_array, original_array, mask=mask)

            # Replace background with white
            background = cv2.bitwise_and(np.full_like(original_array, 255), 
                                         np.full_like(original_array, 255), mask=inverted_mask)

            # Combine foreground and background
            output_image = cv2.add(foreground, background)

            # Save the resulting image
            cv2.imwrite(output_image_path, cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))