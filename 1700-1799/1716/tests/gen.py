"""One test from a seed and a mode: mode 1 small n, mode 2 n up to 5000;
the total size s is anything from 2n to 3n."""

import random
import sys

MOST = 5000
SMALL = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL if mode == 1 else MOST)
    print(n, rng.randint(2 * n, 3 * n))


main()
