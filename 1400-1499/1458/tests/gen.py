"""Parade grounds: a seed, N and a mode. Mode 1 is random, mode 2 has a
single soldier standing differently, mode 3 is a chessboard, mode 4 is
random with few B, mode 5 has only the last column B, and mode 6 is random
with an even number of B in every row and column."""

import random
import sys

SPARSE = 0.01


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        grid = [[rng.choice("BW") for _ in range(n)] for _ in range(n)]
    elif mode == 2:
        grid = [["W"] * n for _ in range(n)]
        grid[rng.randrange(n)][rng.randrange(n)] = "B"
    elif mode == 3:
        grid = [["BW"[(i + j) % 2] for j in range(n)] for i in range(n)]
    elif mode == 5:
        grid = [["W"] * (n - 1) + ["B"] for _ in range(n)]
    elif mode == 6:
        grid = [["W"] * n for _ in range(n)]
        for i in range(n - 1):
            for j in range(n - 1):
                grid[i][j] = rng.choice("BW")
            grid[i][-1] = "B" if grid[i][:-1].count("B") % 2 else "W"
        for j in range(n):
            grid[-1][j] = "B" if sum(grid[i][j] == "B" for i in range(n - 1)) % 2 else "W"
    else:
        grid = [["B" if rng.random() < SPARSE else "W" for _ in range(n)] for _ in range(n)]
    print(n)
    print("\n".join("".join(row) for row in grid))


main()
