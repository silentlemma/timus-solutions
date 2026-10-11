"""A sequence: a seed and a mode. Mode 1 gives up to 60000 numbers of
any sign, mode 2 60000 copies of 30000, mode 3 60000 negative numbers,
mode 4 mostly small negative numbers with a few large positive ones."""

import random
import sys

LENGTH = 60000
TOP = 30000
RARE = 50


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        p = [rng.randint(-TOP, TOP) for _ in range(rng.randint(1, LENGTH))]
    elif mode == 2:
        p = [TOP] * LENGTH
    elif mode == 3:
        p = [rng.randint(-TOP, -1) for _ in range(LENGTH)]
    else:
        p = [
            rng.randint(TOP // 2, TOP) if rng.randrange(RARE) == 0 else rng.randint(-RARE, -1)
            for _ in range(LENGTH)
        ]
    print(len(p))
    print("\n".join(map(str, p)))


main()
