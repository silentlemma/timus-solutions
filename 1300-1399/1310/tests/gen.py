"""L, M, K and a state code: a seed and a mode. Mode 1 gives small L, M
and K, mode 2 the largest L with any M and K, mode 3 the largest L, M
and K with a code near the end of the list."""

import random
import sys

LENGTH, TOP, MOD = 100, 50, 50


def count(length, top, k):
    ways = [1] + [0] * (k - 1)
    for _ in range(length):
        row = [0] * k
        for v in range(1, top + 1):
            for r in range(k):
                row[(r + v) % k] += ways[r]
        ways = row
    return ways[0]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            length, top, k = rng.randint(1, 6), rng.randint(2, 8), rng.randint(1, 10)
        elif mode == 2:
            length, top, k = LENGTH, rng.randint(2, TOP), rng.randint(1, MOD)
        else:
            length, top, k = LENGTH, TOP, MOD
        total = count(length, top, k)
        if total > 0:
            break
    code = rng.randrange(total) if mode != 3 else total - 1 - rng.randrange(min(total, 1000))
    print(length, top, k)
    print(code)


main()
