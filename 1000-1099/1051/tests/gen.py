"""Modes:
small SEED: a seeded random rectangle, sides at most 7 and at most 15 stones.
"""

import random
import sys


def main():
    mode, seed = sys.argv[1:]
    if mode != "small":
        raise SystemExit("usage: gen.py small SEED")
    rng = random.Random(int(seed))
    boards = [(m, n) for m in range(1, 8) for n in range(1, 8) if m * n <= 15]
    m, n = rng.choice(boards)
    print(m, n)


if __name__ == "__main__":
    main()
