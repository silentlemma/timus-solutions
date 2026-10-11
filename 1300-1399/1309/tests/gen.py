"""n: a seed and a mode. Mode 1 gives any n up to 10^8, mode 2 an n just
around a multiple of 9973."""

import random
import sys

TOP = 10**8
MOD = 9973


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(0, TOP)
    else:
        n = min(TOP, rng.randint(0, TOP // MOD) * MOD + rng.randint(-1, 1))
    print(max(n, 0))


main()
