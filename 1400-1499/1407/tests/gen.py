"""Generate one exponent: SEED MODE.

Mode 1: a uniformly random N from 41 through 98, between the 128-bit
decimal-answer boundary and the two largest existing tests.
"""

import random
import sys


def main():
    seed, mode = (int(arg) for arg in sys.argv[1:])
    if mode != 1:
        raise SystemExit("mode must be 1")
    print(random.Random(seed).randint(41, 98))


if __name__ == "__main__":
    main()
