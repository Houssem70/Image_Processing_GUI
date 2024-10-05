from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageFilter
import cv2
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self):
        # Initialize attributes to hold image path, image, and grayscale image
        self.imagepath = None
        self.img = None
        self.imagegray = None

    def load_image(self):
        """
        Opens a file dialog for the user to select an image and loads it.
        The image is stored as a PIL Image object.
        """
        Tk().withdraw()  # Hide the main tkinter window
        self.imagepath = askopenfilename()  # Show file dialog to select an image
        self.img = Image.open(self.imagepath)  # Open and load the selected image

    def calculate_histogram(self):
        """
        Calculates and plots the color histogram of the loaded image.
        The histogram is saved as 'hist.jpg'.
        """
        img = cv2.imread(self.imagepath)  # Load the image using OpenCV
        colors = ('b', 'g', 'r')  # Define the color channels (blue, green, red)
        
        # Loop through each color channel and calculate the histogram
        for i, color in enumerate(colors):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(hist, color=color)  # Plot the histogram for each color
        
        plt.title('Image Histogram')  # Set the title for the plot
        plt.savefig("hist.jpg")  # Save the histogram plot as an image
        plt.clf()  # Clear the current figure
        plt.cla()  # Clear the axes

    def convert_to_grayscale(self):
        """
        Converts the loaded image to grayscale and saves it as 'gray.jpg'.
        """
        self.imagegray = self.img.convert('L')  # Convert the image to grayscale (L mode)
        path = 'gray.jpg'
        self.imagegray.save(path)  # Save the grayscale image

    def perform_edge_detection(self):
        """
        Applies edge detection to the grayscale image using PIL's FIND_EDGES filter.
        The resulting image is saved as 'edge.jpg'.
        """
        imageEdge = self.imagegray.filter(ImageFilter.FIND_EDGES)  # Apply edge detection filter
        path = 'edge.jpg'
        imageEdge.save(path, 'JPEG', quality=88)  # Save the edge-detected image

    def detect_shapes(self):
        """
        Detects shapes/contours in the loaded image by converting it to binary.
        Returns a list of contours found in the image.
        """
        img = cv2.imread(self.imagepath)  # Load the image using OpenCV
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # Apply binary thresholding
        
        # Find contours of the shapes in the image
        cnts, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return cnts  # Return the list of detected contours
