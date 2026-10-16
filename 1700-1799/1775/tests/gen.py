"""One test from a seed and a mode: mode 1 up to 8 pins on a small grid,
mode 2 200 pins anywhere, mode 3 200 pins with k pins nearly on one
line, mode 4 200 pins on a small grid, so that many lie on lines."""

import random
import sys

FEW = 8
SMALL = 6
MOST = 200
FAR = 100000
NEAR = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 1 else MOST
    k = rng.randint(1, n)
    top = SMALL if mode == 1 else (2 * SMALL if mode == 4 else FAR)
    pins = set()
    if mode == 3:
        ax, ay = rng.randint(-FAR // 2, FAR // 2), rng.randint(-FAR // 2, FAR // 2)
        bx, by = rng.randint(-FAR // 2, FAR // 2), rng.randint(-FAR // 2, FAR // 2)
        while len(pins) < k:
            t = rng.random()
            pins.add((int(ax + t * (bx - ax)) + rng.randint(-NEAR, NEAR),
                      int(ay + t * (by - ay)) + rng.randint(-NEAR, NEAR)))
    while len(pins) < n:
        pins.add((rng.randint(-top, top), rng.randint(-top, top)))
    pins = list(pins)
    rng.shuffle(pins)
    print(n, k)
    for x, y in pins:
        print(x, y)


main()
