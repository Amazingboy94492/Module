from tkinter import *
from IMG import *
from Window import *
from Clock import *

class Player:
    def __init__(self, canvas, x, y, image, directions):
        self.canvas = canvas
        self.x, self.y = (x, y)
        self.image = image
        self.dirs = [directions[0], directions[1], directions[2], directions[3]]
        self.id = IMG(self.canvas, self.x, self.y, image_file)
        self.jumping = False

    def draw(self, coords):
        self.id.move(coords[0], coords[1])
        self.canvas.calibrate()
    
    def forward(self, event = None):
        if self.dirs[0] == "forward":
            self.draw([0, -1])

    def backward(self, event = None):
        if self.dirs[1] == "backward":
            self.draw([0, 1])

    def leftward(self, event = None):
        self.draw([-1, 0])

    def rightward(self, event = None):
        self.draw([1, 0])

    def upward(self, event = None):
        if self.dirs[0] == "upward":
            self.draw([0, -1])

    def downward(self, event = None):
        if self.dirs[1] == "downward":
            self.draw([1, -1])

    def jump(self, event = None):
        if self.dirs[1] == "downward":
            if self.jumping == False:
                self.jumping = True
                self.speed = -2
                for self.counter in range(0, 40):
                    self.draw([0, self.speed])
                    self.speed += 0.05
                    Clock.wait(0.005)
                self.speed = 2
                for self.counter in range(0, 40):
                    self.draw([0, self.speed])
                    self.speed -= 0.05
                    Clock.wait(0.005)
                self.jumping = False

window = Window(500, 500)
image_file = PhotoImage(file = "/Users/ArjunNara/Desktop/Programming/Python/GUI/Tkinter/Pictures/avatar.gif")
player = Player(window, 250, 250, image_file, ["upward", "downward", "leftward", "rightward"])
window.key("<space>", player.jump)
