import random
import time

def createlist(numberofitems, sizeofitems):
    randomlist = []
    for i in range(0,numberofitems):
        n = random.randint(1,sizeofitems)
        randomlist.append(n)
    return randomlist


def swappositions(alist, pos1, pos2):
    alist[pos1], alist[pos2] = alist[pos2], alist[pos1]
    return alist


def timing(function, *args):
    start = time.clock()
    print(function(*args))
    end = time.clock()
    totaltime = end - start
    return round(totaltime, 6)
