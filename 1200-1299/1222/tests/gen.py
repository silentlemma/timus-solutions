"""Modes:

random SEED LOW HIGH: one seeded random N in the inclusive range LOW..HIGH;
    requires 1 <= LOW <= HIGH <= 3000.
"""

import random
import sys


def main():
    if len(sys.argv) != 5 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED LOW HIGH")
    seed, low, high = map(int, sys.argv[2:])
    if not 1 <= low <= high <= 3000:
        raise SystemExit("requires 1 <= LOW <= HIGH <= 3000")
    n = random.Random(seed).randint(low, high)
    sys.stdout.buffer.write(f"{n}\n".encode("ascii"))


if __name__ == "__main__":
    main()
