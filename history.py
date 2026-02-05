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

def undo(self, current):
    if self.undo_stack and current is not None:
        self.redo_stack.append(current)
        return self.undo_stack.pop()
    return current