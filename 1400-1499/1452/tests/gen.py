"""Sequences: a seed, N and a mode. Mode 1 draws values up to 10^9, mode 2
hides a progression of N / 4 members among random values, mode 3 is a
shuffled progression of all N members, mode 4 takes values from a small
range with many repeats, mode 5 removes the middle term from an N + 1
member progression spanning 0 to at most 10^9."""

import random
import sys

TOP = 10**9
SMALL = 50


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        s = [rng.randint(0, TOP) for _ in range(n)]
    elif mode == 2:
        k = n // 4
        d = rng.randint(1, TOP // k)
        start = rng.randint(0, TOP - d * (k - 1))
        s = [start + d * i for i in range(k)] + [rng.randint(0, TOP) for _ in range(n - k)]
    elif mode == 3:
        d = rng.randint(1, TOP // n)
        s = [d * i for i in range(n)]
    elif mode == 5:
        d = TOP // n
        s = [d * i for i in range(n + 1) if i != n // 2]
    else:
        s = [rng.randint(0, SMALL) for _ in range(n)]
    rng.shuffle(s)
    print(n)
    print(" ".join(map(str, s)))


main()
