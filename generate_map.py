from random import randint
import json

# scale factor applied after the map creation.
# i have to create the map basics (levels, start door....) but for now i'll just do a random map.

# this file is not finished. it'll be finished when lemmings generation and collision will be functional.


def generateMap(fileName: str):
    try:
        file = open(f"./maps/{fileName}.kimarch", "x")
        print("[+] Creating the map file")
    except:
        print("[*] Map already created")
        pass
    with open(f"./maps/{fileName}.kimarch", "w") as f:
        # Creating an empty map
        theMap = []
        for i in range(1, 21):
            line = []
            for j in range(1, 21):
                line.append(0)
            theMap.append(line)

        # Placing the starting door
        theMap[0][0] = 6
        theMap[1][0] = 7

        # Placing the floors
        for i in range(20):
            print(i)
            # Dirt first floor
            theMap[2][i] = 3
            # Brick first celling
            theMap[3][i] = 2

            # Brick first floor
            theMap[6][i] = 2
            # Brick second celling
            theMap[7][i] = 2

            # Brick second floor
            theMap[10][i] = 2
            # Brick third celling
            theMap[11][i] = 2

            # Ground first floor
            theMap[14][i] = 1

        # Hole first level
        random_hole = randint(2, 19)
        theMap[2][random_hole] = 0
        theMap[3][random_hole] = 0

        # Hole first level
        random_hole = randint(0, 17)
        theMap[6][random_hole] = 0
        theMap[7][random_hole] = 0

        # Hole first level
        random_hole = randint(0, 19)
        theMap[10][random_hole] = 0
        theMap[11][random_hole] = 0

        # Writing and closing the map file
        f.write(str(theMap))
        f.close()


if __name__ == "__main__":
    # mapName = randint(0, 100000)
    # generateMap(mapName)
    generateMap("testing")
