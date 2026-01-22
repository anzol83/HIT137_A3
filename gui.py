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
        panel=tk.Frame(main)
        panel.pack(side=tk.BOTTOM)

        tk.Button(panel, text="Greyscale").pack(side=tk.LEFT, padx=15, pady=15)
        tk.Button(panel, text="Blur").pack(side=tk.LEFT, padx=15, pady=15)
        tk.Button(panel, text="Edges").pack(side=tk.LEFT, padx=15, pady=15)
        tk.Button(panel, text="Rotate").pack(side=tk.LEFT, padx=15, pady=15)
        tk.Button(panel, text="Flip").pack(side=tk.LEFT, padx=15, pady=15)
