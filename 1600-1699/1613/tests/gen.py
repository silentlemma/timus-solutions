"""One test from a seed and a mode, with 69999 cities and 69999 queries.
Mode 1 draws counts from a few values, mode 2 from all values up to
10^9 - 1 with queries asking for counts that exist somewhere, mode 3
gives every city the same count, mode 4 is a small test."""

import random
import sys

MOST = 69999
TOP = 10**9 - 1
FEW = 30


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = q = rng.randint(1, FEW) if mode == 4 else MOST
    if mode == 1 or mode == 4:
        values = [rng.randint(1, TOP) for _ in range(rng.randint(1, 10))]
        counts = [rng.choice(values) for _ in range(n)]
    elif mode == 2:
        counts = [rng.randint(1, TOP) for _ in range(n)]
    else:
        counts = [rng.randint(1, TOP)] * n
    print(n)
    print(*counts)
    print(q)
    for _ in range(q):
        lo = rng.randint(1, n)
        hi = rng.randint(lo, min(n, lo + rng.choice([0, 10, 1000, n])))
        x = rng.choice(counts) if rng.random() < 0.8 else rng.randint(1, TOP)
        print(lo, hi, x)


main()
