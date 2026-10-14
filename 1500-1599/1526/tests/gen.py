"""One test from a seed and a mode, with t = 200 unless small. Mode 1
takes ten dishes and random pairs, mode 2 forbids every dish over itself,
so all sets of dishes come up, mode 3 takes a random size, mode 4 is
small, mode 5 takes 100 pairs."""

import random
import sys

LONGEST = 200
DISHES = 10
MOST_PAIRS = 100
TOP_P = 10**4
SMALL = 8


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    p = rng.randint(2, TOP_P)
    n = DISHES if mode in (1, 2, 5) else rng.randint(1, DISHES)
    t = (
        2 * rng.randint(1, SMALL // 2)
        if mode == 4
        else (LONGEST if mode != 3 else 2 * rng.randint(1, LONGEST // 2))
    )
    if mode == 2:
        pairs = [(i, i) for i in range(1, n + 1)]
    else:
        count = MOST_PAIRS if mode == 5 else rng.randint(0, 2 * n)
        pairs = [(rng.randint(1, n), rng.randint(1, n)) for _ in range(count)]
    print(p, t, n, len(pairs))
    for i, j in pairs:
        print(i, j)


main()
