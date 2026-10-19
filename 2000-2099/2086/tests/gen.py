"""X, Y, Z and the two workplaces from a seed.

Mode 1: small random values. Mode 2: Eugene exactly at distance X from Vanya,
so he may sit at Denis's place. Mode 3: Eugene at distance Y, so he may sit at
the hall. Mode 4: a double root (a single position of Eugene on the segment).
Mode 5: large random values.
"""

import random
import sys

SMALL = 12
TOP = 10 ** 4


def valid(x, y, z):
    return abs(x - y) < z < x + y


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    top = TOP if mode == 5 else SMALL
    while True:
        x, y, z = (rng.randint(1, top) for _ in range(3))
        vx, vy = rng.randint(-top, top), rng.randint(-top, top)
        if mode in (2, 3):
            # an axis-parallel offset has an integer length
            length = x if mode == 2 else y
            ex, ey = (vx + length, vy) if rng.random() < 0.5 else (vx, vy - length)
        else:
            ex, ey = rng.randint(-top, top), rng.randint(-top, top)
        if not valid(x, y, z) or (ex, ey) == (vx, vy):
            continue
        if max(abs(ex), abs(ey)) > TOP:
            continue
        if mode == 4:
            d2 = (ex - vx) ** 2 + (ey - vy) ** 2
            b = y * y - x * x - z * z
            if b * b != 4 * z * z * (x * x - d2):
                continue
        break
    print(x, y, z)
    print(vx, vy)
    print(ex, ey)


main()
