"""One test from a seed: random n and m from 2 to 50."""

import random
import sys

LOW, HIGH = 2, 50


def main():
    rng = random.Random(int(sys.argv[1]))
    print(rng.randint(LOW, HIGH), rng.randint(LOW, HIGH))


main()
