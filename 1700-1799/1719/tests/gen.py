"""One test from a seed and a mode: four bosses with no three on a line,
mode 1 coordinates up to 5, mode 2 up to 10000, mode 3 two nearly
parallel pairs far away."""

import random
import sys

LIMIT = 10000
SMALL = 5
BOSSES = 4


def collinear(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) == (q[1] - p[1]) * (r[0] - p[0])


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else LIMIT
    while True:
        if mode == 3:
            x, y = rng.randint(-LIMIT, -LIMIT // 2), rng.randint(-LIMIT, LIMIT)
            p = [(x, y), (x + rng.randint(1, 100), y + 1),
                 (-x, y + rng.randint(1, 50)), (-x + rng.randint(1, 100), y + rng.randint(1, 52))]
        else:
            p = [(rng.randint(-top, top), rng.randint(-top, top)) for _ in range(BOSSES)]
        triples = [(i, j, k) for i in range(BOSSES) for j in range(i) for k in range(j)]
        if all(not collinear(p[i], p[j], p[k]) for i, j, k in triples):
            break
    for x, y in p:
        print(x, y)


main()
