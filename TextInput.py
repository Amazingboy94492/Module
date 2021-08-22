from tkinter import *
from Window import *

class TextInput:
    def __init__(self, x, y, canvas):
        self.x,self.y,self.tk = (x,y,canvas.tk)
        self.id = Entry(self.tk)
        self.id.pack()
        self.id.place(x = self.x, y = self.y)

    def writevalue(self):
        self.value = str(self.id.get())
