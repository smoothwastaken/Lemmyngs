from utils import printDocstring
import pyxel

class Tile(object):
    w = 16
    h = 16

    @classmethod
    def draw(cls, x, y, tileType):
        """Drawing a block on the screen."""
        if tileType == "void":
            pyxel.blt(x, y, 0, 0, 0, cls.w, cls.h)

        elif tileType == "ground":
            pyxel.blt(x, y, 0, 48, 16, cls.w, cls.h)

        elif tileType == "brick":
            pyxel.blt(x, y, 0, 48, 0, cls.w, cls.h)

        elif tileType == "upDoor":
            pass

        elif tileType == "downDoor":
            pass
