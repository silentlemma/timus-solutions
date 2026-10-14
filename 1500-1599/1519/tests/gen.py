"""One test from a seed and a mode. Holes come in 2 x 2 blocks aligned to
even rows and columns, which keeps the two colours of the board balanced,
so tracks usually exist. Mode 1 is 12 x 12 with a few such blocks, mode 2
has a random even size, mode 3 is 12 x 12 with a single block, mode 4
scatters single holes at random, which mostly leaves no track."""

import random
import sys

LARGEST = 12
BLOCK = 2
FEW = 0.1
SOME = 0.15
LEAST = 4  # the statement promises at least four free cells


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        n = m = LARGEST
        if mode == 2:
            n = BLOCK * rng.randint(1, LARGEST // BLOCK)
            m = BLOCK * rng.randint(1, LARGEST // BLOCK)
        grid = [["."] * m for _ in range(n)]
        if mode == 4:
            for i in range(n):
                for j in range(m):
                    if rng.random() < FEW:
                        grid[i][j] = "*"
        else:
            blocks = [(i, j) for i in range(0, n, BLOCK) for j in range(0, m, BLOCK)]
            if mode == 3:
                chosen = [rng.choice(blocks)]
            else:
                chosen = [b for b in blocks if rng.random() < (FEW if mode == 1 else SOME)]
            for i, j in chosen:
                for di in range(BLOCK):
                    for dj in range(BLOCK):
                        grid[i + di][j + dj] = "*"
        if sum(row.count(".") for row in grid) >= LEAST:
            break
    print(n, m)
    print("\n".join("".join(row) for row in grid))


main()
