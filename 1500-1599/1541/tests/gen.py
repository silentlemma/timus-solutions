"""One test from a seed and a mode: coprime M and N up to 50 with
M / N <= 3. Mode 1 takes a random pair, mode 2 one with M / N above 2.5,
mode 3 one with M and N up to 10."""

import random
import sys
from math import gcd

TOP = 50
SMALL = 10
MOST_HOURS = 3
NEAR = 2.5


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 3 else TOP
    while True:
        m, n = rng.randint(1, top), rng.randint(1, top)
        if gcd(m, n) == 1 and m <= MOST_HOURS * n and (mode != 2 or m > NEAR * n):
            break
    print(m, n)


main()
