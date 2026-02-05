#This is the main system for the application
#Importing tkinter, PIL and cv2 (OpenCV) which are requirements of the assignment
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

#We are importing all the module we created for the application here
#This helps to easily call the functions and keep track of errors
from imageProcessor import ImageProcessor
from history import History
from functions import Functions

#Creating the GUI systemfor the app
#This contains layout and menu for the user interaction
class gui_system:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenCV Image Editor")
        self.root.geometry("1000x600")

        self.processor = ImageProcessor()
        self.history = History()

        self.function = Functions(self.processor, self.history, self.display)


        self.layout()
        self.window()
        self.status_bar()

    #This function cotains the menu bar
    #Which contains options like open, save, exit and undo/redo fuctions
    def window(self):
        menu = tk.Menu(self.root)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save As", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu=tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.function.undo)
        edit_menu.add_command(label="Redo", command=self.function.redo)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menu)

    #This function contain the layout of the application, positions of buttons, sliders and canvas
    #Each buttons are assigned for the respective functions (for eg: button "Grayscale" calls function "grayscale" from another module)
    def layout(self):
        main = tk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)

        panel = tk.Frame(main, width=200, bg="#eeeeee")
        panel.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(panel, text="Grayscale", command=self.function.grayscale).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(panel, text="Blur", command=self.function.blur).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(panel, text="Edges", command=self.function.edges).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(panel, text="Rotate 90°", command=lambda: self.function.rotate_90(90)).pack(fill=tk.X, padx=10, pady=5)
        tk.Button(panel, text="Flip Horizontal", command=lambda: self.function.flip_horizontal(1)).pack(fill=tk.X, padx=10, pady=5)

        #adding canvas - part of window is seperated for image to load and display
        canvas_frame = tk.Frame(main)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(canvas_frame, bg="lightgrey")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        slider_panel = tk.Frame(canvas_frame, height=80, bg="#dddddd")
        slider_panel.pack(side=tk.TOP, fill=tk.X)

        self.slider = tk.Scale(slider_panel, from_=-100, to=100,
                                orient=tk.HORIZONTAL,
                                label="Brightness",
                                command=self.function.brightness)
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

        self.scale_slider = tk.Scale(slider_panel, from_=10, to=200,
                                        orient=tk.HORIZONTAL,
                                        label="Scale (%)",
                                        command=self.function.scale)
        self.scale_slider.set(100)
        self.scale_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

    #Status bar on the bottom of the window to show information while running the program
    def status_bar(self):
        self.status = tk.Label(self.root, text="No image loaded",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    #this function shows the image opened for edit
    def display(self, img):
        #while openening the image for display the color are not matched by default
        #cvtcolor function helps to disply that image in it's original form
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(img)
        self.tk_img = ImageTk.PhotoImage(im)

        self.canvas.delete("all")
        self.canvas.create_image(10, 10, anchor=tk.NW, image=self.tk_img)
        #we used "last_displayed_image" as variable to keep track of the image edited 
        self.last_displayed_image=img
        return img

    #This function opens the file explorer to get and load the image to display and edit
    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.png *.bmp")]
        )
        if path:
            img = self.processor.load_image(path)

            self.slider.set(0)
            self.scale_slider.set(100) 

            self.history.save(img)
            self.display(img)

            h, w = img.shape[:2]
            self.status.config(text=f"{path} | {w} x {h}")

    #finally when the image is edited the last_displayed_image is always the final edit
    #we use that edited image to save to the desired path
    def save_image(self):
        if self.processor.image is None:
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            cv2.imwrite(path, cv2.cvtColor(self.last_displayed_image, cv2.COLOR_RGB2BGR))
            messagebox.showinfo("Saved", "Image saved successfully")
