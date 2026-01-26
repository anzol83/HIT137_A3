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

        
    def blur(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.blur()


    def edges(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.edges()


    def rotate_90(self):
       if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.rotate(angle=90)
       
        # to do
    def flip_horizontal(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.processor.flip(horizontal=True)


    def brightness(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.brightness_value = int(value)

        
    def scale(self):
        if self.processor.image is None:
            return
        self.processor.scale_value = int(value) / 100


    def undo(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.history.undo(self.processor.image)


    def redo(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        self.processor.image = self.history.redo(self.processor.image)
        