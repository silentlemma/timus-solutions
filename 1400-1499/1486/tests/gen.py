"""One test from a seed and a mode, 500 x 500 unless said otherwise.
Mode 1 uses all 26 letters, mode 2 only two, mode 3 plants a copy of a
large square on random letters, mode 4 is one letter everywhere, mode 5
is one row or one column, mode 6 is a small random matrix."""

import random
import sys

LARGEST = 500
SMALL = 12
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = m = LARGEST
    alphabet = LETTERS
    if mode == 2:
        alphabet = "ab"
    elif mode == 4:
        alphabet = "z"
    elif mode == 5:
        n, m = (1, LARGEST) if rng.random() < 0.5 else (LARGEST, 1)
        alphabet = LETTERS[: rng.randint(2, 4)]
    elif mode == 6:
        n, m = rng.randint(1, SMALL), rng.randint(1, SMALL)
        alphabet = LETTERS[: rng.randint(1, 4)]
    grid = [[rng.choice(alphabet) for _ in range(m)] for _ in range(n)]
    if mode == 3:
        k = rng.randint(LARGEST // 4, LARGEST // 2)
        r1, c1 = rng.randint(0, n - k), rng.randint(0, m - k)
        r2, c2 = rng.randint(0, n - k), rng.randint(0, m - k)
        for t in range(k):
            grid[r2 + t][c2 : c2 + k] = grid[r1 + t][c1 : c1 + k]
    print(n, m)
    print("\n".join("".join(row) for row in grid))


main()
