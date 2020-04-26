# pass in 2 numbers and show as a fraction

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):  # We have to overide 1==f2 will only be True if they are references to the same object.
        # Two different objects with the same numerators and denominators would not be equal under this implementation
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)
print(f1 == f2)

## This works but doesnt provide answer in l.c.d. Here we can use Euclids Algorithm

# Euclid’s Algorithm states that the greatest common divisor of two integers m and n is n if n divides m evenly.
# However, if n does not divide m evenly, then the answer is the greatest common divisor of n and the remainder of m divided by n.
