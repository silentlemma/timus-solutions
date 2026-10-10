"""A maze whose free cells form a tree: a seed, the width n, the height m
and a mode. Mode 0 grows a random tree cell by cell, mode 1 carves a
perfect maze on the odd cells by a random depth-first walk, mode 2 lays a
single snake through the whole grid, mode 3 a comb of long teeth."""

import random
import sys

STEPS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def grow(rng, n, m):
    grid = [["#"] * n for _ in range(m)]
    r, c = rng.randrange(m), rng.randrange(n)
    grid[r][c] = "."
    frontier = [(r, c)]
    while frontier:
        k = rng.randrange(len(frontier))
        r, c = frontier[k]
        options = []
        for dr, dc in STEPS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "#":
                touching = sum(
                    1
                    for er, ec in STEPS
                    if 0 <= nr + er < m and 0 <= nc + ec < n and grid[nr + er][nc + ec] == "."
                )
                if touching == 1:
                    options.append((nr, nc))
        if options:
            nr, nc = rng.choice(options)
            grid[nr][nc] = "."
            frontier.append((nr, nc))
        else:
            frontier[k] = frontier[-1]
            frontier.pop()
    return grid


def perfect(rng, n, m):
    grid = [["#"] * n for _ in range(m)]
    grid[1][1] = "."
    stack = [(1, 1)]
    while stack:
        r, c = stack[-1]
        options = [
            (r + 2 * dr, c + 2 * dc, r + dr, c + dc)
            for dr, dc in STEPS
            if 0 < r + 2 * dr < m - 1
            and 0 < c + 2 * dc < n - 1
            and grid[r + 2 * dr][c + 2 * dc] == "#"
        ]
        if not options:
            stack.pop()
            continue
        nr, nc, wr, wc = rng.choice(options)
        grid[wr][wc] = grid[nr][nc] = "."
        stack.append((nr, nc))
    return grid


def snake(n, m):
    grid = [["#"] * n for _ in range(m)]
    for r in range(0, m, 2):
        for c in range(n):
            grid[r][c] = "."
        if r + 1 < m:
            grid[r + 1][n - 1 if r % 4 == 0 else 0] = "."
    return grid


def comb(n, m):
    grid = [["#"] * n for _ in range(m)]
    for c in range(n):
        grid[0][c] = "."
    for c in range(0, n, 2):
        for r in range(m):
            grid[r][c] = "."
    return grid


def main():
    seed, n, m, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 1:
        grid = perfect(rng, n, m)
    elif mode == 2:
        grid = snake(n, m)
    elif mode == 3:
        grid = comb(n, m)
    else:
        grid = grow(rng, n, m)
    lines = ["%d %d" % (n, m)] + ["".join(row) for row in grid]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
