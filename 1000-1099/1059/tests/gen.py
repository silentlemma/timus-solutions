"""Deterministic degree generator; modes and arguments:

random SEED MIN_N MAX_N: uniformly choose one degree in [MIN_N, MAX_N],
    where 1 <= MIN_N <= MAX_N <= 1000.
"""

import random
import sys


def main():
    if len(sys.argv) != 5 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED MIN_N MAX_N")
    seed, low, high = map(int, sys.argv[2:])
    if not 1 <= low <= high <= 1000:
        raise SystemExit("require 1 <= MIN_N <= MAX_N <= 1000")
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
