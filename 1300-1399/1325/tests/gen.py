"""Large flats: a seed and a mode. Mode 1 gives clean and dirty
cells at random with a few walls, mode 2 rows that change kind every
row, mode 3 a spiral corridor with clean and dirty stretches, mode 4 a
clean flat, mode 5 a wall across the middle, mode 6 random blobs of
dirt, mode 7 random cells with the fridge walled in. Mode 8 is a
checkerboard with opposite-kind endpoints, stressing repeated seed
discovery; mode 9 is a random 2 by 500 strip with at least one open
cell per column. The computer and the fridge stand in opposite
corners when they can."""

import random
import sys

N = 500
STRETCH = 37  # length of a clean or dirty stretch in the spiral


def spiral(rng):
    """A corridor two cells wide between walls, winding inwards."""
    grid = [["0"] * N for _ in range(N)]
    top, left, bottom, right = 0, 0, N - 1, N - 1
    path = []
    while top + 1 < bottom and left + 1 < right:
        path += [(top, c) for c in range(left, right + 1)]
        path += [(r, right) for r in range(top + 1, bottom + 1)]
        path += [(bottom, c) for c in range(right - 1, left - 1, -1)]
        path += [(r, left) for r in range(bottom - 1, top + 3, -1)]
        path += [(top + 4, c) for c in range(left + 1, left + 4)]
        top, left, bottom, right = top + 4, left + 4, bottom - 4, right - 4
    for i, (r, c) in enumerate(path):
        grid[r][c] = "1" if i // STRETCH % 2 == 0 else "2"
    return grid, path[0], path[-1]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    start, finish = (0, 0), (N - 1, N - 1)
    if mode == 3:
        grid, start, finish = spiral(rng)
    elif mode == 8:
        grid = [[str(1 + (r + c) % 2) for c in range(N)] for r in range(N)]
        finish = (N - 1, N - 2)
    elif mode == 9:
        columns = [
            rng.choice(("10", "01", "11", "12", "21", "22", "20", "02"))
            for _ in range(N)
        ]
        grid = [[column[r] for column in columns] for r in range(2)]
        finish = (1, N - 1)
    elif mode == 6:
        grid = [["1"] * N for _ in range(N)]
        for _ in range(300):
            r0, c0, size = rng.randrange(N), rng.randrange(N), rng.randint(3, 40)
            for r in range(max(0, r0 - size), min(N, r0 + size)):
                for c in range(max(0, c0 - size), min(N, c0 + size)):
                    grid[r][c] = "2"
    else:
        grid = []
        for r in range(N):
            if mode in (1, 7):
                grid.append(rng.choices("012", weights=[1, 10, 10], k=N))
            elif mode == 2:
                grid.append(["1" if r % 2 == 0 else "2"] * N)
            else:
                grid.append(["1"] * N)
        if mode == 5:
            grid[N // 2] = ["0"] * N
        if mode == 7:
            grid[N - 2][N - 2] = grid[N - 2][N - 1] = grid[N - 1][N - 2] = "0"
    for r, c in (start, finish):
        if grid[r][c] == "0":
            grid[r][c] = "1"
    print(len(grid), len(grid[0]))
    print(start[0] + 1, start[1] + 1)
    print(finish[0] + 1, finish[1] + 1)
    for row in grid:
        print("".join(row))


main()
