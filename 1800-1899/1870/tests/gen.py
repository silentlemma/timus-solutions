"""A board size from a seed and a mode: mode 1 small, 2 large and prime
to 6, 3 large and divisible by 2 or 3, 4 the largest sizes,
5 an explicit size supplied as the third argument (4..100000)."""

import random
import sys
from math import gcd

SMALL = 30
MOST = 10 ** 5
BAD = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(4, SMALL)
    elif mode == 5:
        n = int(sys.argv[3])
        if not 4 <= n <= MOST:
            raise ValueError("board size must be in 4..100000")
    elif mode == 4:
        n = rng.choice([MOST, MOST - 1, MOST - 3])
    else:
        while True:
            n = rng.randint(MOST // 2, MOST)
            if (gcd(n, BAD) == 1) == (mode == 2):
                break
    print(n)


main()
