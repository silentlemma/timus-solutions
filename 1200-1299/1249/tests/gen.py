"""An image: a seed, N, M and a mode. Mode 1 cuts the image into bands of
rows and columns with blank lines between them and fills most cells of
the grid with a dark rectangle; mode 2 does the same and then darkens one
cell beside a rectangle, which makes an L; mode 3 is a checkerboard; mode
4 is all dark; mode 5 is random noise."""

import random
import sys

FILL = 0.7
BAND = 12


def bands(rng, size):
    """Runs [start, end) separated by single blank lines."""
    out, k = [], 0
    while k < size:
        end = min(size, k + rng.randint(1, BAND))
        out.append((k, end))
        k = end + 1
    return out


def main():
    seed, n, m, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    grid = [bytearray(b"0" * m) for _ in range(n)]
    if mode in (1, 2):
        rows, cols = bands(rng, n), bands(rng, m)
        boxes = []
        for r0, r1 in rows:
            for c0, c1 in cols:
                if rng.random() < FILL:
                    for i in range(r0, r1):
                        grid[i][c0:c1] = b"1" * (c1 - c0)
                    boxes.append((r0, r1, c0, c1))
        if mode == 2:
            fits = [b for b in boxes if b[1] < n and b[3] - b[2] >= 2]
            r0, r1, c0, c1 = rng.choice(fits)
            grid[r1][c0] = ord("1")
    elif mode == 3:
        for i in range(n):
            grid[i] = bytearray(b"01" * (m // 2 + 1))[i % 2 : i % 2 + m]
    elif mode == 4:
        grid = [bytearray(b"1" * m) for _ in range(n)]
    else:
        grid = [bytearray(rng.choice(b"01") for _ in range(m)) for _ in range(n)]
    out = sys.stdout
    out.write("%d %d\n" % (n, m))
    for row in grid:
        out.write(" ".join(row.decode()) + "\n")


if __name__ == "__main__":
    main()
