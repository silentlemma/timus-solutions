"""One test from a seed and a mode: mode 1 a radius up to 3000, mode 2
up to 10^9, mode 3 close to 10^9, mode 4 the hypotenuse of a
Pythagorean triple, so the circle passes through slab corners."""

import random
import sys

SMALL = 3000
TOP = 10 ** 9
NEAR = 1000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        radius = rng.randint(1, SMALL)
    elif mode == 2:
        radius = rng.randint(1, TOP)
    elif mode == 3:
        radius = TOP - rng.randint(0, NEAR)
    else:
        while True:
            p = rng.randint(2, 30000)
            q = rng.randint(1, p - 1)
            k = rng.randint(1, TOP // (p * p + q * q) or 1)
            radius = k * (p * p + q * q)
            if radius <= TOP:
                break
    print(radius)


main()
