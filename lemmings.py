import time
import json
import pyxel


class Lemmyng():
    w = 16
    h = 16

    x = 0
    y = 0

    def __init__(self, id) -> None:
        self.id = id

    def draw(self, x, y) -> None:
        x *= self.w
        y *= self.h
        pyxel.blt(x + self.x, y + self.y, 0, 32, 32, self.w, self.h)

    def moveRight(self) -> bool:
        print("Moving right")
        if self.x >= 288:
            print("Cannot move more to the right.")
            return False
        else:
            self.x += 16
            return True

    def moveLeft(self) -> bool:
        print("Moving left")
        if self.x <= -16:
            print("Cannot move more to the left.")
            return False
        else:
            self.x -= 16
            return True


class Lemmyngs:
    lemmyngs = []

    moving_direction = True

    generation_int = 1
    generation = 0

    def __init__(self) -> None:
        print("Starting Lemmings Generation and spawning")
        with open("config.json", 'r') as configFile:
            self.config = json.loads(configFile.read())
            configFile.close()
        spawn_x, spawn_y = self.config["spawn_location"]

    def new_iteration(self, nb_lemmyngs) -> None:
        # Add the number of lemmyngs on the map.
        if self.generation % 2 == 0:
            while len(self.lemmyngs) != nb_lemmyngs:
                l = Lemmyng(len(self.lemmyngs))
                self.lemmyngs.append(l)
            self.generation += 1
        else:
            self.generation = 0

        # Make all of them move
        for l in self.lemmyngs:
            if self.moving_direction:
                if l.moveRight():
                    print('The lemming is moving to the right.')
                else:
                    print(
                        'The lemming was next to the wall, changing direction of his walk.')
                    self.moving_direction = False
                    l.moveLeft()
            else:
                if l.moveLeft():
                    print('The lemming is moving to the left.')
                else:
                    print(
                        'The lemming was next to the wall, changing direction of his walk.')
                    self.moving_direction = True
                    l.moveRight()

            l.draw(1, 1)


if __name__ == "__main__":
    lemmyngs = Lemmyngs()
    lemmyngs.new_iteration(3)
