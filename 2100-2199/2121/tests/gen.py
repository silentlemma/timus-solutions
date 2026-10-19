"""a from a seed: mode 1 a random a up to 10^18, mode 2 a small a, mode 3 an a
near the upper limit."""

import random
import sys

TOP = 10 ** 18
SMALL = 1000
NEAR = 10 ** 6


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        a = rng.randint(1, TOP)
    elif mode == 2:
        a = rng.randint(1, SMALL)
    else:
        a = TOP - rng.randint(0, NEAR)
    print(a)


main()
