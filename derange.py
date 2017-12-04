#Theory behind the algorithm: https://youtu.be/pbXg5EI5t4c

import random

def derange(oldList):
    """
    input: a list
    output: another list
    concept: Function to derange elements of a list if list has more than one elements.
            Returns an unaltered list if list has zero or one element.
    """
    if len(oldList)<2:
        return oldList
    newList = oldList[:]
    while True:
        random.shuffle(newList)
        for a, b in zip(oldList, newList):
            if a == b:
                break
        else:
            return newList