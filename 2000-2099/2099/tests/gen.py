"""Four points from a seed.

Mode 1: a valid flight with small coordinates, possibly turning at B or C.
Mode 2: a valid flight with large coordinates. Mode 3: a valid flight with
one point moved by one unit. Mode 4: random points.
"""

import random
import sys

SMALL = 10
TOP = 10 ** 6
STEP = 10


def perpendicular(rng, u, top):
    # an integer vector orthogonal to u: the cross product with a random vector
    while True:
        w = [rng.randint(-top, top) for _ in range(3)]
        v = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
        if any(v):
            return v


def flight(rng, top):
    while True:
        u = [rng.randint(-STEP, STEP) for _ in range(3)]
        if not any(u):
            continue
        v = perpendicular(rng, u, STEP)
        a = [rng.randint(-top // 2, top // 2) for _ in range(3)]
        t = [0, rng.randint(1, STEP), 0, 0]
        t[2] = t[1] + rng.randint(0, STEP)  # the turning point, from A along u
        s1, s2 = rng.randint(0, STEP), rng.randint(1, STEP)
        turn = [a[i] + t[2] * u[i] for i in range(3)]
        points = [a, [a[i] + t[1] * u[i] for i in range(3)],
                  [turn[i] + s1 * v[i] for i in range(3)],
                  [turn[i] + (s1 + s2) * v[i] for i in range(3)]]
        flat = [x for p in points for x in p]
        if max(map(abs, flat)) <= top and len({tuple(p) for p in points}) == len(points):
            return points


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 4:
        points = [[rng.randint(-SMALL, SMALL) for _ in range(3)] for _ in range(4)]
        while len({tuple(p) for p in points}) < len(points):
            points = [[rng.randint(-SMALL, SMALL) for _ in range(3)] for _ in range(4)]
    else:
        points = flight(rng, SMALL * SMALL * SMALL if mode == 1 else TOP)
        if mode == 3:
            i, j = rng.randrange(4), rng.randrange(3)
            moved = [p[:] for p in points]
            moved[i][j] += rng.choice((-1, 1))
            if len({tuple(p) for p in moved}) == len(moved):
                points = moved
    for p in points:
        print(*p)


main()
