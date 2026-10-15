"""One test from a seed and a mode: mode 1 a small board, mode 2 a large
board, mode 3 a board with a side below 4, mode 4 both sides of the form
4k + 1, mode 5 one side of 4, mode 6 the maximum square, mode 7 the
largest square whose sides are 4k + 1."""

import random
import sys

MOST = 500


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(2, 20), rng.randint(2, 20)
    elif mode == 2:
        n, m = rng.randint(400, MOST), rng.randint(400, MOST)
    elif mode == 3:
        n, m = rng.randint(2, 3), rng.randint(2, MOST)
        if rng.random() < 0.5:
            n, m = m, n
    elif mode == 4:
        n, m = 4 * rng.randint(1, 124) + 1, 4 * rng.randint(1, 124) + 1
    elif mode == 6:
        n, m = MOST, MOST
    elif mode == 7:
        n = m = MOST - 3
    else:
        n, m = 4, rng.randint(2, MOST)
        if rng.random() < 0.5:
            n, m = m, n
    print(n, m)


main()
