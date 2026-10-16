"""One test from a seed and a mode: an even side n from 4 to 10 and a
number k of a grille; mode 1 any k, mode 2 k near the number of
grilles, mode 3 a small k."""

import random
import sys

TURNS = 4
LOW = 4
HIGH = 10
TOP_K = 10 ** 18
NEAR = 1000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.choice(range(LOW, HIGH + 1, 2))
    total = min(TURNS ** (n * n // TURNS), TOP_K)
    if mode == 1:
        k = rng.randint(1, total)
    elif mode == 2:
        k = total - rng.randint(0, min(NEAR, total - 1))
    else:
        k = rng.randint(1, NEAR)
    print(n, k)


main()
