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
        self.display_callback(self.processor.image)
        # to do
    def blur(self):

    def edges(self):

    def rotate_90(self):
        # to do
    def flip_horizontal(self):

    def brightness(self):
        # to do
    def scale(self):

    def undo(self):
        # to do
    def redo(self):
    

    