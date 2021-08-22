import pygame
import sys
from playsound import playsound as ps
pygame.joystick.init()

class Script:
    class OP:
        Write = lambda Value: print(Value)

        def Alert(Value):
            ps("/Users/ArjunNara/Desktop/Programming/Python/GUI/Tkinter/GameCode/PING.mp3", True)
            print("NOTICE: " + Value)

        def Warning(Value, Pre = ""):
            ps("/Users/ArjunNara/Desktop/Programming/Python/GUI/Tkinter/GameCode/ALARM.mp3", True)
            print(Pre + " " + Value)

        Sound = lambda path, wait: ps(path, wait)

    def Path(path):
        sys.path.insert(0, path)

    class Errors:
        def Cause(error_type, error):
            raise error_type(error)

    class External:
        class Devices:
            class Xbox_Controller:
                def __init__(self, index):
                    self.index = index
                    self.controller = pygame.joystick.Joystick(self.index)

                def Init(self):
                    self.controller.init()

                def get_joy_rot(self, index):
                    self.index = index
                    if self.index == 1:
                        self.c1 = str(self.controller.get_axis(self.index + 1))
                        self.c2 = str(self.controller.get_axis(self.index + 2))
                    else:
                        self.c1 = str(self.controller.get_axis(self.index))
                        self.c2 = str(self.controller.get_axis(self.index + 1))
                    self.v1 = ""
                    self.v2 = ""
                    
                    if self.c1[0] == "-":
                        self.v1 = "-"

                    if self.c2[0] == "-":
                        self.v2 = "-"

                    if self.v2 == "-" and self.c2[0:4] in ["-0.6", "-0.7", "-0.8", "-0.9", "-1.0"]:
                        self.y = self.c2[0:4]
                        self.y = str(self.y)
                    elif self.c2[0:3] in ["0.6", "0.7", "0.8", "0.9", "1.0"]:
                        self.y = self.c2[0:3]
                        self.y = str(self.y)
                    else:
                        self.y = "0"

                    if self.v1 == "-" and self.c1[0:4] in ["-0.6", "-0.7", "-0.8", "-0.9", "-1.0"]:
                        self.x = self.c1[0:4]
                        self.x = str(self.x)
                    elif self.c1[0:3] in ["0.6", "0.7", "0.8", "0.9", "1.0"]:
                        self.x = self.c1[0:3]
                        self.x = str(self.x)
                    else:
                        self.x = "0"

                    self.return_value = ((float(self.x) * 10), (float(self.y) * 10))
                    return self.return_value

                def get_button_a(self):
                    self.btn_a = self.controller.get_button(0)
                    if self.btn_a == 1:
                        return True
                    else:
                        return False

                def get_button_b(self):
                    self.btn_b = self.controller.get_button(1)
                    if self.btn_b == 1:
                        return True
                    else:
                        return False

                def get_button_y(self):
                    self.btn_y = self.controller.get_button(4)
                    if self.btn_y == 1:
                        return True
                    else:
                        return False

                def get_button_x(self):
                    self.btn_x = self.controller.get_button(3)
                    if self.btn_x == 1:
                        return True
                    else:
                        return False

                def get_dpad_up(self):
                    self.hat = self.controller.get_hat(0)
                    if self.hat[1] == 1:
                        return True
                    else:
                        return False

                def get_dpad_down(self):
                    self.hat = self.controller.get_hat(0)
                    if self.hat[1] == -1:
                        return True
                    else:
                        return False

                def get_dpad_left(self):
                    self.hat = self.controller.get_hat(0)
                    if self.hat[0] == 1:
                        return True
                    else:
                        return False

                def get_dpad_right(self):
                    self.hat = self.controller.get_hat(0)
                    if self.hat[0] == -1:
                        return True
                    else:
                        return False

                def get_trigger(self, index):
                    if index == 0:
                        self.return_value = self.controller.get_button(4)
                    elif index == 1:
                        self.return_value = self.controller.get_button(5)
                    return self.return_value

                def get_name(self):
                    return self.controller.get_name()

                def get_battery(self):
                    return self.controller.get_power_level()
