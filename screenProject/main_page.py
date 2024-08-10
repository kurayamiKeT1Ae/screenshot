from tkinter import *
import customtkinter
from screeninfo import get_monitors
from PIL import ImageGrab
from photo_page import PhotoPage
from pyautogui import screenshot
from tmath import Point

class MainPage:

    def __init__(self) -> None:
        # set page setting
        self.wScale, self.hScale = [get_monitors()[0].width, get_monitors()[0].height]
        self.root = customtkinter.CTk() 
        self.root.wm_attributes('-fullscreen', 'True')

        # set page size
        x_cordinate = int((self.wScale/2) - (self.wScale/2))
        y_cordinate = int((self.hScale/2) - (self.hScale/2))
        self.root.geometry("{}x{}+{}+{}".format(self.wScale, self.hScale, x_cordinate, y_cordinate))
        self.root.attributes('-alpha', 0.55) # .55

        # set the class Variables
        self.points = []
        self.curMouseX, self.curMouseY = 0, 0
        self.bClicked = False
        self.curLine = None # 

        # set the class canvas
        self.canvas = customtkinter.CTkCanvas(self.root, width=self.wScale, height=self.hScale, bg="gray")




    def makeRectangle(self, canvas:customtkinter.CTkCanvas ,p1: Point, p2: Point, color: str="red", width: int=7):
        return canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, outline=color, width=width)
        


    def events(self):
        self.root.bind("<Escape>", exit) # exit if <ESC> pressed
        self.root.bind('<Motion>', self.motion) # get mouse location
        self.root.bind("<ButtonPress-1>", self.buttonClicked) # get first mouse button click
        self.root.bind("<ButtonRelease-1>", self.buttonReleased) # get last mouse click while pressed



    def buttonClicked(self, event):
        if len(self.points) < 1:
            self.points.append(Point((self.curMouseX, self.curMouseY)))
            self.bClicked = True

    def buttonReleased(self, event):
        if len(self.points) == 1:
            self.points.append(Point((self.curMouseX, self.curMouseY)))
            self.bClicked = False


            # snapshot after release button
            p1, p2 = self.points 
            self.getScreenShot(p1.x, p1.y, p2.x, p2.y)



    def motion(self, event):
        if self.curLine and self.bClicked:
            self.canvas.delete(self.curLine)
        x, y = event.x, event.y
        self.curMouseX = x
        self.curMouseY = y
        if self.bClicked:
            self.curLine = self.makeRectangle(self.canvas, self.points[0], Point((self.curMouseX, self.curMouseY)))
            # print(self.curLine)


    def getScreenShot(self, x1, y1, x2, y2):
        self.root.destroy()
        snap = screenshot()

        snaphandlePoints = Point.handlePoints((x1, y1), (x2, y2))
        x1, y1 = snaphandlePoints["p1"].list
        x2, y2 = snaphandlePoints["p2"].list
        width, height = snaphandlePoints["scale"]

        snap = snap.crop(box=(x1, y1, x2, y2))
        
        # snap.show()
        self.root.quit()

        snap.resize((width, height))

        _ppage = PhotoPage(snap, (width, height))
        _ppage.run()



    def run(self):
        self.canvas.pack()

        self.events()
        self.root.mainloop()
