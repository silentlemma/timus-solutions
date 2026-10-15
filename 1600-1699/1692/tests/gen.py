"""One test from a seed and a mode: mode 1 a small n, mode 2 any n, mode 3
n = k(k - 1) / 2 exactly or one less."""

import random
import sys

MOST_N = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(3, 20)
    elif mode == 2:
        n = rng.randint(3, MOST_N)
    else:
        k = rng.randint(3, 45)
        n = k * (k - 1) // 2 - rng.randint(0, 1)
        n = max(n, 3)
    print(n)


main()
