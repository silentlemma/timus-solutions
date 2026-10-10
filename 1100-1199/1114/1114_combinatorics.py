import sys
from math import comb


def main():
    n, a, b = map(int, sys.stdin.read().split())
    # up to a identical balls in n boxes: put the unused ones in an extra box,
    # then it is a stars-and-bars count C(a + n, n); the colours are independent
    print(comb(a + n, n) * comb(b + n, n))


main()
