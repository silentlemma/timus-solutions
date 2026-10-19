"""Slopes from a seed.

Mode 1: a few short slopes with tiny heights, so matches are common. Mode 2:
long slopes with planted similar sections (various a and b). Mode 3: a long
new slope of length 1, where every section matches. Mode 4: large random
heights, most likely no match. Mode 5: one slope as long as allowed that is
the new slope itself plus a linear term.
"""

import random
import sys

TOTAL = 10 ** 5
TOP = 10 ** 9
TINY = 2
SMALL = 6
PLANTS = 5
SLOPE = 1000


def linear(rng, h, top):
    # add a i + b without leaving [-10^9, 10^9]
    for _ in range(TOTAL):
        a, b = rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL)
        out = [v + a * i + b for i, v in enumerate(h)]
        if max(map(abs, out)) <= top:
            return out
    return h


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        m = rng.randint(1, SMALL // 2)
        x = [rng.randint(-TINY, TINY) for _ in range(m + 1)]
        slopes = [[rng.randint(-TINY, TINY) for _ in range(rng.randint(2, SMALL + 1))]
                  for _ in range(rng.randint(1, SMALL))]
    elif mode in (2, 4):
        top = TOP if mode == 4 else SLOPE
        m = rng.randint(1, SLOPE // 2)
        x = [rng.randint(-top, top) for _ in range(m + 1)]
        slopes = []
        left = TOTAL - SLOPE
        while left > 0:
            length = min(left, rng.randint(1, SLOPE))
            slopes.append([rng.randint(-top, top) for _ in range(length + 1)])
            left -= length
        if mode == 2:
            for _ in range(PLANTS):
                y = rng.choice(slopes)
                if len(y) > m:
                    j = rng.randrange(len(y) - m)
                    y[j:j + m + 1] = linear(rng, x, TOP)
    elif mode == 3:
        m = 1
        x = [rng.randint(-TOP, TOP) for _ in range(2)]
        slopes = [[rng.randint(-TOP, TOP) for _ in range(TOTAL // 2 + 1)] for _ in range(2)]
    else:
        m = TOTAL
        x = [rng.randint(-TOP // 2, TOP // 2) for _ in range(m + 1)]
        slopes = [linear(rng, x, TOP)]
    print(len(slopes))
    print(m, *x)
    for y in slopes:
        print(len(y) - 1, *y)


main()
