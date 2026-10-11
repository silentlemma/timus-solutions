"""A tray and three plates: a seed and a mode. Mode 1 gives small numbers,
mode 2 numbers up to 10^6, mode 3 a tray just around the size where the
three plates fit side by side."""

import random
import sys

TOP = 10**6
SMALL = 40


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        h, w = rng.randint(1, SMALL), rng.randint(1, SMALL)
        radii = [rng.randint(1, SMALL // 2) for _ in range(3)]
    elif mode == 2:
        h, w = rng.randint(1, TOP), rng.randint(1, TOP)
        radii = [rng.randint(1, min(h, w) // 2 + 1) for _ in range(3)]
    else:
        radii = [rng.randint(1, TOP // 8) for _ in range(3)]
        h = 2 * sum(radii) + rng.randint(-2, 2)
        w = 2 * max(radii) + rng.randint(-1, 1)
    print(h, w, *radii)


main()
