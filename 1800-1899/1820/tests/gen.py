"""One test from a seed and a mode: mode 1 random n and k in [1, 1000]."""

import random
import sys

LIMIT = 1000


def main():
    seed, mode = (int(value) for value in sys.argv[1:])
    if mode != 1:
        raise ValueError("unknown mode")
    rng = random.Random(seed)
    print(rng.randint(1, LIMIT), rng.randint(1, LIMIT))


main()
