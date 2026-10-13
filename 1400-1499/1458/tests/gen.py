"""Parade grounds: a seed, N and a mode. Mode 1 is random, mode 2 has a
single soldier standing differently, mode 3 is a chessboard, mode 4 is
random with few B."""

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
    else:
        grid = [["B" if rng.random() < SPARSE else "W" for _ in range(n)] for _ in range(n)]
    print(n)
    print("\n".join("".join(row) for row in grid))


main()
