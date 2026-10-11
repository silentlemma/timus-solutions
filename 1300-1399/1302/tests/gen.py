"""Two cells: a seed and a mode. Mode 1 gives cells up to 10^9, mode 2
two cells in nearby rows, mode 3 cells at the very start and end of rows."""

import random
import sys

TOP = 10**9
ROWS = 31622  # the last full row below 10^9
NEAR = 3


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        m, n = rng.randint(1, TOP), rng.randint(1, TOP)
    elif mode == 2:
        row = rng.randint(1, ROWS - NEAR)
        other = row + rng.randint(0, NEAR)
        m = (row - 1) ** 2 + rng.randint(1, 2 * row - 1)
        n = (other - 1) ** 2 + rng.randint(1, 2 * other - 1)
    else:
        row, other = rng.randint(1, ROWS), rng.randint(1, ROWS)
        m = row * row if rng.random() < 0.5 else (row - 1) ** 2 + 1
        n = other * other if rng.random() < 0.5 else (other - 1) ** 2 + 1
    print(m, n)


main()
