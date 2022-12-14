from generate_map import generateMap
import json
from lemmings import Lemmyngs
import pyxel
import random
from tiles import Tile
import time


class Game(object):
    playing = False
    verbose = True
    game_over = False

    fps = 30
    playing_iteration_int = 0
    total_frames = 0

    color = random.randint(1, 15)
    text_color = random.randint(1, 15)


    score = 0

    bombs_location = [[0, 5], [0, 9], [19, 5], [19, 9], [19, 13]]

    current_lemmyngs = []
    current_lemmyngs_location = []

    added_blocks = []
    block_selected = "wooden_box"

    lemmyngs = Lemmyngs()

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
        pyxel.init(320, 240, title="PyLemings", fps=self.fps,
                   display_scale=1, capture_scale=10)

        if self.verbose:
            print("Activating the mouse.")
        pyxel.mouse(True)

        if self.verbose:
            print("Storing bomb location on './assets/bombs_location.ousontlesbombes'")
        with open('./assets/bombs_location.ousontlesbombes', 'w') as f:
            f.write(json.dumps(self.bombs_location))

        if self.verbose:
            print("Getting the highest score.")
        with open('high_score.nepasmechangersinoncestdelatriche', 'r') as f:
            self.high_score = int(f.read())
            f.close()

        if self.verbose:
            print("Loading the map.")
        pyxel.load("./assets/tileset.pyxres")

        if self.verbose:
            print("Launching the game loop.")
        pyxel.run(self.update, self.draw)

        if self.verbose:
            print("Defining the lemmyngs list.")
        self.lemmyngs = Lemmyngs()

    def loadMap(self):
        if self.mapFile == "":
            mapName = random.randint(0, 100000)
            generateMap(str(mapName))
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

        # Drawing bombs
        for e in self.bombs_location:
            Tile.draw(e[0] * 16, e[1] * 16, 'bomb')

        # Drawing Lemmyngs
        for l in self.current_lemmyngs:  # type: ignore
            # Setting the origin location on the map
            x = 1
            y = 1
            l.origin_location = (x, y)

            # Placing the lemmyng on the map
            x *= l.w
            y *= l.h
            if l.lemmyng_direction == "right":
                pyxel.blt(x + l.x, y + l.y, 0, 32, 32, l.w, l.h, 0)
            elif l.lemmyng_direction == "left":
                pyxel.blt(x + l.x, y + l.y, 0, 32, 48, l.w, l.h, 0)
            elif l.lemmyng_direction == "falling":
                pyxel.blt(x + l.x, y + l.y, 0, 16, 32, l.w, l.h, 0)

            # Updating the current lemmyng's location
            l.current_location = (x + l.x, y + l.y)

        if len(self.added_blocks) > 0:
            for e in self.added_blocks:
                Tile.draw((e[0] // 16) * 16, (e[1] // 16) * 16, e[2])

    def reset(self) -> None:
        self.added_blocks = []

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.playing = True
            self.game_over = False
        if pyxel.btnp(pyxel.KEY_H):
            self.block_selected = "wooden_box"
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            mouse_location = [pyxel.mouse_x, pyxel.mouse_y]
            for e in self.added_blocks:
                if e[0] // 16 == mouse_location[0] // 16 and e[1] // 16 == mouse_location[1] // 16:
                    self.added_blocks.remove(e)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            e = [pyxel.mouse_x, pyxel.mouse_y, self.block_selected]
            with open(f"./maps/{self.mapFile}.kimarch", "r") as f:
                map = json.loads(f.read())
                if map[e[1] // 16][e[0] // 16] == 0 and len(self.added_blocks) < self.config['max_wooden_box']:
                    self.added_blocks.append(e)

        # Saving added blocks in a file ('placed_block.superfileextention')
        with open("./assets/placed_block.superfileextention", "w") as f:
            f.write(json.dumps(self.added_blocks))
            f.close()

        # Touching a bomb -> Game over
        for bomb_location in self.bombs_location:
            for l in self.current_lemmyngs:
                if l.current_location[0] == bomb_location[0] * 16 and l.current_location[1] == bomb_location[1] * 16:
                    print('game over !')
                    self.game_over = True

        # Getting a score
        for l in self.current_lemmyngs:
            current_x, current_y = l.current_location
            if current_x == 0 and current_y == 208:
                self.score += 50
                l.reset()
                self.reset()

        # High score dealing
        if self.high_score < self.score:
            with open('high_score.nepasmechangersinoncestdelatriche', 'w') as f:
                f.write(str(self.score))
                f.close()


    def draw(self):
        # pyxel.cls(col=1)
        if not self.game_over and self.playing == True:
            self.loadMap()

            if self.playing_iteration_int + ((self.config["speed_factor"] * self.fps) // 10) >= self.fps:
                self.current_lemmyngs = self.lemmyngs.new_iteration()

                self.playing_iteration_int = 0
            else:
                self.playing_iteration_int += 1

            pyxel.text(250, 1, f"Score: {self.score} points", 7)
            pyxel.text(280, 11, f"Time: {self.total_frames // self.fps}s", 7)
            if self.block_selected == "wooden_box":
                self.selected_block_name = "Wooden Box"
            elif self.block_selected == "bomb":
                self.selected_block_name = "Bomb"
            pyxel.text(
                250, 21, f"{self.selected_block_name}: {len(self.added_blocks)}", 10)

            Tile.draw((pyxel.mouse_x // 16) * 16,
                      (pyxel.mouse_y // 16) * 16, "selection")

            self.total_frames += 1
        else:
            if not self.playing:
                pyxel.cls(self.color)
                pyxel.text(120, 100, 'Press SPACE To Start', self.text_color)
            else:
                pyxel.cls(1)
                pyxel.text(150, 100, 'Game Over !', 8)

game = Game()
game.initing()
