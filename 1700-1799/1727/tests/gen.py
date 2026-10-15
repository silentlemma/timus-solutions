"""One test from a seed and a mode: mode 1 n up to 100, mode 2 any n."""

import random
import sys

LIMIT = 10 ** 5
SMALL = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(1, SMALL if mode == 1 else LIMIT - 1))


main()
