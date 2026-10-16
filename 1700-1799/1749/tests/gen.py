"""One test from a seed and a mode: mode 1 a short number repeated a few
times, mode 2 a number of 100000 digits repeated up to 10^9 times, mode
3 a 1 followed by zeros, mode 4 a random modulus that is a power of 10."""

import random
import sys

DIGITS = 100000
LIMIT = 10 ** 9
SHORT = 9
FEW = 10
POWERS = 9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        p = str(rng.randint(1, 10 ** rng.randint(1, SHORT)))
        k = rng.randint(1, FEW)
    elif mode == 3:
        p = "1" + "0" * (DIGITS - 1)
        k = rng.randint(1, LIMIT)
    else:
        p = str(rng.randint(1, 9)) + "".join(rng.choice("0123456789") for _ in range(DIGITS - 1))
        k = rng.randint(1, LIMIT)
    m = 10 ** rng.randint(0, POWERS) if mode == 4 else rng.randint(1, LIMIT)
    print(p)
    print(k, m)


main()
