import argparse
from typing import List

def readLevels(path: str) -> List[List[int]]:
    """
    Helper function to read levels from the input file
    """
    levels = []
    with open(path, 'r') as f:
        text = f.read()
        lines = text.split('\n')
        for line in lines:
            elems = line.split(' ')
            level = [int(elems[i]) for i in range(len(elems))]
            levels.append(level)

        return levels
    
def countSafeLevels(path: str) -> int:
    """Method to calculate the number of safe levels"""
    safeLevels = 0 


    levels = readLevels(path)

    for level in levels: 
        increaseCount = 0 
        decreaseCount = 0

        for i in range(1, len(level)):
            if (level[i] - level[i-1] > 0 and level[i] - level[i-1] <= 3):
                increaseCount += 1
            elif (level[i-1] - level[i] > 0 and level[i-1] - level[i] <= 3):
                decreaseCount += 1

        if increaseCount == len(level) - 1 or decreaseCount == len(level) - 1:
            safeLevels += 1

    return safeLevels

def countProbDampedLevels(path: str) -> int:
    """Method to calculate the number of safe levels"""
    safeLevels = 0 


    levels = readLevels(path)

    for level in levels: 
        increaseCount = 0 
        decreaseCount = 0

        for i in range(1, len(level)):
            if (level[i] - level[i-1] > 0 and level[i] - level[i-1] <= 3):
                increaseCount += 1
            elif (level[i-1] - level[i] > 0 and level[i-1] - level[i] <= 3):
                decreaseCount += 1

        if (increaseCount == len(level) - 1 or decreaseCount == len(level) - 1) or (decreaseCount == 1) or (increaseCount == 1):
            safeLevels += 1

    return safeLevels





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prob', dest="probpath", help="Path to the prob1 file", required=True)

    args = parser.parse_args()
    probPath = args.probpath
    print(len(readLevels(probPath)))
    print(countSafeLevels(probPath))
    print(countProbDampedLevels(probPath))
