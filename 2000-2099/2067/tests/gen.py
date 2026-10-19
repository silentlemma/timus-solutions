"""Points from a seed and a mode: 1 a few random points, 2 a few points on
one line, 3 the most points on a line with large coordinates, 4 the same
with one point moved off the line by one, 5 the most random points, 6 two
points, 7 the most points on a vertical line."""

import random
import sys

MOST = 200000
BIG = 10 ** 8


def line(rng, n, step_s, step_r):
    """n distinct points a + k (step_s, step_r) inside the bounds."""
    span = max(abs(step_s), abs(step_r), 1)
    k = sorted(rng.sample(range(-(BIG // span), BIG // span + 1), n))
    return [(t * step_s, t * step_r) for t in k]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (1, 5):
        n = rng.randint(3, 8) if mode == 1 else MOST
        points = set()
        while len(points) < n:
            points.add((rng.randint(-BIG, BIG), rng.randint(-BIG, BIG)))
        points = list(points)
    elif mode == 2:
        points = line(rng, rng.randint(2, 8), rng.randint(-5, 5) or 1, rng.randint(-5, 5))
    elif mode in (3, 4):
        points = line(rng, MOST, rng.randint(1, 300), rng.randint(-300, 300))
        if mode == 4:
            i = rng.randrange(MOST)
            points[i] = (points[i][0], points[i][1] + 1)
    elif mode == 6:
        points = line(rng, 2, rng.randint(-BIG, BIG) // 3, rng.randint(-BIG, BIG) // 3)
    else:
        points = line(rng, MOST, 0, 1)
    rng.shuffle(points)
    print(len(points))
    for s, r in points:
        print(s, r)


main()
