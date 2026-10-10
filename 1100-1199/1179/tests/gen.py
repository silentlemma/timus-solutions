"""A text of digits, capital letters, spaces and line breaks: a seed, its
length, the number of different digit values used (from 0 up) and the
chance of a separator in percent."""

import random
import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PERCENT = 100
WIDTH = 80


def main():
    seed, size, kinds, gap = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    used = DIGITS[:kinds]
    out = []
    for i in range(size):
        if (i + 1) % WIDTH == 0:
            out.append("\n")
        elif rng.randrange(PERCENT) < gap:
            out.append(" ")
        else:
            out.append(rng.choice(used))
    sys.stdout.write("".join(out) + "\n")


if __name__ == "__main__":
    main()
