"""
Adding saving option 
"""
def __init__(self):
    self.undo_stack = []
    self.redo_stack = []


def save(self, image):
    if image is None:
        return
    self.undo_stack.append(image.copy())
    self.redo_stack.clear()