import cv2

class ImageProcessor:
    """A simple OpenCV-based image processor for basic transformations."""

    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.brightness_value = 0
        self.scale_value = 1.0

    def load_image(self, path):
        self.image = cv2.imread(path)
        if self.image is None:
            raise ValueError("Failed to load image")

        self.original = self.image.copy()    
        self.filename = path

        #this is to reset adjustments on new image
        self.brightness_value = 0
        self.scale_value = 1.0

        return self.image
    
    def grayscale(self): 
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
