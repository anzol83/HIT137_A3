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

