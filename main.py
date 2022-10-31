import random

from utils import printDocstring
from generate_map import generateMap

import time
import json
import pyxel
from tiles import Tile
from lemmings import Leming
import sys
# import pytmx
# import pyscroll

class Game(object):
    playing = True
    verbose = True

    def initing(self):
        """Creating the game instance."""
        if self.verbose: print("Loading config values.")
        with open("config.json", 'r') as configFile:
            self.config = json.loads(configFile.read())
            configFile.close()

        if self.verbose: print("Syncing config values.")
        self.verbose = self.config["verbose"]
        self.mapFile = self.config["map"]

        if self.verbose: print("Creating the game instance.")
        pyxel.init(320, 240, "PyLemings")

        if self.verbose: print("Loading the map.")
        pyxel.load("./assets/tileset.pyxres")

        if self.verbose: print("Launching the game loop.")
        pyxel.run(self.update, self.draw)

    def loadMap(self):
        if self.mapFile == "":
            mapName = random.randint(0, 100000)
            generateMap(mapName)
            self.mapFile = mapName

        with open(f"./maps/{self.mapFile}.kimarch", "r") as f:
            map = json.loads(f.read())
            n = 0
            for l in map:
                m = 0
                for c in l:
                    if c == 0:
                        Tile.draw(n * 16, m * 16, "ground")

                    if c == 1:
                        Tile.draw(n * 16, m * 16, "brick")

                    if c == 2:
                        pass

                    m += 1

                n += 1

            f.close()


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        # pyxel.cls(0)
        Leming().draw(16, 208)
        self.loadMap()

        Leming().moveRight()

        
game = Game()
game.initing()