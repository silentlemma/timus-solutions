"""A board with ships: a seed, N, M, the number of ships, K and a mode. Mode
1 scatters the ships anywhere, mode 2 presses them against the edges of
the board, mode 3 lines them up in one band of rows."""

import random
import sys

TRIES = 10000


def cells(col, row, size, way):
    if way == "V":
        return [(row + i, col) for i in range(size)]
    return [(row, col + i) for i in range(size)]


def main():
    seed, n, m, count, k, mode = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    ships, taken = [], set()
    for _ in range(TRIES):
        if len(ships) == count:
            break
        size, way = rng.randint(1, 4), rng.choice("VH")
        height, width = (size, 1) if way == "V" else (1, size)
        if height > n or width > m:
            continue
        if mode == 2:
            row = rng.choice([1, n - height + 1])
            col = rng.randint(1, m - width + 1)
            if rng.random() < 0.5:
                row, col = rng.randint(1, n - height + 1), rng.choice([1, m - width + 1])
        elif mode == 3:
            row = rng.randint(1, min(n, 5) - height + 1) if n >= height else 1
            col = rng.randint(1, m - width + 1)
        else:
            row, col = rng.randint(1, n - height + 1), rng.randint(1, m - width + 1)
        body = cells(col, row, size, way)
        near = {(r + dr, c + dc) for r, c in body for dr in (-1, 0, 1) for dc in (-1, 0, 1)}
        if near & taken:
            continue
        taken |= set(body)
        ships.append("%d %d %d %s" % (col, row, size, way))
    lines = ["%d %d %d" % (n, m, len(ships))] + ships + [str(k)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
