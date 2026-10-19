"""A segment [L; R] from a seed.

Mode 1: a short segment anywhere up to 10^12. Mode 2: a long random segment.
"""

import random
import sys

TOP = 10 ** 12
SHORT = 1000


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        left = rng.randint(2, TOP - SHORT)
        right = left + rng.randint(0, SHORT)
    else:
        left, right = sorted(rng.randint(2, TOP) for _ in range(2))
    print(left, right)


main()
