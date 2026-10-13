"""Deterministic queen positions: MODE SEED N S.

Mode random: sample each of the N coordinates independently from 1 through S.
"""

import random
import sys


def main():
    mode, seed, n, side = sys.argv[1:]
    seed, n, side = int(seed), int(n), int(side)
    if mode != "random" or not 1 <= n <= 5 or not 2 <= side <= 100:
        raise ValueError("expected random SEED N S, with 1 <= N <= 5 and 2 <= S <= 100")
    rng = random.Random(seed)
    print(n, side)
    print(*(rng.randint(1, side) for _ in range(n)))


main()
