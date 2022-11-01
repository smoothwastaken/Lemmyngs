from random import randint
import json

# scale factor applied after the map creation.
# i have to create the map basics (levels, start door....) but for now i'll just do a random map.

# this file is not finished. it'll be finished when lemmings generation and collision will be functional.

def generateMap(fileName: str):
    try:
        file = open(f"./maps/{fileName}.kimarch", "x")
        # print("Creating the file.")
    except:
        # print("File created !")
        pass
    with open(f"./maps/{fileName}.kimarch", "w") as f:
        theMap = []

        startingDoor = [[0, 0], [1, 0]]

        for i in range(1, 21):
            line = []
            for j in range(1, 21):
                if i == 3 or i == 4 or i == 7 or i == 8 or i == 11 or i == 12 or i == 16:
                    line.append(2)
                elif i == 15:
                    line.append(1)
                else:
                    line.append(0)
            theMap.append(line)


        f.write(str(theMap))
        f.close()


if __name__ == "__main__":
    # mapName = randint(0, 100000)
    # generateMap(mapName)
    generateMap("testing")
