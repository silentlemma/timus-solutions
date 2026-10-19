"""Pins of ten frames from a seed: mode 1 any values, mode 2 mostly tens."""

import random
import sys

FRAMES = 10
PINS = 10
LAST = 30
OFTEN = 0.6  # the share of tens in mode 2


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    totals = []
    for _ in range(FRAMES - 1):
        if mode == 2 and rng.random() < OFTEN:
            totals.append(PINS)
        else:
            totals.append(rng.randint(0, PINS))
    totals.append(rng.randint(0, LAST))
    print(*totals)


main()
