"""One deterministic test from a seed and a mode, with no three on a line.

Mode 1: coordinates up to 5.
Mode 2: coordinates up to 10000.
Mode 3: two nearly parallel pairs far away.
Mode 4: a tight random cluster near the positive coordinate limit.
Mode 5: a random triangle and its integer centroid strictly inside.
Mode 6: four distinct points on the integer parabola y = x*x.
"""

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
        elif mode == 4:
            p = [(rng.randint(LIMIT - 10, LIMIT), rng.randint(LIMIT - 10, LIMIT))
                 for _ in range(BOSSES)]
        elif mode == 5:
            p = [(rng.randint(-100, 100), rng.randint(-100, 100)) for _ in range(3)]
            sx, sy = sum(x for x, y in p), sum(y for x, y in p)
            if sx % 3 or sy % 3:
                continue
            p.append((sx // 3, sy // 3))
        elif mode == 6:
            p = [(x, x * x) for x in rng.sample(range(-100, 101), BOSSES)]
        else:
            p = [(rng.randint(-top, top), rng.randint(-top, top)) for _ in range(BOSSES)]
        triples = [(i, j, k) for i in range(BOSSES) for j in range(i) for k in range(j)]
        if all(not collinear(p[i], p[j], p[k]) for i, j, k in triples):
            break
    for x, y in p:
        print(x, y)


main()
