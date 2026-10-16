"""One test file from a seed and a mode: mode 1 a hundred cases with
values up to 60, mode 2 a hundred cases with values up to 10^18, mode 3
a hundred cases with x and y sharing a large factor, mode 4 a hundred
cases with one of x, y equal to 1 or the two equal, and ranges near
the largest values; mode 5 a hundred narrow windows around random sums
of large coprime sizes; mode 6 a hundred scaled small systems with
interval endpoints between multiples of a large common factor."""

import math
import random
import sys

TESTS = 100
SMALL = 60
TOP = 10 ** 18


def case(rng, mode):
    if mode == 1:
        x, y = rng.randint(1, SMALL), rng.randint(1, SMALL)
        lo, hi = sorted(rng.randint(1, SMALL * SMALL // 2) for _ in range(2))
    elif mode == 2:
        x, y = rng.randint(1, TOP), rng.randint(1, TOP)
        if rng.random() < 0.5:
            x = rng.randint(1, 10 ** rng.randint(1, 9))
        lo, hi = sorted(rng.randint(1, TOP) for _ in range(2))
    elif mode == 3:
        g = rng.randint(2, 10 ** rng.randint(1, 12))
        x = g * rng.randint(1, TOP // g)
        y = g * rng.randint(1, TOP // g)
        lo, hi = sorted(rng.randint(1, TOP) for _ in range(2))
    elif mode == 5:
        x, y = rng.randint(10 ** 9, 10 ** 12), rng.randint(10 ** 9, 10 ** 12)
        while math.gcd(x, y) != 1:
            y = rng.randint(10 ** 9, 10 ** 12)
        target = rng.randint(1, 100000) * x + rng.randint(1, 100000) * y
        lo = target + rng.randint(-100, 100)
        hi = lo + rng.randint(0, 128)
    elif mode == 6:
        g = rng.randint(10 ** 10, 10 ** 14)
        x, y = g * rng.randint(2, SMALL), g * rng.randint(2, SMALL)
        a, b = sorted(rng.randint(1, 5000) for _ in range(2))
        lo = a * g + rng.randint(1, g - 1)
        hi = b * g + rng.randint(1, g - 1)
        lo, hi = min(lo, hi), max(lo, hi)
    else:
        x = rng.choice([1, rng.randint(1, TOP)])
        y = rng.choice([1, x, rng.randint(1, TOP)])
        lo, hi = TOP - rng.randint(0, TOP // 2), TOP
    return x, y, lo, hi


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(TESTS)
    for _ in range(TESTS):
        print(*case(rng, mode))


main()
