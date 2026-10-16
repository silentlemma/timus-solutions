"""One test from a seed and a mode: mode 1 a table of 6 to 200 sectors,
mode 2 any table up to 10^9 sectors."""

import random
import sys

FEWEST = 6
SMALL = 200
MOST = 10**9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(FEWEST, SMALL if mode == 1 else MOST))


main()
