import tkinter as tk

class gui_system():
    def __init__(self, root):
        self.root=root
        self.root.title("Image Editor")
        self.root.geometry("600x400")
        
        self.window()
        self.layout()
    
    def window(self):
        menu=tk.Menu(self.root)
        
        menu.add_cascade(label="File")
        menu.add_cascade(label="Edit")

        self.root.config(menu=menu)

    def layout(self):
        tk.Button(text="Greyscale").pack(side=tk.LEFT)
        tk.Button(text="Blur").pack(side=tk.LEFT)
        tk.Button(text="Edges").pack(side=tk.LEFT)
        tk.Button(text="Rotate").pack(side=tk.LEFT)
        tk.Button(text="Flip").pack(side=tk.LEFT)
