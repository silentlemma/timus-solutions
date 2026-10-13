"""One test from a seed and a mode, always with a way from 0 to 1. Mode 1
is a random street plan, mode 2 a chain that needs every one of 20
categories, with many roads of category 0 elsewhere, mode 3 a chain of a
random length with random extra roads, mode 4 is small."""

import random
import sys

CATEGORIES = 20
CROSSINGS = 30
SMALL = 6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    k = rng.randint(1, SMALL) if mode == 4 else CATEGORIES
    n = rng.randint(2, SMALL) if mode == 4 else CROSSINGS
    roads = set()

    def add(a, b, c):
        if a != b and (b, a, c) not in roads:
            roads.add((a, b, c))

    if mode == 2:
        chain = [0] + list(range(2, k + 1)) + [1]
        for c, (a, b) in enumerate(zip(chain, chain[1:])):
            add(a, b, c)
        for a in range(k + 1, n):
            add(0, a, 0)
            for b in range(a + 1, n):
                add(a, b, 0)
    else:
        length = rng.randint(1, min(k, n - 1))
        chain = [0] + rng.sample(range(2, n), length - 1) + [1]
        for a, b in zip(chain, chain[1:]):
            add(a, b, rng.randrange(k))
        extra = {1: 3 * n, 3: n, 4: rng.randint(0, n)}[mode]
        for _ in range(extra):
            add(rng.randrange(n), rng.randrange(n), rng.randrange(k))
    roads = list(roads)
    rng.shuffle(roads)
    print(k, n, len(roads))
    for road in roads:
        print(*road)


main()
