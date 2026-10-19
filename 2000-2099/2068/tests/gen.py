"""An odd number of heaps up to 777, each an odd size up to 54321, from a seed.

Mode 1 takes sizes 1 to 9, mode 2 any size, mode 3 the largest sizes.
"""

import random
import sys

MAX_N = 777
MAX_A = 54321
SMALL = 9
NEAR = 100


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = MAX_N if mode == 3 else rng.randrange(1, MAX_N + 1, 2)
    if mode == 1:
        top, low = SMALL, 1
    elif mode == 2:
        top, low = MAX_A, 1
    else:
        top, low = MAX_A, MAX_A - NEAR
    print(n)
    print(*(rng.randrange(low, top + 1, 2) for _ in range(n)))


main()
