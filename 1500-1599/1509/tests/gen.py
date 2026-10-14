"""One test from a seed and a mode: the dots of a random domino of size L,
turned by a random angle, maybe mirrored, moved, rounded to four decimals
and shuffled. Mode 1 takes random squares and L, mode 2 takes L near 1,
mode 3 takes L near 100, mode 4 takes two dots that fit only one reading
(a 1-1 domino with L above 100 / sqrt 2, or a 0-2 domino with L below
sqrt 2), mode 5 takes the six-dot squares."""

import cmath
import math
import random
import sys

QUARTER = 0.25
MOST = 6
REACH = 1500  # the centre stays well inside the 2000 coordinate limit
DIGITS = 4


def square(k, centre):
    q = QUARTER
    corners = [complex(-q, -q), complex(q, q), complex(q, -q), complex(-q, q)]
    middles = [complex(0, -q), complex(0, q)]
    rings = {
        0: [],
        1: [],
        2: corners[:2],
        3: corners[:2],
        4: corners,
        5: corners,
        6: corners + middles,
    }
    dots = list(rings[k]) + ([0] if k % 2 else [])
    return [centre + d for d in dots]


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    a, b = sorted((rng.randint(0, MOST), rng.randint(0, MOST)))
    size = rng.uniform(1, 100)
    if mode == 2:
        size = rng.uniform(1, 1.5)
    elif mode == 3:
        size = rng.uniform(95, 100)
    elif mode == 4:
        if rng.random() < 0.5:
            a, b, size = 1, 1, rng.uniform(72, 100)
        else:
            a, b, size = 0, 2, rng.uniform(1, 1.4)
    elif mode == 5:
        a, b = rng.randint(0, MOST), MOST
    if a + b == 0:
        b = 1
    dots = square(a, 0) + square(b, 1)
    if rng.random() < 0.5:
        dots = [d.conjugate() for d in dots]
    turn = size * cmath.exp(1j * rng.uniform(0, 2 * math.pi))
    shift = complex(rng.uniform(-REACH, REACH), rng.uniform(-REACH, REACH))
    dots = [shift + d * turn for d in dots]
    rng.shuffle(dots)
    print(len(dots))
    for d in dots:
        print("%.*f %.*f" % (DIGITS, d.real, DIGITS, d.imag))


main()
