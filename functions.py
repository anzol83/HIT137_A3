class Functions:

    def __init__(self, processor, history, display_callback):
        self.processor = processor
        self.history = history
        self.display_callback = display_callback
        
    def grayscale(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.grayscale()
        self.processor.original = self.processor.image.copy()
        self.display(self.processor.image)
        
    def blur(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.blur()
        self.processor.original = self.processor.image.copy()
        self.display(self.processor.image)

    def edges(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.edges()
        self.processor.original = self.processor.image.copy()
        self.display(self.processor.image)

    def rotate_90(self, angle):
       if self.processor.image is None:
            return
       self.history.save(self.processor.image)
       self.processor.image = self.processor.rotate(angle)
       self.processor.original = self.processor.image.copy()
       self.display(self.processor.image)

    def flip_horizontal(self, mode):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.flip(horizontal=True)
        self.processor.original = self.processor.image.copy()
        self.display(self.processor.image)


    def brightness(self, value):
        if self.processor.image is None:
            return
        self.processor.brightness_value = int(value)
        img = self.processor.apply_all()
        self.display(img)
        
    def scale(self, value):
        if self.processor.image is None:
            return
        self.processor.scale_value = int(value) / 100
        img = self.processor.apply_all()
        self.display(img)

    def undo(self):
        if self.processor.image is None:
            return
        self.processor.image = self.history.undo(self.processor.image)
        img = self.processor.apply_all()
        self.display(img)


    def redo(self):
        if self.processor.image is None:
            return
        self.processor.image = self.history.redo(self.processor.image)
        self.processor.original = self.processor.image.copy()
        self.display(self.processor.image)
