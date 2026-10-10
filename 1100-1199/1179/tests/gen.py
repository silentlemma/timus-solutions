"""Modes:
SEED SIZE KINDS GAP: legacy text with the first KINDS digit values,
spaces with GAP percent probability, and a line break every 80 characters.
high SEED SIZE: exactly SIZE bytes, random Y/Z digits on one line plus LF.
"""

import random
import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PERCENT = 100
WIDTH = 80


def main():
    if sys.argv[1] == "high":
        seed, size = map(int, sys.argv[2:])
        if not 1 <= size <= 1_000_000:
            raise ValueError("size must be between 1 and 1000000 bytes")
        rng = random.Random(seed)
        text = "".join(rng.choice("YZ") for _ in range(size - 1)) + "\n"
        sys.stdout.buffer.write(text.encode("ascii"))
        return
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
