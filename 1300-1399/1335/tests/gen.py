"""Usage: gen.py SEED MODE. Print one seeded random N.

Mode 1: N in [257, 8191], above the 16-bit boundary but below 8192.
Mode 2: N in [8193, 29998], with squared-answer sums above 2^53.
"""

import random
import sys


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.randint(257, 8191))
    elif mode == 2:
        print(rng.randint(8193, 29998))
    else:
        raise ValueError("mode must be 1 or 2")


if __name__ == "__main__":
    main()
