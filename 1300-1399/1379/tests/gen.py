"""Roads between 500 junctions: a seed and a mode. Mode 1 gives a complete
graph of short roads, mode 2 a chain of short roads inside a complete
graph of day-long ones, so every search scans all roads, mode 3 a
sparse random graph."""

import random
import sys

COUNT = 500
TRUCK = 3_000_000
TOP = 10**9
DAY = 1440


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = COUNT
    roads = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if mode == 1:
                roads.append((a, b, rng.randint(0, 20), rng.randint(TRUCK, TOP)))
            elif mode == 2:
                t = 2 if b == a + 1 else DAY
                roads.append((a, b, t, rng.randint(TRUCK, TOP)))
            elif rng.random() < 0.01:
                roads.append((a, b, rng.randint(0, 300), rng.randint(0, TOP)))
    rng.shuffle(roads)
    print(n, len(roads))
    for r in roads:
        print(*r)


main()
