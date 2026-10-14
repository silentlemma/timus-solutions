"""One test from a seed and a mode: an even grid whose kinds of statues
each come in multiples of four. Mode 1 is 20 by 20 with all 26 letters,
mode 2 a symmetric grid with a few statues swapped, mode 3 few kinds,
mode 4 a small grid."""

import random
import string
import sys

SIDE = 20


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        n, m = rng.choice([2, 4, 6]), rng.choice([2, 4, 6])
    else:
        n, m = SIDE, SIDE
    groups = n * m // 4
    kinds = string.ascii_lowercase[: 3 if mode == 3 else rng.randint(1, 26)]
    labels = [rng.choice(kinds) for _ in range(groups)]
    grid = [[""] * m for _ in range(n)]
    k = 0
    for i in range(n // 2):
        for j in range(m // 2):
            for a, b in ((i, j), (i, m - 1 - j), (n - 1 - i, j), (n - 1 - i, m - 1 - j)):
                grid[a][b] = labels[k]
            k += 1
    cells = [(i, j) for i in range(n) for j in range(m)]
    if mode == 2:
        for _ in range(rng.randint(1, 10)):
            (a, b), (c, d) = rng.sample(cells, 2)
            grid[a][b], grid[c][d] = grid[c][d], grid[a][b]
    else:
        flat = [grid[i][j] for i, j in cells]
        rng.shuffle(flat)
        grid = [flat[i * m : (i + 1) * m] for i in range(n)]
    print(n, m)
    for row in grid:
        print("".join(row))


main()
