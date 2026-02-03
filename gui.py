import tkinter as tk
import cv2
from PIL import Image, ImageTk

from tkinter import filedialog, messagebox
from functions import Functions

class gui_system():
    def __init__(self, root):
        self.root=root
        self.root.title("Image Editor")
        self.root.geometry("600x400")

        self.func=Functions(self, self, self.display)
        
        self.window()
        self.layout()
        self.status_bar()

    def window(self):
        menu = tk.Menu(self.root)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save As", command=self.run)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.run)

        edit_menu=tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.run)
        edit_menu.add_command(label="Redo", command=self.run)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menu)

    def layout(self):
        main=tk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)
        panel=tk.Frame(main, width=200)
        panel.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(panel, text="Greyscale", command=self.func.grayscale).pack(fill=tk.X, padx=15, pady=5)
        tk.Button(panel, text="Blur").pack(fill=tk.X, padx=15, pady=5)
        tk.Button(panel, text="Edges").pack(fill=tk.X, padx=15, pady=5)
        tk.Button(panel, text="Rotate 90°").pack(fill=tk.X, padx=10, pady=5)
        tk.Button(panel, text="Flip Horizontal").pack(fill=tk.X, padx=10, pady=5)

        canvas_frame=tk.Frame(main)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas=tk.Canvas(canvas_frame, bg="black")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        slider=tk.Frame(canvas_frame, height=80, bg="#dddddd")
        slider.pack(side=tk.TOP, fill=tk.Y)

        self.slider = tk.Scale(slider, from_=-100, to=100,
                                orient=tk.VERTICAL,
                                label="Brightness",
                                command=self.run)
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

        self.scale=tk.Scale(slider, from_=10, to=200,
                                        orient=tk.VERTICAL,
                                        label="Scale (%)",
                                        command=self.run)
        self.scale.set(100)
        self.scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

    def display(self, img):

        if len(img.shape)==2:
            img=cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(img)
        self.tk_img = ImageTk.PhotoImage(im)

        self.canvas.delete("all")
        self.canvas.create_image(10, 10, anchor=tk.NW, image=self.tk_img)
        self.last_displayed_image=img
        return img

    def status_bar(self):
        self.status=tk.Label(self.root, text="No image loaded",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def display(self, img):
        if len(img.shape)==2:
            img=cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        im=Image.fromarray(img)
        self.tk_img=ImageTk.PhotoImage(im)

        self.canvas.delete("all")
        self.canvas.create_image(10, 10, anchor=tk.NW, image=self.tk_img)
        self.last_displayed_image=img
        return img

    def open_image(self):
        path=filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.png *.bmp")]
        )
        if path:
            img=self.load_image(path)

            self.display(img)

            h, w=img.shape[:2]
            self.status.config(text=f"{path} | {w} x {h}")
            
    def run(self):
        return print("this is a test")
    
    def load_image(self, path):
        self.image=cv2.imread(path)
        if self.image is None:
            raise ValueError("Failed to load image")

        self.original=self.image.copy()
        self.filename=path

        self.brightness_value=0
        self.scale_value=1.0

        return self.image