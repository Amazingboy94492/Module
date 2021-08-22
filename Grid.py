from tkinter import *
from Window import *

class Grid:
    def __init__(self, canvas, x, y, width, height, map, linebreak, layers, color = "black"):
        self.canvas, self.map, self.x, self.y, self.width, self.height, self.color, self.linebreak, self.layers = (canvas.canvas, map, x, y, width, height, color, linebreak - 1, layers)
        self.linecounter = 0
        self.totalcounter = 0
        self.cutnumber = len(self.map)
        self.counter = 0
        self.fx = 0
        self.fy = 0
        self.idlist = []
        while self.totalcounter < self.cutnumber:
            if self.counter < self.linebreak:
                for self.i in range(self.layers):
                    while self.counter <= self.linebreak:
                        self.id = Quad(self.fx, self.fy, self.fx + self.width, self.fy + self.height, self.color, self.canvas)
                        self.idlist.append(id)
                        self.counter += 1
                        self.totalcounter += 1
                        self.fx += self.width
                    self.fy += self.height
                    self.counter = 0
                    self.fx = 0
                    self.totalcounter += 1
