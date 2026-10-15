"""One test from a seed and a mode: queries made from random numbers of up
to 100 digits (so mostly answerable), mode 1 few of them, mode 2 10000,
mode 3 10000 queries anywhere in the range (mostly impossible)."""

import random
import sys

MOST = 10000
LONGEST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    t = rng.randint(1, 10) if mode == 1 else MOST
    print(t)
    for _ in range(t):
        if mode == 3:
            print(rng.randint(1, MOST), rng.randint(1, MOST))
        else:
            digits = [rng.randint(0, 9) for _ in range(rng.randint(1, LONGEST))]
            s1 = sum(digits) or 1
            s2 = sum(d * d for d in digits) or 1
            print(s1, s2)


main()
