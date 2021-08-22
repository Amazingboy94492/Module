from tkinter import *
from Code_17 import *
class THREEWall:
    def __init__(self, canvas, x, y, x2, y2, z, list, wall, color = "black"):
        self.canvas, self.x, self.y, self.x2, self.y2, self.z, self.color, self.list, self.wall = (canvas.canvas, x, y, x2, y2, z, color, list, wall)
        self.Fx = self.x + self.z
        self.Fy = self.y + self.z
        self.Fx2 = self.x2 - self.z
        self.Fy2 = self.y2 - self.z
        self.Fx3 = self.Fx2
        self.Fy3 = self.Fy
        self.Fx4 = self.Fx
        self.Fy4 = self.Fy2
        self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx2, self.Fy, self.Fx2, self.Fy2, self.Fx, self.Fy2, fill = self.color, width = 0)
        self.list.append(self)
        self.cx = 200
        self.cy = 0
        self.cz = self.z
        self.rot = 0
        self.rrot = 0
        self.lrot = 0

    def rotate(self, way):
        self.dir = way
        if self.dir == "right":
            if self.lrot > 0:
                self.lrot -= 1
                self.x -= 2
                self.y -= 2
                self.x2 -= 8
                self.y2 -= 8
                self.Fx -= 2
                self.Fy -= 2
                self.Fx2 -= 8
                self.Fy2 -= 8
                self.Fx3 -= 8
                self.Fy3 += 8
                self.Fx4 -= 2
                self.Fy4 += 2
                self.rot += 1
                self.canvas.delete(self.id)
                self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx3, self.Fy3, self.Fx2, self.Fy2, self.Fx4, self.Fy4, fill = self.color, width = 0)
            self.rrot += 1
            self.x -= 8
            self.y -= 8
            self.x2 -= 2
            self.y2 -= 2
            self.Fx -= 8
            self.Fy -= 8
            self.Fx2 -= 2
            self.Fy2 -= 2
            self.Fx3 -= 2
            self.Fy3 += 2
            self.Fx4 -= 8
            self.Fy4 += 8
            self.rot += 1
            self.canvas.delete(self.id)
            self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx3, self.Fy3, self.Fx2, self.Fy2, self.Fx4, self.Fy4, fill = self.color, width = 0)
        elif self.dir == "left":
            if self.rrot > 0:
                self.rrot += 1
                self.x += 8
                self.y += 8
                self.x2 += 2
                self.y2 += 2
                self.Fx += 8
                self.Fy += 8
                self.Fx2 += 2
                self.Fy2 += 2
                self.Fx3 += 2
                self.Fy3 -= 2
                self.Fx4 += 8
                self.Fy4 -= 8
                self.rot -= 1
                self.canvas.delete(self.id)
                self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx3, self.Fy3, self.Fx2, self.Fy2, self.Fx4, self.Fy4, fill = self.color, width = 0)
            self.lrot += 1
            self.x += 2
            self.y += 2
            self.x2 += 8
            self.y2 += 8
            self.Fx += 2
            self.Fy += 2
            self.Fx2 += 8
            self.Fy2 += 8
            self.Fx3 += 8
            self.Fy3 -= 8
            self.Fx4 += 2
            self.Fy4 -= 2
            self.rot -= 1
            self.canvas.delete(self.id)
            self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx3, self.Fy3, self.Fx2, self.Fy2, self.Fx4, self.Fy4, fill = self.color, width = 0)
        
    def move(self, x, y, x2, y2, z):
        # if player is not touching wall
        if self.z > -200:
            self.blank = False
            self.x = self.x + x
            self.y = self.y + y
            self.x2 = self.x2 + x2
            self.y2 = self.y2 + y2
            self.z = self.z + z
            self.Fx = self.x + self.z
            self.Fy = self.y + self.z
            self.Fx2 = self.x2 - self.z
            self.Fy2 = self.y2 - self.z
            self.canvas.delete(self.id)
            self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx2, self.Fy, self.Fx2, self.Fy2, self.Fx, self.Fy2, fill = self.color, width = 0)
        else:
            if self.wall == False:
                self.blank = True
                self.x = self.x + x
                self.y = self.y + y
                self.x2 = self.x2 + x2
                self.y2 = self.y2 + y2
                self.z = self.z + z
                self.Fx = self.x + self.z
                self.Fy = self.y + self.z
                self.Fx2 = self.x2 - self.z
                self.Fy2 = self.y2 - self.z
                self.canvas.delete(self.id)
            else:
                if self.z == -200:
                    # check if you are moving forward or backwards
                    possibleZ = self.z + z
                    if possibleZ > -200:
                        # you are going backwards, create rectangle
                        self.x = self.x + x
                        self.y = self.y + y
                        self.x2 = self.x2 + x2
                        self.y2 = self.y2 + y2
                        self.z = self.z + z
                        self.Fx = self.x + self.z
                        self.Fy = self.y + self.z
                        self.Fx2 = self.x2 - self.z
                        self.Fy2 = self.y2 - self.z
                        self.canvas.delete(self.id)
                        self.id = self.canvas.create_polygon(self.Fx, self.Fy, self.Fx2, self.Fy, self.Fx2, self.Fy2, self.Fx, self.Fy2, fill = self.color, width = 0)
                    else:
                        # you are hitting a wall
                        pass

    def delete(self):
        self.canvas.delete(self.id)
