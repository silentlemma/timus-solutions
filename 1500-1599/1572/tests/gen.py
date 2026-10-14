"""One test from a seed: a well and 100 covers of random shapes and sizes."""

import random
import sys

COVERS = 100
TOP = 100
SHAPES = 3


def main():
    rng = random.Random(int(sys.argv[1]))
    print(rng.randint(1, SHAPES), rng.randint(1, TOP))
    print(COVERS)
    for _ in range(COVERS):
        print(rng.randint(1, SHAPES), rng.randint(1, TOP))


main()
