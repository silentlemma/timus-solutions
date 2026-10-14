"""One test from a seed and a mode: mode 1 random n, m and k, mode 2 the
largest n and k, mode 3 n a power of two (the most shared factors),
mode 4 small values."""

import random
import sys

TOP_N = 10**9
TOP_K = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, TOP_N)
        k = rng.randint(0, TOP_K)
    elif mode == 2:
        n, k = TOP_N, TOP_K
    elif mode == 3:
        n, k = 2 ** rng.randint(1, 29), TOP_K
    else:
        n, k = rng.randint(1, 10), rng.randint(0, 20)
    print(n, rng.randint(0, n), k)


main()
