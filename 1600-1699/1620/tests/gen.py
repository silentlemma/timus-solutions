"""One test from a seed and a mode: mode 1 random n, m and k, mode 2 the
largest n and k, mode 3 n a power of two (the most shared factors),
mode 4 small values, mode 5 nearly maximal odd n with all bulbs off,
mode 6 nearly maximal odd n with all bulbs on, mode 7 odd n with small
prime factors and m divisible by three, mode 8 large even n with m one
away from half. Modes 5 through 8 use the largest k."""

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
    elif mode in (5, 6):
        n, k = TOP_N - 2 * rng.randint(0, 499) - 1, TOP_K
    elif mode == 7:
        n = 3 ** rng.randint(2, 7) * 5 ** rng.randint(1, 3) * 7 ** rng.randint(1, 2)
        k = TOP_K
    elif mode == 8:
        n, k = 2 * rng.randint(TOP_N // 4, TOP_N // 2), TOP_K
    else:
        n, k = rng.randint(1, 10), rng.randint(0, 20)
    if mode == 5:
        m = 0
    elif mode == 6:
        m = n
    elif mode == 7:
        m = 3 * rng.randint(0, n // 3)
    elif mode == 8:
        m = n // 2 + rng.choice((-1, 1))
    else:
        m = rng.randint(0, n)
    print(n, m, k)


main()
