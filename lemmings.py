import time
import json
import pyxel
import glob
import os


class Lemmyng():
    w = 16
    h = 16
    previous_lemmyng_direction = ""
    lemmyng_direction = "right"

    x = 0
    y = 0

    origin_location = (0, 0)

    current_location = (0, 0)

    def __init__(self, id: int) -> None:
        self.id = id

    def draw(self, x: int, y: int) -> None:
        # Setting the origin location on the map
        self.origin_location = (x, y)

        # Placing the lemmyng on the map
        x *= self.w
        y *= self.h
        if self.lemmyng_direction == "right":
            pyxel.blt(x + self.x, y + self.y, 0, 32, 32, self.w, self.h)
        elif self.lemmyng_direction == "left":
            pyxel.blt(x + self.x, y + self.y, 0, 48, 32, self.w, self.h)
        elif self.lemmyng_direction == "falling":
            pyxel.blt(x + self.x, y + self.y, 0, 16, 32, self.w, self.h)

        # Updating the current lemmyng's location
        self.current_location = (x + self.x, y + self.y)

    def get_current_location(self) -> tuple:
        x, y = self.current_location
        x /= self.w
        y /= self.h
        return (int(x), int(y))

    def get_current_map(self) -> list:
        # Get the config file
        config_file = None
        with open("config.json", 'r') as configFile:
            config_file = json.loads(configFile.read())
            configFile.close()

        # Adding the map name to map_file variable
        map_filename = config_file["map"]

        # If no map specified, get the latest created
        if map_filename == "":
            list_of_files = glob.glob('./maps/*.kimarch')
            map_filename = max(list_of_files, key=os.path.getctime)

        # Getting the map
        with open(f"./maps/{map_filename}.kimarch", "r") as f:
            self.map = json.loads(f.read())
            f.close()
        return self.map

    def empty_under(self) -> bool:
        # Getting the map
        map = self.get_current_map()

        # Getting the lemmyng's position
        x_location, y_location = self.get_current_location()
        print("x:", x_location)
        print("y:", y_location)

        # Getting the block under the lemmyng's position
        # Verifying if the block under the lemmyng is empty
        # Returning whether the block under the lemmyng is empty or not
        print(map[x_location - 1][y_location])
        if map[y_location + 1][x_location] == 0:
            return True
        else:
            return False

    def moveRight(self) -> bool:
        # Moving right
        if self.x >= 288:
            # Cannot move more to the right.
            return False
        else:
            self.x += 16
            return True

    def moveLeft(self) -> bool:
        # Moving left
        if self.x <= -16:
            # Cannot move more to the left.
            return False
        else:
            self.x -= 16
            return True

    def fall(self) -> bool:
        self.y += 16
        return True

    def get_id(self) -> int:
        return self.id

    def get_moving_direction(self) -> str:
        return self.lemmyng_direction

    def set_moving_direction(self, new_moving_direction: str) -> bool:
        self.previous_lemmyng_direction = self.lemmyng_direction
        self.lemmyng_direction = new_moving_direction
        return True


class Lemmyngs:
    lemmyngs = []
    generation_int = 1
    generation = 0
    nb_lemmyngs = 1

    def __init__(self) -> None:
        print("Starting Lemmings Generation and spawning")
        with open("config.json", 'r') as configFile:
            self.config = json.loads(configFile.read())
            configFile.close()
        spawn_x, spawn_y = self.config["spawn_location"]
        self.generation_int = int(self.config["generation_speed_factor"])

    def new_iteration(self) -> None:
        # Add the number of lemmyngs on the map.
        if self.generation == self.generation_int or self.generation == 0:
            while len(self.lemmyngs) != self.nb_lemmyngs:
                l = Lemmyng(len(self.lemmyngs))
                self.lemmyngs.append(l)
            self.nb_lemmyngs += 1
            self.generation = 1
        else:
            self.generation += 1

        # Make all of them move
        for l in self.lemmyngs:
            if l.empty_under():
                l.fall()
                l.set_moving_direction("falling")
            elif l.get_moving_direction() in ("right", "falling"):
                l.set_moving_direction("right")
                if l.moveRight():
                    # The lemming is moving to the right.
                    pass
                else:
                    # The lemming was next to the wall, changing direction of his walk.
                    l.moveLeft()
            elif l.get_moving_direction() in ("left", "falling"):
                l.set_moving_direction("left")
                if l.moveLeft():
                    # The lemming is moving to the left.
                    pass
                else:
                    # The lemming was next to the wall, changing direction of his walk.
                    l.moveRight()
            elif l.get_moving_direction() == "falling":
                if l.fall():
                    # The lemming is moving to the left.
                    pass
                else:
                    # The lemming was next to the wall, changing direction of his walk.
                    if l.previous_moving_direction == "right":
                        l.set_moving_direction("right")
                    else:
                        l.set_moving_direction("left")

            l.draw(1, 1)


if __name__ == "__main__":
    lemmyngs = Lemmyngs()
    lemmyngs.new_iteration(3)
