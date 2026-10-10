"""The sum 1 + 2 + ... + N for an N of a given number of digits: a seed,
the number of digits and a mode. Mode 0 draws N at random, mode 1 takes
the largest N with that many digits, mode 2 a power of ten."""

import random
import sys

BASE = 10


def main():
    seed, digits, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        n = BASE**digits - 1
    elif mode == 2:
        n = BASE ** (digits - 1)
    else:
        n = rng.randrange(BASE ** (digits - 1), BASE**digits)
    sys.stdout.write("%d\n" % (n * (n + 1) // 2))


if __name__ == "__main__":
    main()
