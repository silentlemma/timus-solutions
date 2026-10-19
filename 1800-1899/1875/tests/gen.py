"""Five monkeys from a seed and a mode: mode 1 small random points,
2 large random points, 3 points on parabolas y = x (b - c x), as many as
the mode allows on one of them, 4 several points sharing an x, 5 a
parabola through three points and another through the other two,
6 random points with both coordinates in 9989..10000. No two monkeys
are ever on one line with the slingshot."""

import random
import sys
from math import gcd

MONKEYS = 5
LARGEST = 10000
SMALL = 12


def on_parabola(rng, count, xs_taken):
    # integer points of y = x (b - c x) with 0 < y <= LARGEST
    while True:
        c = rng.randint(1, SMALL)
        b = rng.randint(c + 1, c * SMALL * SMALL)
        xs = [x for x in range(1, b // c + 1) if 0 < x * (b - c * x) <= LARGEST and x not in xs_taken]
        if len(xs) >= count:
            return [(x, x * (b - c * x)) for x in rng.sample(xs, count)]


def valid(points):
    slopes = {(y // gcd(x, y), x // gcd(x, y)) for x, y in points}
    return len(slopes) == len(points) and len(set(points)) == len(points)


def make(rng, mode):
    if mode == 1:
        return [(rng.randint(1, SMALL), rng.randint(1, SMALL)) for _ in range(MONKEYS)]
    if mode == 2:
        return [(rng.randint(1, LARGEST), rng.randint(1, LARGEST)) for _ in range(MONKEYS)]
    if mode == 3:
        count = rng.randint(2, MONKEYS)
        pts = on_parabola(rng, count, set())
        return pts + [(rng.randint(1, LARGEST), rng.randint(1, LARGEST))
                      for _ in range(MONKEYS - count)]
    if mode == 4:
        x = rng.randint(1, SMALL)
        pts = [(x, rng.randint(1, LARGEST)) for _ in range(MONKEYS - 2)]
        return pts + [(rng.randint(1, SMALL), rng.randint(1, LARGEST)) for _ in range(2)]
    if mode == 6:
        return [(rng.randint(LARGEST - SMALL + 1, LARGEST),
                 rng.randint(LARGEST - SMALL + 1, LARGEST)) for _ in range(MONKEYS)]
    first = on_parabola(rng, MONKEYS - 2, set())
    return first + on_parabola(rng, 2, {x for x, _ in first})


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        pts = make(rng, mode)
        if valid(pts):
            break
    rng.shuffle(pts)
    print("\n".join("%d %d" % p for p in pts))


main()
