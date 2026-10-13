"""Modes: random SEED LOW HIGH chooses N in [LOW, HIGH], then a legal M."""

import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    seed, low, high = int(seed), int(low), int(high)
    if mode != "random" or not 1 <= low <= high <= 256:
        raise ValueError("expected: random SEED LOW HIGH, 1 <= LOW <= HIGH <= 256")
    rng = random.Random(seed)
    n = rng.randint(low, high)
    m = rng.randint(1, min(n, 20))
    sys.stdout.reconfigure(newline="\n")
    print(n, m)


if __name__ == "__main__":
    main()
