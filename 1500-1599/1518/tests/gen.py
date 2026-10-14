"""One test from a seed and a mode, with X and Y below 2^28. Mode 1 takes
N = 100 with random keys and shifts, mode 2 takes N = 100 with every
shift 1, mode 3 takes a random small N, mode 4 sets every shift to 0
except one, mode 5 takes X = 2^28 - 1 and the largest modulus, and mode 6
takes N = 100, a small composite modulus and several full window rollovers."""

import random
import sys

LARGEST = 100
LIMIT = 2**28
SMALL = 5
TOP = 100


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 3 else LARGEST
    if mode == 6:
        x = rng.randint(2 * n + 1, 10 * n)
        y = rng.choice((4, 8, 9, 12, 16, 25, 27, 32, 49, 64, 81, 100))
    else:
        x = LIMIT - 1 if mode == 5 else rng.randint(n + 1, LIMIT - 1)
        y = LIMIT - 1 if mode == 5 else rng.randint(2, LIMIT - 1)
    keys = [rng.randint(0, TOP) for _ in range(n)]
    if mode == 2 or mode == 5:
        shifts = [1] * n
    elif mode == 4:
        shifts = [0] * n
        shifts[rng.randrange(n)] = 1
    else:
        shifts = [rng.randint(0, 1) for _ in range(n)]
    print(n, x, y)
    print(" ".join(map(str, keys)))
    print(" ".join(map(str, shifts)))


main()
