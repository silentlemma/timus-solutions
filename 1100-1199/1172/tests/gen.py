"""Modes:
random SEED LOW HIGH: choose N uniformly from the inclusive range [LOW, HIGH].
"""

import random
import sys


def main():
    if len(sys.argv) != 5 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED LOW HIGH")
    seed, low, high = map(int, sys.argv[2:])
    if not 1 <= low <= high <= 30:
        raise SystemExit("require 1 <= LOW <= HIGH <= 30")
    sys.stdout.reconfigure(newline="\n")
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
