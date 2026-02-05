"""
This code contains a class for managing undo and redo functionalities
"""

class History:
    """
    This class has 2 stacks:
    undo_stack stores previous image state for undo function
    redo_stack stores undone image state for redo function
    """

    def __init__(self):
        #Initializing the history class with empty undo & redo stack list
        self.undo_stack = []
        self.redo_stack = []


    def save(self, image):
        if image is None:
            return
        
        #storing a copy of image to avoid mutating saved states
        self.undo_stack.append(image.copy())

        #clearing redo history after new action
        self.redo_stack.clear()

    def undo(self, current):
        """
        Reverting to previous image state
        
        Current image is pushed to redo stack
        And most recent image state from undo stack is returned.
        :param current: Current image state
        :return: The previous image state if available,
                 otherwise the current image
        """
        if self.undo_stack and current is not None:

            #save current state for redo
            self.redo_stack.append(current)
            
            #restore last saved state
            return self.undo_stack.pop()
        return current

    def redo(self, current):
        if self.redo_stack and current is not None:
            self.undo_stack.append(current)
            return self.redo_stack.pop()
        return current