"""One test from a seed and a mode: the board sides N and M. Mode 1 is the
largest board, mode 2 has an odd number of rows, mode 3 an odd number of
columns, mode 4 a long strip six cells wide, mode 5 random sides,
mode 6 a horizontal strip six cells high, mode 7 random sides from 6 to 31."""

import random
import sys

MOST = 1000
LEAST = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = MOST, MOST
    elif mode == 2:
        n, m = MOST - 1, MOST
    elif mode == 3:
        n, m = MOST, MOST - 3
    elif mode == 4:
        n, m = MOST, LEAST
    elif mode == 6:
        n, m = LEAST, MOST
    elif mode == 7:
        n, m = rng.randint(LEAST, 31), rng.randint(LEAST, 31)
    else:
        n, m = rng.randint(LEAST, MOST), rng.randint(LEAST, MOST)
    print(n, m)


main()
