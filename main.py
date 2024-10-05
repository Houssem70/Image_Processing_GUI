import sys
from PyQt5 import QtWidgets
from ui import Ui_Form  # Import the UI class from the generated UI file
from image_processing import ImageProcessor  # Import the image processing class
from PyQt5.QtGui import QPixmap  # Import QPixmap to handle image display

class MainApp(QtWidgets.QWidget):
    def __init__(self):
        """
        Initialize the main application window and connect UI buttons to functions.
        """
        super().__init__()
        self.ui = Ui_Form()  # Set up the UI
        self.ui.setupUi(self)  # Set up widgets and layout

        self.processor = ImageProcessor()  # Initialize the image processor object

        # Connect buttons to corresponding functions
        self.ui.ImportButton.clicked.connect(self.load_image)  # Load image when clicked
        self.ui.ConvertButton.clicked.connect(self.convert_image)  # Convert image to grayscale when clicked
        self.ui.EdgeButton.clicked.connect(self.detect_edges)  # Detect edges when clicked

    def load_image(self):
        """
        Load an image using the ImageProcessor, display it, and show its size.
        """
        self.processor.load_image()  # Load the image from the file dialog
        self.ui.ColorImage.setPixmap(QPixmap(self.processor.imagepath))  # Display the original image
        self.ui.size.setText(f"Image size: {self.processor.img.size}")  # Display image size

        # Calculate and display the histogram of the image
        self.processor.calculate_histogram()
        self.ui.hist.setPixmap(QPixmap("hist.jpg"))  # Display the histogram image

    def convert_image(self):
        """
        Convert the loaded image to grayscale and display it.
        """
        self.processor.convert_to_grayscale()  # Convert the image to grayscale
        self.ui.GrayImage.setPixmap(QPixmap('gray.jpg'))  # Display the grayscale image

    def detect_edges(self):
        """
        Perform edge detection on the grayscale image, display the result, and show the number of detected objects.
        """
        self.processor.perform_edge_detection()  # Apply edge detection
        self.ui.EdgeDetection.setPixmap(QPixmap('edge.jpg'))  # Display the edge-detected image
        
        # Detect shapes and display the number of detected objects
        contours = self.processor.detect_shapes()
        self.ui.Nbobj.setText(f"Number of objects detected: {len(contours)}")

if __name__ == "__main__":
    # Create the application and main window
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()  # Instantiate the main app
    main_app.show()  # Show the app window
    sys.exit(app.exec_())  # Start the event loop
