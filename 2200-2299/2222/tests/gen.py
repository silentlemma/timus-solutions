"""Print one board width: python gen.py MODE SEED."""

import random
import sys

MAX_N = 100_000
SMALL_LIMIT = 64
MAX_POWER = MAX_N.bit_length()
SMALL = 1
RANDOM = 2
MAXIMUM = 3
NEAR_MAXIMUM = 4
POWER_BOUNDARY = 5


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == SMALL:
        n = rng.randint(1, SMALL_LIMIT)
    elif mode == RANDOM:
        n = rng.randint(1, MAX_N)
    elif mode == MAXIMUM:
        n = MAX_N
    elif mode == NEAR_MAXIMUM:
        n = MAX_N - rng.randrange(SMALL_LIMIT)
    elif mode == POWER_BOUNDARY:
        n = (1 << rng.randrange(MAX_POWER)) + rng.randint(-2, 2)
        n = max(1, min(MAX_N, n))
    else:
        raise SystemExit("unknown mode")
    print(n)


if __name__ == "__main__":
    main()
