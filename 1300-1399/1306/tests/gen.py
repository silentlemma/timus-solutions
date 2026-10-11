"""A sequence: a seed and a mode. Mode 1 gives a few small numbers, mode 2
250000 numbers of any size, mode 3 249999 numbers with many repeats,
mode 4 250000 numbers in decreasing order, mode 5 numbers near 2^31 - 1."""

import random
import sys

COUNT = 250000
TOP = 2**31 - 1


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(0, 9) for _ in range(rng.randint(1, 9))]
    elif mode == 2:
        values = [rng.randint(0, TOP) for _ in range(COUNT)]
    elif mode == 3:
        values = [rng.randint(0, 5) for _ in range(COUNT - 1)]
    elif mode == 4:
        values = sorted((rng.randint(0, TOP) for _ in range(COUNT)), reverse=True)
    else:
        values = [TOP - rng.randint(0, 3) for _ in range(COUNT)]
    print(len(values))
    print("\n".join(map(str, values)))


main()
