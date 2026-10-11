import sys
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, stones = data[0], data[1 : 1 + data[0]]
    order = sorted(range(n), key=stones.__getitem__)
    # a swap moves a stone K + 1 places, so K + 1 must divide every stone's
    # distance to its place, in one order or the other; all weights differ
    best = 0
    for target in (range(n), range(n - 1, -1, -1)):
        g = 0
        for place, at in zip(target, order):
            g = gcd(g, abs(place - at))
        best = max(best, g - 1 if g else n - 1)
    print(best)


main()
