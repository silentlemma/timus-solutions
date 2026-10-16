"""One input: random SEED samples three distinct lengths from 1 through 1000."""

import random
import sys


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED")
    seed = int(sys.argv[2])
    h, height, length = sorted(random.Random(seed).sample(range(1, 1001), 3))
    print(h, height, length)


if __name__ == "__main__":
    main()
