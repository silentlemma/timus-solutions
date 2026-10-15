"""One test from a seed and a mode: mode 1 a small board, mode 2 any
board with any k, mode 3 the largest board with k near its upper end."""

import random
import sys

SMALL = 10
LARGEST = 1000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = 2 * rng.randint(2, SMALL // 2)
    elif mode == 2:
        n = 2 * rng.randint(2, LARGEST // 2)
    else:
        n = LARGEST
    top = n * n // 4
    k = rng.randint(max(2, top - n), top) if mode == 3 else rng.randint(2, top)
    print(n, k)


main()
