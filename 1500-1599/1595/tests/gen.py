"""One test from two integers: a seed (or N for mode 4) and a mode.

Mode 1: the largest N. Mode 2: random N up to the largest.
Mode 3: random N up to 1000. Mode 4: the first argument is an exact N.
"""

import random
import sys

MOST = 250000
SMALL = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(MOST)
    elif mode == 2:
        print(rng.randint(1, MOST))
    elif mode == 4:
        if not 1 <= seed <= MOST:
            raise ValueError("N must be in 1..250000")
        print(seed)
    else:
        print(rng.randint(1, SMALL))


main()
