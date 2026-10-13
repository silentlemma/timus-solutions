"""Seeded child counts: SEED random LOW HIGH.

Mode random prints one uniformly sampled count in the inclusive range
LOW..HIGH, with 1 <= LOW <= HIGH <= 1000.
"""

import random
import sys


def main():
    seed = int(sys.argv[1])
    mode = sys.argv[2]
    low, high = map(int, sys.argv[3:5])
    if mode != "random" or not 1 <= low <= high <= 1000:
        raise ValueError("expected SEED random LOW HIGH with 1 <= LOW <= HIGH <= 1000")
    sys.stdout.reconfigure(newline="\n")
    sys.stdout.write(str(random.Random(seed).randint(low, high)) + "\n")


if __name__ == "__main__":
    main()
