"""Usage: gen.py SEED MODE; modes: fixed (SEED is n), minimum, maximum, random."""

import random
import sys

MIN_SIDE = 1
MAX_SIDE = 256


def generate(seed, mode):
    if mode == "fixed":
        assert MIN_SIDE <= seed <= MAX_SIDE
        return seed
    if mode == "minimum":
        return MIN_SIDE
    if mode == "maximum":
        return MAX_SIDE
    assert mode == "random"
    return random.Random(seed).randint(MIN_SIDE, MAX_SIDE)


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]))
