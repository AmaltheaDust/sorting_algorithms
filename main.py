from bubblesort import bubblesort1
from etc import createlist, timing
import time

#bubblesort
#shufflesort
#WIP Bucketsort
#WIP quicksort
#WIP mergesort

mylist = createlist(1000, 1000)

#bubblesort with a for loop that checks from outside indexes to center after each bubble loop.
print(timing(bubblesort1, mylist))

