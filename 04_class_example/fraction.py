class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print self.num, "/", self.den

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __div__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __le__(self, otherfraction):
        return self.num * otherfraction.den < self.den * otherfraction.num

    def __gt__(self, otherfraction):
        return self.num * otherfraction.den > self.den * otherfraction.num


def gcd(m, n):
    while m % n != 0:
        #oldm = m
        #oldn = n

        #m = oldn
        #n = oldm % oldn
        m, n = n, m%n

    return n

if __name__ == "__main__":
    x = Fraction(1,2)
    y = Fraction(2,3)
    print x + y
    print x == y
    print x * y
    print x / y
    print x - y
    print x < y
    print x > y
