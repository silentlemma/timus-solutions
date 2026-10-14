"""One test from a seed: random bag sizes and a recipe of one to three
different colors in random order."""

import random
import sys

TOP = 100
COLORS = ["Blue", "Red", "Yellow"]


def main():
    rng = random.Random(int(sys.argv[1]))
    print(*(rng.randint(1, TOP) for _ in COLORS))
    recipe = rng.sample(COLORS, rng.randint(1, len(COLORS)))
    print(len(recipe))
    print("\n".join(recipe))


main()
