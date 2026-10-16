"""One test from a seed and a mode: mode 1 the longest n that is still
listed, mode 2 a random n that is listed, mode 3 any n, mode 4 the
first n whose six words contain more than 65535 letters."""

import random
import sys

LIMIT = 100000
NAMES = 6
LARGEST = 20000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    longest = LIMIT // NAMES
    if mode == 1:
        print(longest)
    elif mode == 2:
        print(rng.randint(1, longest))
    elif mode == 4:
        print(65536 // NAMES + 1)
    else:
        print(rng.randint(1, LARGEST))


main()
