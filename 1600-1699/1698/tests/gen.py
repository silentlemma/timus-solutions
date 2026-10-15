"""One test from a seed and a mode: mode 1 a small n, mode 2 any n."""

import random
import sys

MOST_N = 2000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(1, 30) if mode == 1 else rng.randint(1, MOST_N))


main()
