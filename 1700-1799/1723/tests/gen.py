"""One test from a seed and a mode: mode 1 a random word of up to 50
letters over a few letters, mode 2 50 letters over the whole alphabet,
mode 3 one letter repeated."""

import random
import string
import sys

LONGEST = 50
FEW = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        letters = string.ascii_lowercase[:FEW]
        size = rng.randint(1, LONGEST)
    else:
        letters = string.ascii_lowercase
        size = LONGEST
    if mode == 3:
        letters = rng.choice(letters)
    print("".join(rng.choice(letters) for _ in range(size)))


main()
