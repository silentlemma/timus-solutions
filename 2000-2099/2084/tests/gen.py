"""Tasks from a seed.

Mode 1: a few tasks with small values. Mode 2: 200 tasks, X = 100, any values.
Mode 3: 200 tasks, X = 100, small repairs and utilities near X. Mode 4: X = 0.
"""

import random
import sys

SMALL_N = 7
MAX_N = 200
MAX_X = 100
MAX_A = 100
MAX_B = 10 ** 6
SMALL = 12
NEAR = 30


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n, x = rng.randint(1, SMALL_N), rng.randint(0, SMALL)
        a = [rng.randint(0, SMALL // 2) for _ in range(n)]
        b = [rng.randint(0, SMALL + SMALL // 2) for _ in range(n)]
    else:
        n, x = MAX_N, (0 if mode == 4 else MAX_X)
        if mode == 3:
            a = [rng.randint(0, SMALL // 2) for _ in range(n)]
            b = [rng.randint(MAX_X - NEAR, MAX_X + NEAR) for _ in range(n)]
        else:
            a = [rng.randint(0, MAX_A) for _ in range(n)]
            b = [rng.randint(0, MAX_B) for _ in range(n)]
    print(x, n)
    print(*a)
    print(*b)


main()
