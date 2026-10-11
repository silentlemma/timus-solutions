"""Modes:
SEED LINES LONGEST: random printable text with line lengths from 0 to LONGEST.
fullwords SEED LINES WIDTH: random Latin words filling every line to WIDTH.
"""

import random
import string
import sys

SYMBOLS = string.ascii_letters * 4 + string.digits + string.punctuation + " " * 10


def main():
    if sys.argv[1] == "fullwords":
        seed, lines, width = map(int, sys.argv[2:])
        if not 1 <= lines <= 1000 or not 1 <= width <= 255:
            raise SystemExit("fullwords requires 1..1000 lines and width 1..255")
        rng = random.Random(seed)
        out = [
            "".join(rng.choice(string.ascii_letters) for _ in range(width)) for _ in range(lines)
        ]
        sys.stdout.buffer.write(("\n".join(out) + "\n").encode("ascii"))
        return

    seed, lines, longest = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    out = [
        "".join(rng.choice(SYMBOLS) for _ in range(rng.randint(0, longest))) for _ in range(lines)
    ]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
