"""One map from a seed and a mode: mode 1 a few random cities, mode 2
thirty random cities with a random radius, mode 3 thirty cities in
small clusters, mode 4 a chain of cities one radius apart, mode 5 a
5 by 6 lattice whose step is close to the radius, mode 6 thirty random
cities with a radius that needs many bottles."""

import random
import sys

LIMIT = 30
SIDE = 1000
SMALL = 12
ROWS, COLS = 5, 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else LIMIT
    if mode == 3:
        centres = [(rng.randint(100, 900), rng.randint(100, 900)) for _ in range(rng.randint(3, 8))]
        r = rng.randint(30, 150)
        cities = []
        for _ in range(n):
            cx, cy = rng.choice(centres)
            cities.append((max(0, min(SIDE, cx + rng.randint(-r, r))),
                           max(0, min(SIDE, cy + rng.randint(-r, r)))))
    elif mode == 4:
        r = rng.randint(10, 33)
        start = rng.randint(0, SIDE - r * (n - 1))
        cities = [(start + r * i, SIDE // 2) for i in range(n)]
    elif mode == 5:
        step = rng.randint(50, 150)
        r = step + rng.choice((0, 0, step // 2, step))
        cities = [(100 + step * c, 100 + step * row) for row in range(ROWS) for c in range(COLS)]
    else:
        cities = [(rng.randint(0, SIDE), rng.randint(0, SIDE)) for _ in range(n)]
        r = rng.randint(1, SIDE) if mode != 6 else rng.randint(150, 300)
    rng.shuffle(cities)
    print(len(cities), r)
    for x, y in cities:
        print(x, y)


main()
