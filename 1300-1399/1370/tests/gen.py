"""Deterministic wheel inputs: random SEED N M.

Mode random prints N independent uniform digits (0..9), with M clicks.
N must be in 11..1000 and M in 0..32767.
"""

import random
import sys


def main():
    if len(sys.argv) != 5 or sys.argv[1] != "random":
        raise ValueError("usage: gen.py random SEED N M")
    seed, n, clicks = map(int, sys.argv[2:])
    if not 11 <= n <= 1000 or not 0 <= clicks <= 32767:
        raise ValueError("N must be in 11..1000 and M in 0..32767")
    rng = random.Random(seed)
    print(n, clicks)
    for _ in range(n):
        print(rng.randrange(10))


if __name__ == "__main__":
    main()
