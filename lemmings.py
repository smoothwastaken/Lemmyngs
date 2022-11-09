import time
import json
import pyxel


class Lemmyng():
    w = 16
    h = 16
    lemmyng_direction = "right"
    x = 0
    y = 0

    def __init__(self, id: int) -> None:
        self.id = id

    def draw(self, x: int, y: int) -> None:
        x *= self.w
        y *= self.h
        if self.lemmyng_direction == "right":
            pyxel.blt(x + self.x, y + self.y, 0, 32, 32, self.w, self.h)
        else:
            pyxel.blt(x + self.x, y + self.y, 0, 48, 32, self.w, self.h)

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

    def get_id(self) -> int:
        return self.id

    def get_moving_direction(self) -> str:
        return self.lemmyng_direction

    def set_moving_direction(self, new_moving_direction: str) -> bool:
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
            if l.get_moving_direction() == "right":
                if l.moveRight():
                    # The lemming is moving to the right.
                    pass
                else:
                    # The lemming was next to the wall, changing direction of his walk.
                    l.set_moving_direction("left")
                    l.moveLeft()
            else:
                if l.moveLeft():
                    # The lemming is moving to the left.
                    pass
                else:
                    # The lemming was next to the wall, changing direction of his walk.
                    l.set_moving_direction("right")
                    l.moveRight()

            l.draw(1, 1)


if __name__ == "__main__":
    lemmyngs = Lemmyngs()
    lemmyngs.new_iteration(3)
