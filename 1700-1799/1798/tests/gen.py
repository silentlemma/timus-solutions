"""One test from a seed and a mode:
1: a radius up to 3000;
2: a radius up to 10^9;
3: a radius close to 10^9;
4: a multiple of a Pythagorean hypotenuse;
5: a large Pell radius, with a diagonal corner one squared unit from the circle;
6: a large power of two, whose squared radius loses minus one in binary64;
7: a multiple of six distinct primes congruent to one modulo four, giving
   hundreds of corner-only contacts to exclude.
"""

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
    elif mode == 5:
        radii = []
        for radius, diagonal in ((1, 1), (3, 2)):
            while radius <= TOP:
                if radius >= 10 ** 7:
                    radii.append(radius)
                radius, diagonal = 3 * radius + 4 * diagonal, 2 * radius + 3 * diagonal
        radius = rng.choice(radii)
    elif mode == 6:
        radius = 1 << rng.randint(27, 29)
    elif mode == 7:
        base = 5 * 13 * 17 * 29 * 37 * 41
        radius = base * rng.randint(1, TOP // base)
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
