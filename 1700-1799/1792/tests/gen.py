"""One test from a seed: any seven bits. Every word of seven bits is a
code word or one change away from exactly one, so all of them are
valid inputs."""

import random
import sys

BITS = 7


def main():
    rng = random.Random(int(sys.argv[1]))
    print(*(rng.randint(0, 1) for _ in range(BITS)))


main()
