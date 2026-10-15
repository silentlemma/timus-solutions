"""One test from a seed and a mode: mode 1 small values, mode 2 the
largest n and k with any p, mode 3 any values with a small p."""

import random
import sys

MOST_N = 1000
MOST_K = 200
MOST_P = 10 ** 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, k, p = rng.randint(1, 8), rng.randint(1, 6), rng.randint(2, 50)
    elif mode == 2:
        n, k, p = MOST_N, MOST_K, rng.randint(2, MOST_P)
    else:
        n, k, p = rng.randint(1, MOST_N), rng.randint(1, MOST_K), rng.randint(2, 10)
    print(n, k, p)


main()
