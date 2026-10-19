"""Generate from seed and mode: 1 small, 2 medium, 3 maximal random,
4 around word boundaries, 5 maximal k=1, 6 maximal k=2, 7 maximal k=n.
All generated inputs satisfy 1 <= k <= n <= 1100000."""

import random
import sys

MAX_COUNT = 1_100_000
MEDIUM_COUNT = 10_000
SMALL_COUNT = 200
WORD_BITS = 64
BOUNDARY_MULTIPLIERS = 3
SMALL_MODE = 1
MEDIUM_MODE = 2
MAXIMAL_MODE = 3
BOUNDARY_MODE = 4
UNIT_MODE = 5
TWO_MODE = 6
LAST_MODE = 7


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == SMALL_MODE:
        n = rng.randint(1, SMALL_COUNT)
    elif mode == MEDIUM_MODE:
        n = rng.randint(SMALL_COUNT + 1, MEDIUM_COUNT)
    elif mode == BOUNDARY_MODE:
        n = WORD_BITS * rng.randint(1, BOUNDARY_MULTIPLIERS) + rng.choice((-1, 0, 1))
    else:
        n = MAX_COUNT
    k = rng.randint(1, n)
    if mode == UNIT_MODE:
        k = 1
    elif mode == TWO_MODE:
        k = 2
    elif mode == LAST_MODE:
        k = n
    return n, k


def render(n, k):
    return f"{n} {k}\n"


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode not in range(SMALL_MODE, LAST_MODE + 1):
        raise ValueError("mode must be from 1 to 7")
    sys.stdout.write(render(*generate(seed, mode)))


if __name__ == "__main__":
    main()
