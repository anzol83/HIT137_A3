import cv2

class ImageProcessor:
    """A simple OpenCV-based image processor for basic transformations."""

def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.brightness_value = 0
        self.scale_value = 1.0