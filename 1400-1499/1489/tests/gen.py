"""One test from a seed and a mode: two points on random faces of the
net, mode 1 with random sizes, mode 2 exactly on edges and corners of the
faces, mode 3 with the largest sizes, mode 4 with tiny ones."""

import random
import sys

LARGEST = 1000
TINY = 3


def point(rng, a, b, c, on_edge):
    def pick(lo, hi):
        if on_edge:
            return rng.choice([lo, hi])
        return rng.randint(lo * 100, hi * 100) / 100

    face = rng.randrange(6)
    column = (c, c + a)
    if face < 4:
        bands = [(0, b), (b, b + c), (b + c, 2 * b + c), (2 * b + c, 2 * b + 2 * c)]
        return pick(*column), pick(*bands[face])
    flap = (0, c) if face == 4 else (c + a, 2 * c + a)
    return pick(*flap), pick(b + c, 2 * b + c)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = {1: LARGEST, 2: LARGEST, 3: LARGEST, 4: TINY}[mode]
    low = LARGEST if mode == 3 else 1
    a, b, c = (rng.randint(low, top) for _ in range(3))
    p = q = None
    while p == q:
        p = point(rng, a, b, c, mode == 2)
        q = point(rng, a, b, c, mode == 2)
    print(a, b, c)
    print("%.2f %.2f" % p)
    print("%.2f %.2f" % q)


main()
