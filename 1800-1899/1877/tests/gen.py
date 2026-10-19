"""Two lock codes from a seed and a mode: mode 1 any codes, 2 an odd
first code and an even second one, the only way to stay safe, 3 codes
with leading zeros."""

import random
import sys

CODES = 10000
SMALL = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    a, b = rng.randrange(CODES), rng.randrange(CODES)
    if mode == 2:
        a, b = a | 1, b & ~1
    elif mode == 3:
        a, b = rng.randrange(SMALL), rng.randrange(SMALL)
    print("%04d" % a)
    print("%04d" % b)


main()
