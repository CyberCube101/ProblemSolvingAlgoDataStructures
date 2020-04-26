# Newton’s Method for approximating square roots
# newguess=0.5∗(oldguess+n/oldguess)

import math as m


def square_root(n):
    return m.sqrt(n)


# now lets try our approximation using Newtons method

def newton_root(n, iteration):
    root = n / 2  # initial guess
    for i in range(iteration):
        root = 0.5 * (root + (n / root))
    return root


if __name__ == '__main__':
    print(square_root(2))
    print(newton_root(2, 10000))
