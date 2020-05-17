import time


def sumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1, n + 1):
        theSum += i

    end = time.time()
    return theSum, end - start


# now is a more efficient way

def sumOfN2(n):
    start = time.time()
    theSum = (n * (n + 1)) / 2
    end = time.time()
    return theSum, end - start


print(sumOfN(10000000))
print(sumOfN2(10000000))
