"""Usage: gen.py SEED MODE; even_edge,odd_boundary,reversed,adjacent,same_center,same_edge,zeros,spike_mid,random_distinct,random_same,near_edge,alternating."""

import random
import sys

MAXIMUM = 100000
WEIGHT = 10000


def generate(seed, mode):
    n = MAXIMUM - 1 if mode in ("odd_boundary", "spike_mid") else MAXIMUM
    values = [WEIGHT] * n
    if mode == "reversed":
        return values, n - 1, 0
    if mode == "adjacent":
        return values, n // 2 - 1, n // 2
    if mode == "same_center":
        return values, n // 2 - 1, n // 2 - 1
    if mode == "same_edge":
        return values, 0, 0
    if mode == "zeros":
        return [0] * n, n // 3, 2 * n // 3
    if mode == "spike_mid":
        values = [0] * n
        values[n // 2] = WEIGHT
        return values, 0, n - 1
    if mode == "near_edge":
        return values, 0, 1
    if mode == "alternating":
        return [WEIGHT if i % 2 else 0 for i in range(n)], n - 2, n - 2
    if mode.startswith("random"):
        rng = random.Random(seed)
        values = [rng.randint(0, WEIGHT) for _ in range(n)]
        first = rng.randrange(n)
        second = first if mode == "random_same" else (first + 1 + rng.randrange(n - 1)) % n
        return values, first, second
    return values, 0, n - 1


if __name__ == "__main__":
    values, first, second = generate(int(sys.argv[1]), sys.argv[2])
    print(len(values))
    print(*values)
    print(first + 1, second + 1)
