from random import randint

def splitdeck(alist):
    variance = len(alist) // 3
    i = (len(alist) // 2) + (variance // 2) - randint(0, variance)
    return alist[:i], alist[i:]


def shufflesort(alist):

    cyclecount = 0

    while alist != sorted(alist):
        cyclecount += 1
        half1, half2 = splitdeck(alist)
        everyothercounter = 0
        for i in half2:
            half1.insert(min(everyothercounter, len(half1)), i)
            everyothercounter += 1 + (1 if randint(0, 6) else (0 if randint(0, 1) else 2))
        alist = half1
    print(cyclecount)
    return alist
