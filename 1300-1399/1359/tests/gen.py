"""Seed and mode. Mode 1: random wide, shallow descent (20..50 by 2..15).
Mode 2: random narrow, deep descent (2..15 by 20..50).
Mode 3: random near-limit rectangle (both dimensions 40..50).
"""

import random
import sys


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(20, 50), rng.randint(2, 15)
    elif mode == 2:
        n, m = rng.randint(2, 15), rng.randint(20, 50)
    elif mode == 3:
        n, m = rng.randint(40, 50), rng.randint(40, 50)
    else:
        raise ValueError('mode must be 1, 2, or 3')
    print(n, m)


if __name__ == '__main__':
    main()
