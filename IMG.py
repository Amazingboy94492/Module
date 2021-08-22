from tkinter import *
from Window import *

class IMG:
    def __init__(self, canvas, x, y, image):
        self.x,self.y,self.image,self.canvas = (x,y,image,canvas.canvas)
        self.id = self.canvas.create_image(self.x, self.y, image = self.image)

    def move(self, x, y):
        self.canvas.move(self.id, x, y)

    def delete(self):
        self.canvas.delete(self.id)

    def drag(self, x, y):
        px = self.canvas.coords(self.id)[0]
        py = self.canvas.coords(self.id)[1]
        while px != x or py != y:
            if x > px:
                self.canvas.move(self.id, 1, 0)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
            else:
                self.canvas.move(self.id, -1, 0)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
            if y > py:
                self.canvas.move(self.id, 0, 1)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
            else:
                self.canvas.move(self.id, 0, -1)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
                
        px = str(self.canvas.coords(self.id)[0])
        py = str(self.canvas.coords(self.id)[1])
        print("x = " + px + ", y = " + py)
