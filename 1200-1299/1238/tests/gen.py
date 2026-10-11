"""A sequence of at most 100 letters: a seed and a mode. Mode 1 draws two
letters at random, mode 2 all 26, and mode 3 unfolds a random folded
sequence with nested repeats, cut to 100 letters."""

import random
import sys

LONGEST = 100
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def nested(rng, depth):
    if depth == 0 or rng.random() < 0.3:
        return "".join(rng.choice("ABC") for _ in range(rng.randint(1, 3)))
    parts = [nested(rng, depth - 1) for _ in range(rng.randint(1, 3))]
    return "".join(p * rng.randint(1, 4) for p in parts)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        text = "".join(rng.choice("AB") for _ in range(LONGEST))
    elif mode == 2:
        text = "".join(rng.choice(LETTERS) for _ in range(LONGEST))
    else:
        text = ""
        while len(text) < LONGEST:
            text += nested(rng, 4)
        text = text[:LONGEST]
    sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
