"""Generate one length: gen.py random SEED LOW HIGH.

Modes:
  random: draw n uniformly from the inclusive interval [LOW, HIGH],
          where 1 <= LOW <= HIGH <= 61, using the supplied seed.
"""

import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    seed, low, high = int(seed), int(low), int(high)
    if mode != "random" or not 1 <= low <= high <= 61:
        raise ValueError("expected random SEED LOW HIGH with 1 <= LOW <= HIGH <= 61")
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
