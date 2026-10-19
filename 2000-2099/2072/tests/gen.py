"""Flower dryness from a seed.

Mode 1: up to 8 flowers with dryness 1 to 3. Mode 2: 10^5 flowers with
dryness 1 to 10. Mode 3: 10^5 flowers with any dryness. Mode 4: 10^5 flowers,
two values alternating, so every group spans the whole bed.
"""

import random
import sys

SMALL_N = 8
SMALL_VALUE = 3
MAX_N = 10 ** 5
FEW = 10
MAX_VALUE = 10 ** 9


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        values = [rng.randint(1, SMALL_VALUE) for _ in range(n)]
    elif mode == 4:
        n = MAX_N
        values = [MAX_VALUE - i % 2 for i in range(n)]
    else:
        n = MAX_N
        top = FEW if mode == 2 else MAX_VALUE
        values = [rng.randint(1, top) for _ in range(n)]
    print(n)
    print(*values)


main()
