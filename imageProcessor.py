import cv2

class ImageProcessor:
    # A simple OpenCV-based image processor for basic transformations.

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
    
    def blur(self, k=11):
        return cv2.GaussianBlur(self.image, (k, k), 0)

    def edges(self):
        gray = self.grayscale()
        return cv2.Canny(gray, 100, 200)
    
    def brightness(self, img, value):   # to accept img
        return cv2.convertScaleAbs(img, alpha=1, beta=value)
    
    def rotate(self, angle):
        if angle == 90:
            return cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        if angle == 180:
            return cv2.rotate(self.image, cv2.ROTATE_180)
        if angle == 270:
            return cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return self.image  # Return original if angle doesn't match

    def flip(self, mode):
        return cv2.flip(self.image, mode)

    def resize(self, img, scale):      # to accept img first
        h, w = img.shape[:2]
        new_w, new_h = int(w * scale), int(h * scale)
        return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    
    def apply_all(self):
        img = self.original.copy()     

        if self.brightness_value != 0:
            img = self.brightness(img, self.brightness_value)  

        if self.scale_value != 1.0:
            img = self.resize(img, self.scale_value)           

        self.image = img
        return img
