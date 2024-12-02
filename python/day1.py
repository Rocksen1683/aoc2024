import argparse
from typing import List
from collections import Counter

def retrieveList(path: str) -> List[List[int]]:
    """
    Helper function to retrieve the two lists from the input file
    """
    list1 = []
    list2 = []
    with open(path, 'r') as f:
        text = f.read()
        lines = text.split('\n')
        for line in lines:
            elems = line.split('   ')
            list1.append(int(elems[0]))
            list2.append(int(elems[1]))
    
    return [list1, list2]

def distBetweenLists(path: str) -> int:
    """
    Method to calculate distance between list by sorting both of them 
    """
    dist = 0

    l = retrieveList(path)
    list1, list2 = l[0], l[1]

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        dist += abs(list1[i] - list2[i])

    return dist


def listSimilarity(path: str) -> int:
    """
    Method to calculate the similarity of two lists 
    """
    sim = 0

    l = retrieveList(path)
    list1, list2 = l[0], l[1]

    list2Counter = Counter(list2)

    for num in list1:
        if num in list2Counter:
            sim += num * list2Counter[num]

    return sim
    
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prob', dest="probpath", help="Path to the prob1 file", required=True)

    args = parser.parse_args()
    probPath = args.probpath

    print("Distance: ", distBetweenLists(probPath))
    print("Similarity: ", listSimilarity(probPath))


