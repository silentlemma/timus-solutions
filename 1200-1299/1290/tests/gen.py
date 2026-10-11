"""N numbers from 1 to 25000: a seed and a mode. Mode 1 gives a few small
numbers with repeats, mode 2 up to 25000 numbers of any size, mode 3
exactly 25000 numbers with many repeats."""

import random
import sys

LARGEST = 25000
FEW = 10
REPEATS = 50


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        p = [rng.randint(1, FEW) for _ in range(rng.randint(1, FEW))]
    elif mode == 2:
        p = [rng.randint(1, LARGEST) for _ in range(rng.randint(1, LARGEST))]
    else:
        p = [rng.randint(1, REPEATS) * REPEATS for _ in range(LARGEST)]
    print(len(p))
    print("\n".join(map(str, p)))


main()
