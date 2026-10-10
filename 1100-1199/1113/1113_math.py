import sys
from fractions import Fraction


def main():
    n, m = map(int, sys.stdin.read().split())
    # from the target backwards: the last m km take one load; before it, a
    # stretch of m / (2k - 1) km is crossed 2k - 1 times to bring k loads
    stretch = Fraction(0)
    k = 1
    while stretch + Fraction(m, 2 * k - 1) < n:
        stretch += Fraction(m, 2 * k - 1)
        k += 1
    fuel = (k - 1) * m + (n - stretch) * (2 * k - 1)
    print(-(-fuel.numerator // fuel.denominator))


main()
