"""
This code contains a class for managing saving, undo and redo functionalities
"""

class History:
    """
    This class has 2 stacks:
    undo_stack stores previous image state for undo function
    redo_stack stores undone image state for redo function
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

    def redo(self, current):
        if self.redo_stack and current is not None:
            self.undo_stack.append(current)
            return self.redo_stack.pop()
        return current