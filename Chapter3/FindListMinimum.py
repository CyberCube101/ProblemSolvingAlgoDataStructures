import time
from random import randrange


def FindMin(alist):  # Search using O(n^2)
    overllmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overllmin = i
    return overllmin


myList = [randrange(10000) for x in range(10000)]


start = time.time()
FindMin(myList)
end = time.time()
print(end - start)


def Linear(newList):
    min_os_far = newList[0]
    for i in range(1, len(newList)):
        if newList[i] < min_os_far:
            min_os_far = newList[i]
    return min_os_far


start = time.time()
Linear(myList)
end = time.time()
print(end - start)

