"""Slipper counts from a seed and a mode: mode 1 any counts, 2 more left
slippers than right ones, 3 more right slippers than left ones, 4 equal
counts."""

import random
import sys

FEWEST = 40
MOST = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    a, b = rng.randint(FEWEST, MOST), rng.randint(FEWEST, MOST)
    if mode == 2:
        a, b = max(a, b) + 1 if max(a, b) < MOST else MOST, min(a, b)
    elif mode == 3:
        a, b = min(a, b), max(a, b) + 1 if max(a, b) < MOST else MOST
    elif mode == 4:
        b = a
    print(a, b)


main()
