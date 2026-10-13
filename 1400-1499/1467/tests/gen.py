"""Generate an exponent: random SEED.

random draws k uniformly from the complete allowed range 0 through 30.
"""

import random
import sys


def main():
    sys.stdout.reconfigure(newline="\n")
    mode, seed = sys.argv[1:]
    if mode != "random":
        raise ValueError("expected: random SEED")
    print(random.Random(int(seed)).randint(0, 30))


if __name__ == "__main__":
    main()
