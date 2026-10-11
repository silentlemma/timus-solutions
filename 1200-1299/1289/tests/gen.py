"""An even number of digits: a seed and a mode. Mode 1 gives up to 20
digits, mode 2 any even number up to 200000, mode 3 the largest, 200000."""

import random
import sys

LARGEST = 200000
SMALL = 20


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = 2 * rng.randint(0, SMALL // 2)
    elif mode == 2:
        n = 2 * rng.randint(0, LARGEST // 2)
    else:
        n = LARGEST
    print(n)


main()
