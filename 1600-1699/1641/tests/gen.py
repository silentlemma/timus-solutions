"""One test from a seed and a mode: n, k and a feasible m (mode 1 small,
mode 2 up to 100 students, mode 3 the fewest days, mode 4 the most)."""

import random
import sys

MOST = 100


def most_pairs(n, k):
    """pairs from different rooms when the rooms are as even as possible"""
    sizes = [n // k + (1 if r < n % k else 0) for r in range(k)]
    return (n * n - sum(s * s for s in sizes)) // 2


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 8) if mode == 1 else rng.randint(2, MOST)
    k = rng.randint(2, n)
    low, high = (n + 1) // 2, most_pairs(n, k)
    m = {3: low, 4: high}.get(mode, rng.randint(low, high))
    print(n, k, m)


main()
