"""One test from a seed and a mode: mode 1 a number of monsters right at
or right below the edge of a word's range, mode 2 any number from 1 to
2000."""

import random
import sys

EDGES = [5, 10, 20, 50, 100, 250, 500, 1000]
LIMIT = 2000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.choice(EDGES) - rng.randint(0, 1))
    else:
        print(rng.randint(1, LIMIT))


main()
