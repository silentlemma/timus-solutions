"""One test from a seed and a mode: a pineapple and a number of pieces.
Mode 1 is random with up to two decimals, mode 2 nearly round (a close to
b), mode 3 long and thin with 100 pieces."""

import random
import sys

TOP = 100
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        b = round(rng.uniform(2, TOP), 2)
        a = round(b - rng.uniform(0.01, 0.5), 2)
    elif mode == 3:
        a, b = round(rng.uniform(1, 2), 2), round(rng.uniform(TOP - 10, TOP), 2)
    else:
        a, b = sorted(round(rng.uniform(1, TOP), 2) for _ in range(2))
        if a == b:
            a = b - 1
    n = MOST if mode == 3 else rng.randint(1, MOST)
    print(a, b, n)


main()
