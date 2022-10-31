from random import randint
import json

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

        f.write(str(theMap))
        f.close()
