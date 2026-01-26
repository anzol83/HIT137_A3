class Functions:

    def __init__(self, processor, history, display_callback):
        self.processor = processor
        self.history = history
        self.display_callback = display_callback
        
    def grayscale(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)

        
    def blur(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)


    def edges(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)


    def rotate_90(self):
       if self.processor.image is None:
            return
        self.history.save(self.processor.image)
       
        # to do
    def flip_horizontal(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)


    def brightness(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)
        
        
    def scale(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)


    def undo(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)

        
    def redo(self):
        if self.processor.image is None:
            return
        self.history.save(self.processor.image)

    