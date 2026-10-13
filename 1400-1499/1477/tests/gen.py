"""One test from a seed and a mode, always with different directions.
Mode 1 is up to 150 random directions with coordinates up to 600, mode 2
up to 150 directions with coordinates up to 3 (many on common planes),
mode 3 puts most directions on one great circle, mode 4 is a small random
test, mode 5 splits the directions between two narrow opposite cones."""

import random
import sys
from math import gcd

LARGEST = 150
REACH = 600
NEAR = 3
SMALL = 8
CONE = 40  # in mode 5 the directions are (x, y, ±600) with |x|, |y| up to this


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    count = rng.randint(1, SMALL) if mode == 4 else LARGEST
    reach = NEAR if mode in (2, 4) else REACH
    seen = set()
    points = []

    def add(p):
        g = gcd(gcd(p[0], p[1]), p[2])
        if g == 0 or tuple(x // g for x in p) in seen:
            return
        seen.add(tuple(x // g for x in p))
        points.append(p)

    attempts = 0
    while len(points) < count and attempts < 100 * LARGEST:
        attempts += 1
        if mode == 3 and rng.random() < 0.9:
            add((rng.randint(-reach, reach), rng.randint(-reach, reach), 0))
        elif mode == 5:
            pole = REACH if len(points) % 2 == 0 else -REACH
            add((rng.randint(-CONE, CONE), rng.randint(-CONE, CONE), pole))
        else:
            add(tuple(rng.randint(-reach, reach) for _ in range(3)))
    lines = [str(len(points))] + ["%d %d %d" % p for p in points]
    print("\n".join(lines))


main()
