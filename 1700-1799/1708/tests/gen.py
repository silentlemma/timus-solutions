"""Generate one base.

Modes:
    1 BASE: print BASE (the original fixed-base mode).
    random SEED LOW HIGH: choose a seeded random base in inclusive LOW..HIGH.
"""

import random
import sys


def main():
    if sys.argv[1] == "random":
        seed, low, high = map(int, sys.argv[2:])
        if not 2 <= low <= high <= 36:
            raise ValueError("expected 2 <= LOW <= HIGH <= 36")
        print(random.Random(seed).randint(low, high))
    else:
        print(int(sys.argv[2]))


main()
