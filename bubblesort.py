from etc import swappositions


def bubblesort1(*alist):
    alist = [i for i in alist]
    alist = alist[0]
    previousnumber = 0
    while alist != sorted(alist):

        for count, i in enumerate(alist):
            if not count > len(alist)/2 and count+1 != len(alist) and alist[count] > alist[-count]:
                swappositions(alist, count, -count)

        for count, i in enumerate(alist):
            if count+1 != len(alist) and alist[count] > alist[count+1]:
                swappositions(alist, count, count+1)

    return alist


def bubblesort2(alist):
    alist = [i for i in alist]
    previousnumber = 0
    while alist != sorted(alist):
        for count, i in enumerate(alist):
            if count+1 != len(alist) and alist[count] > alist[count+1]:
                swappositions(alist, count, count+1)

    return alist
