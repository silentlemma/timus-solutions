"""One test from a seed and a mode: mode 1 small values, mode 2 any
values, mode 3 the longest words with k = 2."""

import random
import sys

MOST_M = 18
MOST_N = 22


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        m, k, n = rng.randint(1, 4), rng.randint(2, 3), rng.randint(1, 10)
    elif mode == 2:
        m, k, n = rng.randint(1, MOST_M), rng.randint(2, 5), rng.randint(1, MOST_N)
    else:
        m, k, n = rng.randint(1, MOST_M), 2, rng.randint(MOST_N - 2, MOST_N)
    print(m, k, n)


main()
