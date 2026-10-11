"""Paintings: a seed, the number of tests, N and a mode. Mode 1 paints
cells at random, mode 2 plants figures of random sizes and then flips a
few cells, mode 3 plants one figure as large as the sheet allows, mode 4
gives all-white and all-black sheets. Mode 5 plants an inset figure on
random surroundings: sheet 0 is intact, and subsequent sheets flip each
cell of the figure in row-major order, cycling if necessary (N >= 5)."""

import random
import sys


def plant(grid, ci, cj, r):
    for i in range(ci - r, ci + r + 1):
        for j in range(cj - r, cj + r + 1):
            grid[i][j] = 0 if abs(i - ci) + abs(j - cj) <= r else 1


def main():
    seed, tests, n, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = []
    for t in range(tests):
        grid = [[rng.randint(0, 1) for _ in range(n)] for _ in range(n)]
        if mode == 2:
            for _ in range(rng.randint(1, 5)):
                r = rng.randint(1, max(1, (n - 1) // 2))
                if 2 * r + 1 <= n:
                    plant(grid, rng.randint(r, n - 1 - r), rng.randint(r, n - 1 - r), r)
            for _ in range(rng.randint(0, n)):
                grid[rng.randrange(n)][rng.randrange(n)] ^= 1
        elif mode == 3 and n >= 3:
            r = (n - 1) // 2
            plant(grid, r, r, r)
            if t % 2:
                grid[rng.randrange(n)][rng.randrange(n)] ^= 1
        elif mode == 4:
            grid = [[t % 2] * n for _ in range(n)]
        elif mode == 5:
            if n < 5:
                raise ValueError("mode 5 needs N >= 5")
            r = (n - 3) // 2
            side = 2 * r + 1
            plant(grid, r + 1, r + 1, r)
            if t:
                i, j = divmod((t - 1) % (side * side), side)
                grid[i + 1][j + 1] ^= 1
        lines.append(str(n))
        lines += [" ".join(map(str, row)) for row in grid]
    lines.append("0")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
