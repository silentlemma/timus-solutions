"""One test from a seed and a mode: the accuracies 1, b and c with b != c.
Mode 1 uses three decimals, mode 2 one decimal, mode 3 six decimals near
each other."""

import random
import sys

DIGITS = {1: 3, 2: 1, 3: 6}


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    digits = DIGITS[mode]
    while True:
        b = round(rng.random(), digits)
        c = (
            round(b + rng.uniform(-0.01, 0.01), digits)
            if mode == 3
            else round(rng.random(), digits)
        )
        if b != c and 0 <= c <= 1:
            break
    print("1.0 %.*f %.*f" % (digits, b, digits, c))


main()
