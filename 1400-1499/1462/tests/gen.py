"""Modes: random SEED LOW HIGH chooses N uniformly from [LOW, HIGH]."""

import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    seed, low, high = int(seed), int(low), int(high)
    if mode != "random" or not 3 <= low <= high <= 70000:
        raise ValueError("expected: random SEED LOW HIGH, 3 <= LOW <= HIGH <= 70000")
    rng = random.Random(seed)
    sys.stdout.reconfigure(newline="\n")
    print(rng.randint(low, high))


if __name__ == "__main__":
    main()
