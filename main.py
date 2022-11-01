from generate_map import generateMap
import json
from lemmings import Lemming
import pyxel
import random
from tiles import Tile
import time


class Game(object):
    playing = True
    verbose = True

    moving_direction = True

    def initing(self):
        """Creating the game instance."""
        if self.verbose:
            print("Loading config values.")
        with open("config.json", 'r') as configFile:
            self.config = json.loads(configFile.read())
            configFile.close()

        if self.verbose:
            print("Syncing config values.")
        self.verbose = self.config["verbose"]
        self.mapFile = self.config["map"]

        if self.verbose:
            print("Creating the game instance.")
        pyxel.init(320, 240, title="PyLemings", fps=2,
                   display_scale=12, capture_scale=6)

        if self.verbose:
            print("Loading the map.")
        pyxel.load("./assets/tileset.pyxres")

        if self.verbose:
            print("Launching the game loop.")
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
                    # Default block value will be "void"
                    block_type = "void"
                    if c == 0:
                        block_type = "void"
                    elif c == 1:
                        block_type = "ground"
                    elif c == 2:
                        block_type = "brick"
                    elif c == 3:
                        block_type = "dirt"
                    elif c == 4:
                        block_type = "wooden_box"
                    elif c == 5:
                        block_type = "bomb"
                    elif c == 6:
                        block_type = "top_door"
                    elif c == 7:
                        block_type = "bottom_door"

                    Tile.draw(m * 16, n * 16, block_type)
                    m += 1

                n += 1

            f.close()

    def update(self):
        if pyxel.btnp(pyxel.KEY_P):
            pyxel.quit()
        if self.moving_direction:
            if Lemming.moveRight():
                print('The lemming is moving to the right.')
            else:
                print(
                    'The lemming was next to the wall, changing direction of his walk.')
                self.moving_direction = False
                Lemming.moveLeft()
        else:
            if Lemming.moveLeft():
                print('The lemming is moving to the left.')
            else:
                print(
                    'The lemming was next to the wall, changing direction of his walk.')
                self.moving_direction = True
                Lemming.moveRight()

    def draw(self):
        pyxel.cls(0)
        self.loadMap()
        Lemming().draw(1, 8)


game = Game()
game.initing()
