"""n and the values from a seed: mode 1 small n and small values, mode 2
the maximum n with random values, mode 3 the maximum n with values of
alternating sign at the bounds, mode 4 all values at the lower bound."""

import random
import sys

MAX_N = 10 ** 5
MAX_A = 10 ** 5
SMALL_N = 8
SMALL_A = 5


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        values = [rng.randint(-SMALL_A, SMALL_A) for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        values = [rng.randint(-MAX_A, MAX_A) for _ in range(n)]
    elif mode == 3:
        n = MAX_N
        values = [MAX_A if i % 2 == 0 else -MAX_A for i in range(n)]
    else:
        n = MAX_N
        values = [-MAX_A] * n
    print(n)
    print(*values)


main()
