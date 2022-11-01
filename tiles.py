from utils import printDocstring
import pyxel
import random

class Tile(object):
    w = 16
    h = 16

    @classmethod
    def draw(cls, x, y, tileType):
        """Drawing a block on the screen."""
        # Generating a random number for block variants
        n = random.randint(0, 1)

        if tileType == "void":
            pyxel.blt(x, y, 0, 240, 224, cls.w, cls.h)

        elif tileType == "ground":
            if n % 2 == 0:
                pyxel.blt(x, y, 0, 32, 16, cls.w, cls.h)
            else:
                pyxel.blt(x, y, 0, 48, 16, cls.w, cls.h)

        elif tileType == "brick":
            if n % 2 == 0:
                pyxel.blt(x, y, 0, 32, 0, cls.w, cls.h)
            else:
                pyxel.blt(x, y, 0, 48, 0, cls.w, cls.h)

        elif tileType == "dirt":
            pyxel.blt(x, y, 0, 0, 0, cls.w, cls.h)

        elif tileType == "wooden_box":
            pyxel.blt(x, y, 0, 16, 16, cls.w, cls.h)

        elif tileType == "bomb":
            pyxel.blt(x, y, 0, 16, 0, cls.w, cls.h)

        elif tileType == "top_door":
            pyxel.blt(x, y, 0, 0, 16, cls.w, cls.h)

        elif tileType == "bottom_door":
            pyxel.blt(x, y, 0, 0, 32, cls.w, cls.h)
