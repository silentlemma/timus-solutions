import sys
from math import isqrt

QUARTERS = 4


def main():
    r = int(sys.stdin.read())
    # a tile shares more than one point with the disc exactly when its
    # corner nearest to the centre lies strictly inside: in one quarter,
    # tiles (i, j) with i^2 + j^2 < r^2, that is j <= isqrt(r^2 - i^2 - 1)
    total = sum(isqrt(r * r - i * i - 1) + 1 for i in range(r))
    print(QUARTERS * total)


main()
