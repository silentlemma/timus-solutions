"""One test from a seed and a mode, a permutation of n = 20000 unless
small. Mode 1 is random with a random k, mode 2 decreasing with k = 10,
mode 3 increasing, mode 4 small, mode 5 decreasing with a few swaps."""

import random
import sys

LARGEST = 20000
MOST_K = 10
SMALL = 9
SWAPS = 30


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 4 else LARGEST
    k = MOST_K if mode in (2, 5) else rng.randint(2, MOST_K)
    perm = list(range(1, n + 1))
    if mode in (2, 5):
        perm.reverse()
    if mode == 5:
        for _ in range(SWAPS):
            i, j = rng.randrange(n), rng.randrange(n)
            perm[i], perm[j] = perm[j], perm[i]
    elif mode in (1, 4):
        rng.shuffle(perm)
    print(n, k)
    print(" ".join(map(str, perm)))


main()
