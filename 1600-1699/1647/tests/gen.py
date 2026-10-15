"""One test from a seed and a mode: a random triangle (mode 1 small
coordinates, mode 2 up to 2000, mode 3 a long thin triangle)."""

import random
import sys

LIMIT = 2000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    span = 10 if mode == 1 else LIMIT
    while True:
        if mode == 3:
            pts = [(-LIMIT, rng.randint(-2, 2)), (LIMIT, rng.randint(-2, 2)),
                   (rng.randint(-LIMIT, LIMIT), rng.randint(-3, 3))]
        else:
            pts = [(rng.randint(-span, span), rng.randint(-span, span)) for _ in range(3)]
        (x1, y1), (x2, y2), (x3, y3) = pts
        if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
            break
    print(*[v for p in pts for v in p])


main()
