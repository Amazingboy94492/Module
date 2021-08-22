from tkinter import *
from Code_17 import *
class THREEPlayer:
    def __init__(self, canvas, list):
        self.canvas, self.list = (canvas.canvas, list)
        self.cn = len(self.list) - 1
        self.cZ = 1
        self.cX = 1
        self.x = 0
        self.y = 0
        self.z = 0
        self.rotation = 0

    def forward(self, event = None):
        self.cZ = -10
        self.counter = 0
        for self.i in range(self.cn + 1):
            self.list[self.counter].move(0, 0, 0, 0, self.cZ)
            self.counter += 1
        self.counter = 0

    def backward(self, event = None):
        self.counter = 0
        self.cZ = 10
        for self.i in range(self.cn + 1):
            self.list[self.counter].move(0, 0, 0, 0, self.cZ)
            self.counter += 1

    def leftward(self, event = None):
        self.cX = -10
        self.counter = 0
        for self.i in range(self.cn + 1):
            self.list[self.counter].move(self.cX, 0, self.cX, 0, 0)
            self.counter += 1
        self.counter = 0

    def rightward(self, event = None):
        self.cX = 10
        self.counter = 0
        for self.i in range(self.cn + 1):
            self.list[self.counter].move(self.cX, 0, self.cX, 0, 0)
            self.counter += 1
        self.counter = 0

    def rotate_right(self, event = None):
        self.counter = 0
        for self.i in range(self.cn + 1):
            self.list[self.counter].rotate("right")
            self.counter += 1
        self.counter = 0

    def rotate_left(self, event = None):
        self.counter = 0
        for self.i in range(self.cn + 1):
            self.list[self.counter].rotate("left")
            self.counter += 1
        self.counter = 0
