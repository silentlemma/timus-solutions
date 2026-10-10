"""Deterministic pile inputs.

random SEED DIGITS: uniformly sampled positive decimal pile of 1..250 digits.
"""

import random
import sys


def main():
    if len(sys.argv) != 4 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED DIGITS")
    seed, digits = map(int, sys.argv[2:])
    if not 1 <= digits <= 250:
        raise SystemExit("DIGITS must be between 1 and 250")
    rng = random.Random(seed)
    pile = str(rng.randint(1, 9))
    pile += "".join(str(rng.randrange(10)) for _ in range(digits - 1))
    print(pile)


if __name__ == "__main__":
    main()
