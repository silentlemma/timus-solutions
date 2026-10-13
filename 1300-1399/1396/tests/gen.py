"""Queries: a seed and a mode, 10 000 numbers each. Mode 1 is random below
10^18, mode 2 random below 10^5, mode 3 alternating bit patterns and their
neighbours, where the largest values sit, mode 4 powers of two and their
neighbours."""

import random
import sys

COUNT = 10000
TOP = 10**18 - 1


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(1, TOP) for _ in range(COUNT)]
    elif mode == 2:
        values = [rng.randint(1, 10**5) for _ in range(COUNT)]
    else:
        values = []
        while len(values) < COUNT:
            k = rng.randint(1, 59)
            if mode == 3:
                base = int(("10" * 30)[:k], 2)
                base |= rng.choice((0, 1)) << k
            else:
                base = 1 << k
            values.append(min(TOP, max(1, base + rng.randint(-2, 2))))
    print("\n".join(map(str, values)))
    print(0)


main()
