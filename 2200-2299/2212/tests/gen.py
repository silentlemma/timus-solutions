"""Generate one valid input: python gen.py MODE SEED, with MODE from 1 through 9."""

import random
import sys

MAX_N = 100_000
MAX_DAYS = 10_000_000
MAX_VALUE = 100_000_000
SMALL_N = 64
MEDIUM_N = 4096
MODE_SMALL = 1
MODE_MEDIUM = 2
MODE_MAX_RANDOM = 3
MODE_MAX_VALUES = 4
MODE_ONES = 5
MODE_ONE_DAY = 6
MODE_BOUNDARY = 7
MODE_TWO_DAYS = 8
MODE_RANDOM = 9


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL:
        n = rng.randint(2, SMALL_N)
    elif mode == MODE_MEDIUM:
        n = rng.randint(SMALL_N + 1, MEDIUM_N)
    elif mode == MODE_BOUNDARY:
        sizes = [
            (1 << power) + delta
            for power in range(1, MAX_N.bit_length())
            for delta in (-1, 0, 1)
            if 2 <= (1 << power) + delta <= MAX_N
        ]
        n = rng.choice(sizes)
    elif mode == MODE_RANDOM:
        n = rng.randint(2, MAX_N)
    elif MODE_MAX_RANDOM <= mode <= MODE_TWO_DAYS:
        n = MAX_N
    else:
        raise ValueError("mode must be between 1 and 9")

    days = rng.choice((1, 2, MAX_DAYS, rng.randint(1, MAX_DAYS)))
    if mode in (MODE_MAX_RANDOM, MODE_MAX_VALUES, MODE_ONES):
        days = MAX_DAYS
    elif mode == MODE_ONE_DAY:
        days = 1
    elif mode == MODE_TWO_DAYS:
        days = 2

    if mode == MODE_MAX_VALUES:
        values = [MAX_VALUE] * n
    elif mode == MODE_ONES:
        values = [1] * n
    elif mode == MODE_ONE_DAY:
        values = [MAX_VALUE if i % 2 == 0 else 1 for i in range(n)]
    else:
        values = [rng.randint(1, MAX_VALUE) for _ in range(n)]
    print(n, days)
    print(*values)


if __name__ == "__main__":
    generate(*map(int, sys.argv[1:]))
