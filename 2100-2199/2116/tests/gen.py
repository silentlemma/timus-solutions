"""Generate one board: python gen.py MODE SEED."""

import random
import sys

MAX_SIDE = 10**9
MAX_STEP = 3
SMALL_LIMIT = 30
PAIRS = [(a, b) for b in range(MAX_STEP + 1) for a in range(b + 1)]
MODE_SMALL = 1
MODE_RANDOM = 2
MODE_BOUNDARY = 3
MODE_MAXIMUM = 4
MODE_NEAR_MAXIMUM = 5
MODE_EXHAUSTIVE = 6


def generate(mode, seed):
    rng = random.Random(seed)
    a, b = PAIRS[seed % len(PAIRS)]
    if mode == MODE_SMALL:
        n = rng.randint(1, SMALL_LIMIT)
    elif mode == MODE_RANDOM:
        n = rng.randint(1, MAX_SIDE)
        a, b = rng.choice(PAIRS)
    elif mode == MODE_BOUNDARY:
        boundary = (1, max(1, b), b + 1, max(1, 2 * b - 1), max(1, 2 * b), 2 * b + 1)
        n = rng.choice(boundary)
    elif mode == MODE_MAXIMUM:
        n = MAX_SIDE
    elif mode == MODE_NEAR_MAXIMUM:
        n = MAX_SIDE - rng.randrange(2 * MAX_STEP + 1)
    elif mode == MODE_EXHAUSTIVE:
        n = 1 + (seed // len(PAIRS)) % SMALL_LIMIT
    else:
        raise SystemExit("unknown generator mode")
    return n, a, b


def main():
    mode, seed = map(int, sys.argv[1:])
    print(*generate(mode, seed), sep="\n")


if __name__ == "__main__":
    main()
