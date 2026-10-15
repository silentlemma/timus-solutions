"""One test from a seed and a mode: mode 1 random small values, mode 2
random values over the whole range, mode 3 a right angle at the elbow
(a^2 + b^2 = r^2), mode 4 a straight arm (r = a + b), mode 5 just outside
one of the two limits."""

import random
import sys

LIMIT = 100
TRIPLES = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]


def line_at(rng, r):
    """Two points of an axis-parallel rail at distance r from the origin."""
    axis = rng.randrange(3)
    other = rng.choice([i for i in range(3) if i != axis])
    p, q = [0, 0, 0], [0, 0, 0]
    p[other] = q[other] = r * rng.choice((-1, 1))
    p[axis], q[axis] = rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)
    while q[axis] == p[axis]:
        q[axis] = rng.randint(-LIMIT, LIMIT)
    return p, q


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (1, 2):
        top = 20 if mode == 1 else LIMIT
        a, b = rng.randint(4, top), rng.randint(4, top)
        while True:
            p = [rng.randint(-top, top) for _ in range(3)]
            q = [rng.randint(-top, top) for _ in range(3)]
            if p != q:
                cross = [p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2],
                         p[0] * q[1] - p[1] * q[0]]
                if any(cross):
                    break
    elif mode == 3:
        x, y, z = rng.choice(TRIPLES)
        k = rng.randint(1, max(1, 30 // z))
        a, b = (k * x, k * y) if rng.random() < 0.5 else (k * y, k * x)
        while min(a, b) < 4:
            a, b, k = a * 2, b * 2, k * 2
        p, q = line_at(rng, k * z)
    elif mode == 4:
        a, b = rng.randint(4, 48), rng.randint(4, 48)
        p, q = line_at(rng, a + b)
    else:
        x, y, z = rng.choice(TRIPLES[1:])
        a, b = x, y
        r = z - 1 if rng.random() < 0.5 else a + b + 1
        p, q = line_at(rng, min(r, LIMIT))
    print(a, b)
    print(*p)
    print(*q)


main()
