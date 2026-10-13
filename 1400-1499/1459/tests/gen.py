"""Modes: even SEED N LOW HIGH chooses a seeded even M in [LOW, HIGH]."""

import random
import sys


def main():
    mode = sys.argv[1]
    seed, n, low, high = map(int, sys.argv[2:])
    if mode != "even" or not (2 <= n <= 5 and 2 <= low <= high <= 10**9):
        raise ValueError("expected: even SEED N LOW HIGH with valid board bounds")
    first = low + low % 2
    if first > high:
        raise ValueError("the interval must contain an even length")
    rng = random.Random(seed)
    m = first + 2 * rng.randrange((high - first) // 2 + 1)
    print(n, m)


if __name__ == "__main__":
    main()
