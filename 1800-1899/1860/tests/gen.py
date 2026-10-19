"""A number from a seed and a mode: mode 1 a small n, 2 a large n,
3 the largest n, 4 a random n between 51 and 999."""

import random
import sys

MOST = 10 ** 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    choices = {1: rng.randint(1, 50), 2: rng.randint(MOST // 2, MOST)}
    choices[4] = rng.randint(51, 999)
    print(choices.get(mode, MOST))


main()
