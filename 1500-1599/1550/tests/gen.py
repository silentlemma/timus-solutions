"""One test from a seed and a mode: a pyramid and a hole that meets no
edge. Mode 1 takes random sizes up to 10^4, mode 2 a hole touching an edge
almost, mode 3 the largest pyramid, mode 4 small numbers."""

import math
import random
import sys

TOP = 10**4
SMALL = 10
CLOSE = 0.999


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 4 else TOP
    h = TOP - rng.random() if mode == 3 else rng.uniform(0.01, top)
    w = TOP - rng.random() if mode == 3 else rng.uniform(0.01, top)
    while True:
        x, y = rng.uniform(-w / 2, w / 2), rng.uniform(-w / 2, w / 2)
        # room to the diagonals |x| = |y| and to the sides of the base
        room = min(abs(abs(x) - abs(y)) / math.sqrt(2), w / 2 - abs(x), w / 2 - abs(y))
        if room > 0:
            break
    r = room * (CLOSE if mode == 2 else rng.uniform(0.01, CLOSE))
    print("%.4f %.4f" % (h, w))
    print("%.4f %.4f" % (x, y))
    print("%.6f" % r)


main()
