# Transparent Background Remover

## Overview
This project provides a tool for removing the background from images, particularly focusing on `.jpg` files. It utilizes the `transparent_background` library and additional image processing techniques to achieve this. The tool is designed to be easy to use and efficient in processing a batch of images.

## Features
- Batch processing of `.jpg` images.
- Utilizes `transparent_background` library for initial background removal.
- Additional image processing including conversion to grayscale, binarization, and morphological operations to refine the output.

## Prerequisites
- Python 3.x
- Libraries: PIL, NumPy, OpenCV, tqdm

## Installation

Before using this script, ensure that you have Python 3.x installed on your system. Then, you can install the `transparent-background` library using `pip`.

To install the `transparent-background` library, run:

```bash
pip install transparent-background
```

## Usage

Place your `.jpg` images in the `images` folder. Then run the script:

```bash
python main.py
```

Processed images will be saved in the `images/output` directory.

## How It Works

1. **Initialization**: The `Remover` object is created with the mode set to 'base-nightly'.
2. **Preparation**: The script checks for the `output` directory within the `images` folder, creating it if it doesn't exist, and clears it if it does.
3. **Processing**: Each `.jpg` image in the `images` folder is processed as follows:
    - The background is removed using the `transparent_background` library.
    - The image is converted to grayscale.
    - Binarization is applied to the image.
    - Morphological closing is performed to fill holes.
4. **Output**: The processed image is saved in the `output` directory.

## Contributing
Feel free to fork the project and submit pull requests. You can also open an issue if you find any bugs or have feature requests.

## License
[MIT License](LICENSE)