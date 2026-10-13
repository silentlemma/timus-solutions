"""Mode random: random SEED LOW HIGH prints a seeded sum in [LOW, HIGH].

The bounds must satisfy 1 <= LOW <= HIGH <= 81.
"""

import argparse
import random
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["random"])
    parser.add_argument("seed", type=int)
    parser.add_argument("low", type=int)
    parser.add_argument("high", type=int)
    args = parser.parse_args()
    if not 1 <= args.low <= args.high <= 81:
        parser.error("bounds must satisfy 1 <= LOW <= HIGH <= 81")
    target = random.Random(args.seed).randint(args.low, args.high)
    sys.stdout.buffer.write(f"{target}\n".encode("utf-8"))


if __name__ == "__main__":
    main()
