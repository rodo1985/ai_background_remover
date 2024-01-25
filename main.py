import shutil
from transparent_background import Remover
from PIL import Image
import numpy as np
import cv2
import os
import tqdm

# create remover
remover = Remover(mode='fast')

image_folder = 'images'

# remove output directory if exist and all files
if os.path.exists(os.path.join(image_folder, 'output')):
    shutil.rmtree(os.path.join(image_folder, 'output'))

# create output folder
os.makedirs(os.path.join(image_folder, 'output'), exist_ok=True)

# list all files with jpg extension
files = [file for file in os.listdir(image_folder) if file.endswith('.jpg')]

# for each file
for file in tqdm.tqdm(files):

    input_image_path = os.path.join(image_folder, file)
    output_image_path = os.path.join(image_folder, 'output', file)

    # read image
    imagen = Image.open(input_image_path).convert('RGB')

    # proceed image
    out = np.array(remover.process(imagen, type='map'))

    # convert to gray
    out = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY)

    # binarize image
    _, out = cv2.threshold(out, 127, 255, cv2.THRESH_BINARY)

    # set kernel
    kernel = np.ones((11, 11), np.uint8)

    # closing image to fill holes
    out = cv2.morphologyEx(out, cv2.MORPH_CLOSE, kernel)

    # save image
    cv2.imwrite(output_image_path, out)