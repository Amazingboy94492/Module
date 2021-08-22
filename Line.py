from tkinter import *
from Window import *

class Line:
    def __init__(self, canvas, x, y, x2, y2, color = "black", border_weight = 1):
        self.canvas, self.x, self.y, self.x2, self.y2, self.color, self.bw = (canvas.canvas, x, y, x2, y2, color, border_weight)
        self.id = self.canvas.create_line(self.x, self.y, self.x2, self.y2, fill = self.color, width = self.bw)
        self.canvas.update()

    def move(self, x, y):
        self.canvas.move(self.id, x, y)

    def delete(self):
        self.canvas.delete(self.id)
        self.canvas.update()

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
