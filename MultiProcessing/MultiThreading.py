import time
import threading

arr = [2, 4, 6, 8]


def calc_square(numbers):
    print("Calculating Square Numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n * n)


def calc_cube(numbers):
    print("Calculating Cube Numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n * n * n)


# t = time.time()
# calc_square(arr)
# calc_cube(arr)
# print("done in : ", time.time() - t)
# print('###############################')

# This takes 1.6 seconds. Now we will see this using multi-threading

start = time.time()
t1 = threading.Thread(target=calc_square, args=(arr, ))
t2 = threading.Thread(target=calc_cube, args=(arr, ))
t1.start()
t2.start()
t1.join()
t2.join()
print("threading done in : ", time.time() - start)