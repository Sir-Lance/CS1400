import random
from array import *

def fisherYatesShuffle(dataArray):
    n = len(dataArray)
    while (n > 1):
        n = n - 1
        k = random.randint(0, n+1)
        tmp = dataArray[k]
        dataArray[k] = dataArray[n]
        dataArray[n] = tmp

tempArray = array('d', [1, 2, 3, 4, 5])
