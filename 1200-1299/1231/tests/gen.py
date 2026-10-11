"""Modes:

random SEED LOW HIGH: print one seeded uniformly random k in [LOW, HIGH],
where 1 <= LOW <= HIGH <= 200.
"""

import random
import sys


def main():
    if len(sys.argv) != 5 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED LOW HIGH")
    seed, low, high = map(int, sys.argv[2:])
    if not 1 <= low <= high <= 200:
        raise SystemExit("require 1 <= LOW <= HIGH <= 200")
    k = random.Random(seed).randint(low, high)
    sys.stdout.buffer.write(f"{k}\n".encode("utf-8"))


if __name__ == "__main__":
    main()
