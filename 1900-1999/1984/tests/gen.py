"""Usage: gen.py SEED MODE; modes: minimum, maximum, random."""

import random
import sys

MINIMUM = 1
MAXIMUM = 10


def generate(seed, mode):
    if mode == "minimum":
        return MINIMUM
    if mode == "maximum":
        return MAXIMUM
    assert mode == "random"
    return random.Random(seed).randint(MINIMUM, MAXIMUM)


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]))
