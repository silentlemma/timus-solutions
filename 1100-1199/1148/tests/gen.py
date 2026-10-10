"""Tower queries: a seed, N, H, M, the number of queries and a mode. Mode
0 asks random numbers, mode 1 the first and the last tower and their
neighbours, mode 2 numbers near powers of two. The total count comes from
a plain memoized recursion over (bricks left, levels, width)."""

import random
import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def count(n, h, m):
    if m == 0 or n < m:
        return 0
    if h == 1:
        return 1
    return count(n - m, h - 1, m - 1) + count(n - m, h - 1, m + 1)


def main():
    seed, n, h, m, queries, mode = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    sys.setrecursionlimit(10000)
    total = count(min(n, m * h + h * (h - 1) // 2), h, m)
    ks = []
    if total:
        if mode == 1:
            ks = [1, 2, total - 1, total]
        elif mode == 2:
            ks = [1 << rng.randrange(total.bit_length()) for _ in range(queries)]
        else:
            ks = [rng.randint(1, total) for _ in range(queries)]
        ks = [k for k in ks if 1 <= k <= total]
    lines = ["%d %d %d" % (n, h, m)] + [str(k) for k in ks] + ["-1"]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
