import tkinter as tk
import cv2
from PIL import Image, ImageTk

from functions import Functions

class gui_system():
    def __init__(self, root):
        self.root=root
        self.root.title("Image Editor")
        self.root.geometry("600x400")

        self.func=Functions(self, self, self.display)
        
        self.window()
        self.layout()
    
    def window(self):
        menu=tk.Menu(self.root)
        
        file_menu=tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save As")
        file_menu.add_command(label="Exit")

        menu.add_cascade(label="File")
        menu.add_cascade(label="Edit")

        self.root.config(menu=menu)

    def layout(self):
        main=tk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)
        panel=tk.Frame(main, width=200)
        panel.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(panel, text="Greyscale").pack(fill=tk.X, padx=15, pady=5)
        tk.Button(panel, text="Blur").pack(fill=tk.X, padx=15, pady=5)
        tk.Button(panel, text="Edges").pack(fill=tk.X, padx=15, pady=5)
        tk.Button(panel, text="Rotate 90°").pack(fill=tk.X, padx=10, pady=5)
        tk.Button(panel, text="Flip Horizontal").pack(fill=tk.X, padx=10, pady=5)

        canvas_frame=tk.Frame(main)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas=tk.Canvas(canvas_frame, bg="black")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_status_bar(self):
        self.status = tk.Label(self.root, text="No image loaded",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def display(self, img):

        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(img)
        self.tk_img = ImageTk.PhotoImage(im)

        self.canvas.delete("all")
        self.canvas.create_image(10, 10, anchor=tk.NW, image=self.tk_img)
        self.last_displayed_image=img
        return img