"""Flower dryness from a seed.

Mode 1: up to 8 flowers with dryness 1 to 3. Mode 2: 10^5 flowers with
dryness 1 to 10. Mode 3: 10^5 flowers with any dryness. Mode 4: 10^5 flowers,
two values alternating, so every group spans the whole bed.
Mode 5: 10^5 distinct dryness values, with their watering order alternating
between shuffled left and right halves to force a total beyond 32 bits.
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
    elif mode == 5:
        n = MAX_N
        left = list(range(n // 2))
        right = list(range(n // 2, n))
        rng.shuffle(left)
        rng.shuffle(right)
        values = [0] * n
        for i, (lo, hi) in enumerate(zip(left, right)):
            values[lo] = 1 + (MAX_VALUE - 1) * (2 * i) // (n - 1)
            values[hi] = 1 + (MAX_VALUE - 1) * (2 * i + 1) // (n - 1)
    else:
        n = MAX_N
        top = FEW if mode == 2 else MAX_VALUE
        values = [rng.randint(1, top) for _ in range(n)]
    print(n)
    print(*values)


main()
