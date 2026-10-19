"""One input: random SEED LOW HIGH draws k uniformly from [LOW, HIGH]."""

import random
import sys


def main():
    if len(sys.argv) != 5 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED LOW HIGH")
    seed, low, high = map(int, sys.argv[2:])
    if not 1 <= low <= high <= 5000:
        raise SystemExit("require 1 <= LOW <= HIGH <= 5000")
    sys.stdout.buffer.write(f"{random.Random(seed).randint(low, high)}\n".encode("ascii"))


if __name__ == "__main__":
    main()
