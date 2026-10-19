"""Heights from a seed.

Mode 1: a short line, sorted and then maybe broken by swaps. Mode 2: a long
sorted line with one swap. Mode 3: a long sorted line with two swaps. Mode 4: a
long descending line with repeated heights and one swap.
"""

import random
import sys

SMALL = 6
MAX_N = 10 ** 5
TOP = 10 ** 9
FEW = 3


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else MAX_N
    top = FEW if mode in (1, 4) else TOP
    a = sorted((rng.randint(0, top) for _ in range(n)), reverse=rng.random() < 0.5 or mode == 4)
    swaps = {1: rng.randint(0, 2), 2: 1, 3: 2, 4: 1}[mode]
    for _ in range(swaps):
        i, j = rng.randrange(n), rng.randrange(n)
        a[i], a[j] = a[j], a[i]
    print(n)
    print(*a)


main()
