"""One test from a seed and a mode: mode 1 n up to 300, mode 2 random
bits up to 1000 digits, mode 3 a million digits that are all
zeros after the leading one except for the last three, which are
random, so that n is near 2^(k-1) + 7, mode 4 a million
random digits."""

import random
import sys

SMALL = 300
MEDIUM = 1000
MOST = 1000000
TAIL = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(bin(rng.randint(1, SMALL))[2:])
        return
    k = rng.randint(1, MEDIUM) if mode == 2 else MOST
    if mode == 3:
        rest = "0" * (k - 1 - TAIL) + "".join(rng.choice("01") for _ in range(TAIL))
    else:
        rest = "".join(rng.choice("01") for _ in range(k - 1))
    print("1" + rest)


main()
