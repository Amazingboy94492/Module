from tkinter import *
from Window import *
class Btn:
    def __init__(self, canvas, x, y, width, height, text, bg = "black", fg = "white", command = None, type = "raised"):
        self.canvas, self.x, self.y, self.width, self.height, self.bg, self.fg, self.command, self.type, self.text = (canvas, x, y, width, height, bg, fg, command, type, text)
        print(self.canvas)
        self.tk = self.canvas.tk
        self.id = Button(self.tk, text = self.text, bg = self.bg, fg = self.fg, height = self.height, width = self.width, relief = self.type, command = self.command)
        self.id.pack()
        self.finalx = self.x
        self.finaly = self.y
        self.id.place(x = self.finalx, y = self.finaly)

    def move(self, x, y):
        self.finalx = self.x
        self.finaly = self.y
        self.id.place(x = self.finalx, y = self.finaly)

    def delete(self):
        self.id.destroy()
