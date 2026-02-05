"""
This is the main entry point of the application.

Run this program to start the application.

It creates the main Tkinter window, initializes the GUI system, and starts the event loop to run the image editor.
"""

import tkinter as tk
from gui import gui_system

if __name__ == "__main__":
    root = tk.Tk()
    app = gui_system(root)
    root.mainloop()
