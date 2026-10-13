"""Modes: random SEED LOW HIGH prints one seeded N in [LOW, HIGH], within 1..21."""

import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    seed, low, high = int(seed), int(low), int(high)
    if mode != "random" or not 1 <= low <= high <= 21:
        raise ValueError("expected: random SEED LOW HIGH, 1 <= LOW <= HIGH <= 21")
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
