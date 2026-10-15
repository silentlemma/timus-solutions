"""One test from a seed and a mode: mode 1 small sizes, mode 2 the largest
sizes with any K and L, mode 3 K = M or L = N, mode 4 a thin board."""

import random
import sys

MOST = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        m, n = rng.randint(1, 10), rng.randint(1, 10)
    elif mode == 4:
        m, n = rng.randint(1, 3), rng.randint(1, MOST)
    else:
        m, n = rng.randint(MOST // 2, MOST), rng.randint(MOST // 2, MOST)
    k, l = rng.randint(0, m), rng.randint(0, n)
    if mode == 3:
        if rng.random() < 0.5:
            k = m
        else:
            l = n
    print(m, n, k, l)


main()
