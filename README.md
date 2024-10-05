# Image Processing Application

## Overview

This project is a graphical user interface (GUI) application designed for basic image processing tasks, including:
- Grayscale conversion
- Edge detection
- RGB histogram calculation
- Shape/object detection

The application is built using **Python** and key libraries such as **PyQt5** for the GUI, **PIL** (Pillow) for image manipulation, **OpenCV** for advanced image processing, and **Matplotlib** for plotting histograms.

## Features

- **Load Image**: Import an image from the user's local system.
- **Convert to Grayscale**: Convert the image to black and white.
- **Edge Detection**: Detect edges in the grayscale image using image filters.
- **Display Histogram**: Show the RGB histogram of the original image.
- **Object Detection**: Detect and count shapes in the image.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Houssem70/Image_Processing_GUI.git
    cd Image_Processing_GUI
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Use the interface** to:
   - Click "Import Image" to load an image.
   - Click "Convert B/W" to convert it to grayscale.
   - Click "Edge Detection" to perform edge detection.
   - View the RGB histogram and detected objects count.

## Dependencies

The project requires the following Python libraries:
- **PyQt5**
- **PIL (Pillow)**
- **OpenCV**
- **Matplotlib**

These can be installed using the `requirements.txt` file.

## Screenshot

Here’s a screenshot of the application in action:

![Image Processing Application](screenshot.png)


