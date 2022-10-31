import time

import pyxel

class Leming():
    w = 16
    h = 16

    x = 0
    y = 0

    def draw(cls, x, y):
        cls.x = x
        cls.y = y
        pyxel.blt(x + cls.x, y + cls.y, 0, 32, 32, cls.w, cls.h)

    def moveRight(self):
        self.x += 1

