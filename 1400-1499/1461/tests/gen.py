"""Garlands of length N: a seed, N and a mode. Mode 1 is a random garland,
mode 2 the last one in the book (u as long as possible), mode 3 a random
garland that stays low, mode 4 a random garland that climbs high."""

import random
import sys

STEP = {"d": -1, "h": 0, "u": 1}
LOW = 3


def finishes(height, left):
    if height == 0:
        return left == 0 or left >= 2
    return left >= height


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    out, height = [], 0
    for left in range(n, 0, -1):
        options = [
            c
            for c in "dhu"
            if height + STEP[c] >= 0
            and not (c == "h" and height == 0)
            and finishes(height + STEP[c], left - 1)
        ]
        if mode == 2:
            c = options[-1]
        elif mode == 3 and height >= LOW and "u" in options and len(options) > 1:
            c = rng.choice(options[:-1])
        elif mode == 4 and "u" in options and rng.random() < 0.7:
            c = "u"
        else:
            c = rng.choice(options)
        out.append(c)
        height += STEP[c]
    print(n)
    print("".join(out))


main()
