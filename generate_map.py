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
        startingDoor = [[0, 0], [1, 0]]

        # Writing and closing the map file
        f.write(str(theMap))
        f.close()


if __name__ == "__main__":
    # mapName = randint(0, 100000)
    # generateMap(mapName)
    generateMap("testing")
