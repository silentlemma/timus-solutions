"""One test from a seed and a mode: n distinct cities with coordinates from
0 to 10000. Mode 1 is 300 random cities, mode 2 a dense grid with many
cities per road, mode 3 cities on a few lines through one point, mode 4
300 cities on one line, mode 5 a few cities in a small square."""

import random
import sys

MOST = 300
SIDE = 10000
GRID = 17  # 17 * 17 = 289 cities
SPOKES = 6
SMALL = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    cities = set()
    if mode == 1:
        while len(cities) < MOST:
            cities.add((rng.randint(0, SIDE), rng.randint(0, SIDE)))
    elif mode == 2:
        step = rng.randint(1, SIDE // (GRID - 1))
        cities = {(i * step, j * step) for i in range(GRID) for j in range(GRID)}
    elif mode == 3:
        cx, cy = SIDE // 2, SIDE // 2
        dirs = [(rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL)) for _ in range(SPOKES)]
        for dx, dy in dirs:
            for k in range(-MOST, MOST):
                x, y = cx + k * dx, cy + k * dy
                if 0 <= x <= SIDE and 0 <= y <= SIDE and len(cities) < MOST:
                    cities.add((x, y))
    elif mode == 4:
        dx, dy = rng.randint(0, SMALL), rng.randint(1, SMALL)
        cities = {(k * dx, k * dy) for k in range(MOST) if k * dy <= SIDE}
    else:
        n = rng.randint(1, SMALL)
        while len(cities) < n:
            cities.add((rng.randint(0, SMALL), rng.randint(0, SMALL)))
    cities = list(cities)
    rng.shuffle(cities)
    print(len(cities))
    for x, y in cities:
        print(x, y)


main()
