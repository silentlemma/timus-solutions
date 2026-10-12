"""Generate one integer n. Mode: random SEED LOW HIGH chooses uniformly
from the inclusive interval [LOW, HIGH], within 1 through 10^9.
"""

import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    seed, low, high = int(seed), int(low), int(high)
    if mode != "random" or not 1 <= low <= high <= 10**9:
        raise ValueError("expected random SEED LOW HIGH with 1 <= LOW <= HIGH <= 10^9")
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
