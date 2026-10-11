"""N: a seed and a mode. Mode 1 draws up to 2003 random digits, mode 2
only the digits 4, 8 and 9, the ones whose Roman form is not a run of
equal letters."""

import random
import sys

DIGITS = 2003


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    pool = "0123456789" if mode == 1 else "489"
    n = rng.choice("123456789" if mode == 1 else pool)
    n += "".join(rng.choice(pool) for _ in range(rng.randint(0, DIGITS - 1)))
    sys.stdout.write(n + "\n")


if __name__ == "__main__":
    main()
