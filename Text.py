from tkinter import *
from Window import *

class Text:
    def __init__(self, canvas, x, y, text, color = "black", font = "Helvetica", size = 20):
        self.x,self.y,self.text,self.color,self.canvas, self.size, self.font = (x,y,text,color,canvas.canvas, size, font)
        self.id = self.canvas.create_text(self.x, self.y, text = self.text, fill=self.color, font = (self.font, self.size))
        self.canvas.update()

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
