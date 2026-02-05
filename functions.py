from tkinter import messagebox

class Functions: # This class controls user actions and connects them to image processing and display.

    def __init__(self, processor, history, display_callback):
        # processor: does the actual image editing (grayscale, blur, etc.)
        # history: stores previous images for undo and redo
        # display_callback: function used to show the image on the screen
        self.processor = processor
        self.history = history
        self.display_callback = display_callback
        
    def grayscale(self):
        if self.processor.image is None: # If no image is loaded, do nothing
            return messagebox.showwarning("Warning", "No image loaded.") #In case if no inmage is loaded, show a warning message
        self.history.save(self.processor.image)  # Save current image so we can undo later
        self.processor.image = self.processor.grayscale() # Convert the image to grayscale
        self.processor.original = self.processor.image.copy() # Store a clean copy as the new original image
        self.display(self.processor.image) # Display the updated image
        
    def blur(self):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.history.save(self.processor.image) # Save current state before applying blur
        self.processor.image = self.processor.blur() # Apply blur effect
        self.processor.original = self.processor.image.copy() # Update original image after blur
        self.display(self.processor.image) # Display the blurred image

    def edges(self):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.history.save(self.processor.image) # Save image for undo
        self.processor.image = self.processor.edges()  # Detect edges in the image
        self.processor.original = self.processor.image.copy() # Update original image
        self.display(self.processor.image) # Display the edge-detected image

    def rotate_90(self, angle):
       if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
       self.history.save(self.processor.image) # Save current image before rotation
       self.processor.image = self.processor.rotate(angle) # Rotate the image by the specified angle
       self.processor.original = self.processor.image.copy() # Update original image after rotation
       self.display(self.processor.image) # Display the rotated image

    def flip_horizontal(self, mode):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.history.save(self.processor.image) # Save current image before flipping
        self.processor.image = self.processor.flip(horizontal=True) # Flip the image horizontally
        self.processor.original = self.processor.image.copy() # Update original image after flip
        self.display(self.processor.image) # Display the flipped image


    def brightness(self, value):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.processor.brightness_value = int(value) / 100 # Set brightness level
        img = self.processor.apply_all() # Reapply all effects including brightness
        self.display(img) # Display the updated image
        
    def scale(self, value):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.processor.scale_value = int(value) / 100 # Set scale level
        img = self.processor.apply_all() # Reapply all effects including scaling
        self.display(img) # Display the updated image

    def undo(self):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.processor.image = self.history.undo(self.processor.image) # Revert to previous image state
        img = self.processor.apply_all() # Reapply all effects to the undone image
        self.display(img) # Display the undone image


    def redo(self):
        if self.processor.image is None:
            return messagebox.showwarning("Warning", "No image loaded.")
        self.processor.image = self.history.redo(self.processor.image) # Reapply the next image state
        self.processor.original = self.processor.image.copy() # Update original image
        self.display(self.processor.image) # Display the redone image
