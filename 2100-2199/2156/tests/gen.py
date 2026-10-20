"""Friends from "MODE SEED": mode 1 a few small values; mode 2 10^5
random values; mode 3 10^5 equal values; mode 4 10^5 values with many
equal neighbours; mode 5 10^5 strictly increasing values spanning both
bounds; mode 6 10^5 alternating bounds; mode 7 99999 values with seeded,
isolated dips of distinct depths in a constant plateau."""

import random
import sys

MAX_N = 10 ** 5
MAX_A = 10 ** 9
SMALL_N = 8
SMALL_A = 4


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(3, SMALL_N)
        a = [rng.randint(1, SMALL_A) for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        a = [rng.randint(1, MAX_A) for _ in range(n)]
    elif mode == 3:
        n = MAX_N
        a = [rng.randint(1, MAX_A)] * n
    elif mode == 4:
        n = MAX_N
        a = []
        while len(a) < n:
            a += [rng.randint(1, MAX_A)] * rng.randint(1, SMALL_N)
        a = a[:n]
    elif mode == 5:
        n = MAX_N
        a = [1 + i * (MAX_A - 1) // (n - 1) for i in range(n)]
    elif mode == 6:
        n = MAX_N
        a = [1, MAX_A] * (n // 2)
    elif mode == 7:
        n = MAX_N - 1
        a = [MAX_A] * n
        positions = rng.sample(range(1, n - 1, 3), SMALL_N)
        depths = rng.sample(range(1, MAX_A), SMALL_N)
        for position, depth in zip(positions, depths):
            a[position] = MAX_A - depth
    else:
        raise ValueError("unknown mode")
    print(n)
    print(*a)


main()
