"""One test from a seed and a mode, ending with 0 0. Mode 1 takes 5000
cases with large n and p, mode 2 random n and p of any size, mode 3 many
cases with n at least p. Mode 4 reuses a small set of n values with random
small, nearby, and large moduli to check that each query is independent."""

import random
import sys

CASES = 5000
LARGEST_N = 10000
LARGEST_P = 2 * 10**9


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    for _ in range(CASES):
        if mode == 1:
            n, p = rng.randint(LARGEST_N - 1000, LARGEST_N), rng.randint(LARGEST_P // 2, LARGEST_P)
        elif mode == 3:
            p = rng.randint(2, LARGEST_N)
            n = rng.randint(p, LARGEST_N)
        elif mode == 4:
            n = rng.choice((2, 3, 7, 25, 99, 100, 101, 9999, LARGEST_N))
            band = rng.randrange(3)
            if band == 0:
                p = rng.randint(2, n + 1)
            elif band == 1:
                p = rng.randint(n + 1, 2 * n + 1)
            else:
                p = rng.randint(LARGEST_P // 2, LARGEST_P)
        else:
            n, p = rng.randint(1, LARGEST_N), rng.randint(2, LARGEST_P)
        print(n, p)
    print(0, 0)


main()
