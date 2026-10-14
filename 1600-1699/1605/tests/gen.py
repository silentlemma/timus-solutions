"""One test from a seed and a mode.

Mode 1: a random even n between 1000 and 49998.
Mode 2: a random odd n between 50001 and 99997.
"""

import random
import sys


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randrange(1000, 50000, 2)
    elif mode == 2:
        n = rng.randrange(50001, 99999, 2)
    else:
        raise ValueError("mode must be 1 or 2")
    print(n)


if __name__ == "__main__":
    main()
