"""Generate one tree size: python gen.py MODE SEED."""

import random
import sys

MAX_N = 400
SMALL_N = 12
NEAR_MAX = 380
MODE_RANDOM = 1
MODE_SMALL = 2
MODE_LARGE = 3
MODE_MAX = 4
MODE_SWEEP = 5


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == MODE_RANDOM:
        n = rng.randint(1, MAX_N)
    elif mode == MODE_SMALL:
        n = rng.randint(1, SMALL_N)
    elif mode == MODE_LARGE:
        n = rng.randint(NEAR_MAX, MAX_N)
    elif mode == MODE_MAX:
        n = MAX_N
    elif mode == MODE_SWEEP:
        n = seed % MAX_N + 1
    else:
        raise ValueError("unknown mode")
    print(n)


if __name__ == "__main__":
    main()
