"""One test from a seed and a mode: mode 1 the longest n that is still
listed, mode 2 a random n that is listed, mode 3 any n."""

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
    else:
        print(rng.randint(1, LARGEST))


main()
