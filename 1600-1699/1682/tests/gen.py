"""One test from a seed and a mode: mode 1 a small k, mode 2 a large k,
mode 3 a large power of two or a multiple of a large square."""

import random
import sys

MOST_K = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        k = rng.randint(1, 100)
    elif mode == 2:
        k = rng.randint(MOST_K // 2, MOST_K)
    else:
        base = rng.choice((2, 3, 5, 7, 10))
        k = base
        while k * base <= MOST_K:
            k *= base
        k *= rng.randint(1, MOST_K // k)
    print(k)


main()
