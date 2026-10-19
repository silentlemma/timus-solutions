"""Programs and courses from a seed.

Mode 1: small tables. Mode 2: 100 by 100 at random. Mode 3: 100 by 100 with
rare ones. Mode 4: 100 by 100 of ones only.
"""

import random
import sys

MAX = 100
MIN = 4
SMALL = 8
HALF = 0.5
RARE = 0.05
ALL = 1.0


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n, m = (rng.randint(MIN, SMALL), rng.randint(MIN, SMALL)) if mode == 1 else (MAX, MAX)
    share = {1: HALF, 2: HALF, 3: RARE}.get(mode, ALL)
    print(n, m)
    for _ in range(n):
        print(*(int(rng.random() < share) for _ in range(m)))


main()
