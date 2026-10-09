"""Deterministic random query modes (at most ten queries).

SEED COUNT: queries from 1..99999 (the original mode).
small SEED COUNT: queries from 1..256, exercising small odd/even recurrences.
"""

import random
import sys

TOP = 99999


def main():
    args = sys.argv[1:]
    small = args[0] == "small"
    if small:
        args = args[1:]
    seed, count = (int(x) for x in args[:2])
    rng = random.Random(seed)
    limit = 256 if small else TOP
    lines = [str(rng.randint(1, limit)) for _ in range(count)] + ["0"]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
