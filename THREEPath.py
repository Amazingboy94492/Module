from tkinter import *
from Window import *
class THREEPath:
    def __init__(self, canvas, x, x21, bY2a1, sub1, sub2, border_color = "black", borderweight1 = 1, borderweight2 = 1):
        self.canvas,self.x,self.x21,self.border_color, self.bY2a1, self.sub1, self.sub2, self.borderweight1, self.borderweight2 = (canvas, x, x21, border_color, bY2a1, sub1, sub2, borderweight1, borderweight2)
        self.canvasH = self.canvas.height
        self.id1 = self.canvas.canvas.create_line(self.x, self.canvasH, self.x + self.sub1, self.bY2a1, fill = self.border_color, width = self.borderweight1)
        self.id2 = self.canvas.canvas.create_line(self.x21, self.canvasH, self.x21 - self.sub2, self.bY2a1, fill = self.border_color, width = self.borderweight2)

    def delete(self):
        self.canvas.canvas.delete(self.id1)
        self.canvas.canvas.delete(self.id2)
