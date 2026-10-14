"""One test from a seed and a mode, with K chosen so that the first K - 1
columns of the minimal height do not use up all N numbers. Mode 1 takes
random N and K, mode 2 takes N = 100 with three-digit numbers, mode 3
takes K = N, a single row, mode 4 takes K = 1, a single column."""

import random
import sys

LARGEST = 100
TOP = 999
WIDE = 100


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        n = LARGEST if mode == 2 else rng.randint(1, LARGEST)
        k = {3: n, 4: 1}.get(mode, rng.randint(1, n))
        height = -(-n // k)
        if (k - 1) * height < n:
            break
    low = WIDE if mode == 2 else 0
    print(n, k)
    print(" ".join(str(rng.randint(low, TOP)) for _ in range(n)))


main()
