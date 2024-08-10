from tkinter import *
import customtkinter
from screeninfo import get_monitors
from PIL import ImageGrab, ImageTk, Image
from tmath import Point


class PhotoPage:

    def __init__(self, photo: Image, scale: tuple) -> None:
        # set page setting
        width, height = scale
        self.root = customtkinter.CTk() 
        self.root.geometry("{}x{}+{}+{}".format(width, height, 0, 0))


        # show image
        _image = customtkinter.CTkImage(dark_image=photo, size=(width, height))
        label = customtkinter.CTkLabel(self.root, image=_image, text='')
        label.pack()


    def run(self):
        self.root.mainloop()