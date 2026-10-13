"""One test from a seed and a mode; both pieces are always connected.
Mode 1 cuts a 1000 x 1000 sheet along a random staircase, mode 2 cuts a
black blob out of its middle, mode 3 is a black comb whose teeth rise
from the bottom, mode 4 is the same comb with a hook on one tooth, mode
5 is a small random cut."""

import random
import sys

LARGEST = 1000
SMALL = 7


def connected(grid, n, colour):
    cells = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == colour]
    if not cells:
        return False
    seen, stack = {cells[0]}, [cells[0]]
    while stack:
        i, j = stack.pop()
        for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= a < n and 0 <= b < n and grid[a][b] == colour and (a, b) not in seen:
                seen.add((a, b))
                stack.append((a, b))
    return len(seen) == len(cells)


def small(rng):
    while True:
        n = rng.randint(3, SMALL)
        grid = [["0"] * n for _ in range(n)]
        start = (rng.randrange(n), rng.randrange(n))
        grid[start[0]][start[1]] = "1"
        grown = [start]
        for _ in range(rng.randint(0, n * n - 2)):
            i, j = rng.choice(grown)
            a, b = rng.choice(((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))
            if 0 <= a < n and 0 <= b < n and grid[a][b] == "0":
                grid[a][b] = "1"
                grown.append((a, b))
        if connected(grid, n, "0") and connected(grid, n, "1"):
            return grid


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = LARGEST
    if mode == 5:
        grid = small(rng)
    elif mode == 1:
        # white keeps a staircase of row prefixes that shrink downwards
        width = n - 1
        grid = []
        for _ in range(n):
            width = max(0, width - rng.randint(0, 2))
            grid.append(["0"] * width + ["1"] * (n - width))
        grid[0][0] = "0"
    elif mode == 2:
        grid = [["0"] * n for _ in range(n)]
        for i in range(n // 4, 3 * n // 4):
            for j in range(n // 4, 3 * n // 4):
                grid[i][j] = "1"
    else:
        # a black bar along the bottom with teeth rising every 4 columns
        grid = [["0"] * n for _ in range(n)]
        for j in range(n):
            grid[n - 1][j] = "1"
        for j in range(1, n - 1, 4):
            top = rng.randint(n // 2, n - 2)
            for i in range(top, n - 1):
                grid[i][j] = "1"
            if mode == 4 and j == 1:
                grid[top][j + 1] = "1"  # a hook: the comb cannot slide down
    print(n if mode != 5 else len(grid))
    print("\n".join("".join(row) for row in grid))


main()
