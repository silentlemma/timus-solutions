import sys
from math import isqrt

SQUARE = 8


def main():
    data = sys.stdin.buffer.read().split()
    out = []
    for k in map(int, data[1 : 1 + int(data[0])]):
        # the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
        # perfect square
        v = SQUARE * (k - 1) + 1
        out.append("1" if isqrt(v) ** 2 == v else "0")
    print(" ".join(out))


main()
