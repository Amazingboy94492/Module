from tkinter import *
import time

class Window:
    def __init__(self, width = 0, height = 0, color = "white", title = "Untitled"):
        self.width,self.height,self.color,self.title = (width, height, color, title)
        self.tk = Tk()
        self.tk.title(self.title)
        self.canvas = Canvas(self.tk, height = self.height, width = self.width, bg = self.color)
        self.canvas.pack()
        self.canvas.update()
        self.o = self.canvas.create_text(self.width / 2, 100, text = "id " + str(self))
        self.t = self.canvas.create_text(self.width / 2, 120, text = " name " + title + " __init__ = True" + " qd ")
        self.th = self.canvas.create_text(self.width / 2, 140, text = str(self.width) + " " + str(self.height))
        self.f = self.canvas.create_text(self.width / 2, 160, text = " ###### " + self.color + " str value printing " + " P = True")
        self.canvas.update()
        time.sleep(0.001)
        self.canvas.delete(self.o, self.t, self.th, self.f)
        self.height = self.canvas.winfo_height()
        self.width = self.canvas.winfo_width()
    
    def mainloop(self):
        self.canvas.update()
        self.tk.update()
        self.tk.mainloop()

    def key(self, key, function):
        if key == "<Button-1>" or key == "<Button-2>":
            self.canvas.bind(key, function)
        else:
            self.canvas.bind_all(key, function)

    def del_key(self, key):
        if key != "<Motion>":
            self.canvas.unbind(key)
        else:
            self.canvas.unbind_all(key)

    def calibrate(self):
        self.canvas.update()
        self.tk.update()
