"""A first layer: a seed, N, M and a number of flips. The bricks start all
lying flat; every flip picks a random 2 x 2 square covered by two parallel
bricks and turns them by a right angle, so the bricks soon cross the
borders of the aligned 2 x 2 blocks in every way. The brick numbers are
shuffled."""

import random
import sys


def main():
    seed, n, m, flips = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    grid = [[i * (m // 2) + j // 2 for j in range(m)] for i in range(n)]
    for _ in range(flips):
        i, j = rng.randrange(n - 1), rng.randrange(m - 1)
        a, b = grid[i][j], grid[i][j + 1]
        c, d = grid[i + 1][j], grid[i + 1][j + 1]
        if a == b and c == d:
            grid[i][j] = grid[i + 1][j] = a
            grid[i][j + 1] = grid[i + 1][j + 1] = c
        elif a == c and b == d:
            grid[i][j] = grid[i][j + 1] = a
            grid[i + 1][j] = grid[i + 1][j + 1] = b
    labels = list(range(1, n * m // 2 + 1))
    rng.shuffle(labels)
    lines = ["%d %d" % (n, m)] + [" ".join(str(labels[v]) for v in row) for row in grid]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
