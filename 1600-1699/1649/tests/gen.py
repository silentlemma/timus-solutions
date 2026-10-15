"""One test from a seed and a mode: the picture of a random settling order
(mode 1 small, mode 2 20 by 20), of a chessboard order with every inner
cell showing 1 (mode 3), a random picture that is mostly impossible
(mode 4), a settled picture with one cell changed (mode 5), a chessboard
picture with one count raised and another lowered, which keeps the totals
balanced (mode 6), or every inner cell 1 and a random border (mode 7)."""

import random
import sys

SIDE = 20


def picture(n, m, order):
    count = [[0] * m for _ in range(n)]
    settled = [[False] * m for _ in range(n)]
    for r, c in order:
        settled[r][c] = True
        count[r][c] = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and settled[nr][nc]:
                count[nr][nc] = count[nr][nc] % 4 + 1
    return count


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(1, 5), rng.randint(1, 5)
    else:
        n, m = rng.randint(SIDE - 5, SIDE), rng.randint(SIDE - 5, SIDE)
    cells = [(r, c) for r in range(n) for c in range(m)]
    if mode in (3, 6, 7):
        black = [p for p in cells if (p[0] + p[1]) % 2 == 0]
        white = [p for p in cells if (p[0] + p[1]) % 2]
        rng.shuffle(black)
        rng.shuffle(white)
        order = black + white
    else:
        order = cells[:]
        rng.shuffle(order)
    count = picture(n, m, order)
    if mode == 4:
        count = [[rng.randint(1, 4) for _ in range(m)] for _ in range(n)]
    if mode == 5:
        r, c = rng.randrange(n), rng.randrange(m)
        count[r][c] = count[r][c] % 4 + 1
    if mode == 6:
        (r1, c1), (r2, c2) = rng.sample(cells, 2)
        count[r1][c1] = count[r1][c1] % 4 + 1
        count[r2][c2] = (count[r2][c2] + 2) % 4 + 1
    if mode == 7:
        for r, c in cells:
            if 0 < r < n - 1 and 0 < c < m - 1:
                count[r][c] = 1
            else:
                count[r][c] = rng.randint(1, 4)
    print(n, m)
    for row in count:
        print(*row)


main()
