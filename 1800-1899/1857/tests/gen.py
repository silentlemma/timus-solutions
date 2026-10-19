"""An alphabet size and a key length from a seed and a mode: mode 1 a
short key, 2 a long key, 3 the longest key with a random alphabet."""

import random
import sys

LETTERS = 26
MOST = 10000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    a = rng.randint(1, LETTERS)
    n = {1: rng.randint(1, 30), 2: rng.randint(MOST // 2, MOST)}.get(mode, MOST)
    print(a, n)


main()
