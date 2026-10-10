"""Deterministic digit-length inputs.

random SEED LOW HIGH: choose K uniformly from the inclusive range [LOW, HIGH],
    where 2 <= LOW <= HIGH <= 50.
"""

import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    assert mode == "random"
    seed, low, high = int(seed), int(low), int(high)
    assert 2 <= low <= high <= 50
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
