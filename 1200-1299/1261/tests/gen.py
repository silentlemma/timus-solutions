"""N: a seed and a mode. Mode 1 draws any N, mode 2 an N whose ternary
digits are only 0 and 1, so that balanced ternary leaves no tip."""

import random
import sys

TOP = 10**7
DIGITS = 15  # 3^15 is above TOP


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = 0
    while not 1 <= n <= TOP:
        if mode == 1:
            n = rng.randint(1, TOP)
        else:
            n = sum(3**k for k in range(DIGITS) if rng.random() < 0.5)
    sys.stdout.write("%d\n" % n)


if __name__ == "__main__":
    main()
