"""One test from a seed and a mode, with nonsquare x up to 10^6.

Mode 1: small x and k.
Mode 2: any x and k up to 10^9.
Mode 3: x just below a square, giving a short period, and a large k.
Mode 4: a period of at least 500 terms, with k strictly inside its first copy.
Mode 5: x just above a large square, a period of one, and a large random k.
"""

import random
import sys
from math import isqrt

LIMIT_X = 10 ** 6
LIMIT_K = 10 ** 9
SMALL = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            x, k = rng.randint(2, SMALL), rng.randint(0, SMALL)
        elif mode == 2:
            x, k = rng.randint(2, LIMIT_X), rng.randint(0, LIMIT_K)
        elif mode == 4:
            x = rng.randint(2, LIMIT_X)
            a0 = isqrt(x)
            if a0 * a0 == x:
                continue
            m, d, a, length = 0, 1, a0, 0
            while a != 2 * a0:
                m = d * a - m
                d = (x - m * m) // d
                a = (a0 + m) // d
                length += 1
            if length < 500:
                continue
            k = rng.randint(1, length - 1)
        elif mode == 5:
            r = rng.randint(500, isqrt(LIMIT_X) - 1)
            x, k = r * r + 1, rng.randint(LIMIT_K // 2, LIMIT_K)
        else:
            r = rng.randint(2, isqrt(LIMIT_X))
            x, k = r * r - rng.randint(1, 2), rng.randint(0, LIMIT_K)
        if isqrt(x) ** 2 != x and x >= 2:
            break
    print(x, k)


main()
