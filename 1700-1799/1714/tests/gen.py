"""One test from a seed and a mode: mode 1 a random length up to 40,
mode 2 a random length from 900 to 1000."""

import random
import sys

MOST = 1000
SHORT = 40
LONG = 900


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(1, SHORT) if mode == 1 else rng.randint(LONG, MOST))


main()
