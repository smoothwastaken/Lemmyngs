import time

import pyxel


class Lemming():
    w = 16
    h = 16

    x = 0
    y = 0

    @classmethod
    def draw(cls, x, y):
        x *= cls.w
        y *= cls.h
        pyxel.blt(x + cls.x, y + cls.y, 0, 32, 32, cls.w, cls.h)

    @classmethod
    def moveRight(cls):
        print("Moving right")
        if cls.x >= 288:
            print("Cannot move more to the right.")
            return False
        else:
            cls.x += 16
            return True

    @classmethod
    def moveLeft(cls):
        print("Moving left")
        if cls.x <= -16:
            print("Cannot move more to the left.")
            return False
        else:
            cls.x -= 16
            return True


class Lemmings:
    pass
