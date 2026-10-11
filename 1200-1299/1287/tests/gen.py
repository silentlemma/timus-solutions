"""A field: a seed and a mode. Mode 1 draws random letters on up to 1400
cells a side, mode 2 thin diagonal stripes, mode 3 random blocks of one
letter, mode 4 a field of one letter with a single long line of the
other."""

import random
import sys

SIDE = 1400


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = SIDE if seed % 2 == 0 else rng.randint(1, SIDE)
    if mode == 1:
        rows = ["".join(rng.choice("sS") for _ in range(n)) for _ in range(n)]
    elif mode == 2:
        k = rng.randint(2, 5)
        sign = rng.choice([1, -1])
        rows = ["".join("sS"[((i + sign * j) % k) == 0] for j in range(n)) for i in range(n)]
    elif mode == 3:
        grid = [[rng.choice("sS") for _ in range(n)] for _ in range(n)]
        for _ in range(20):
            c = rng.choice("sS")
            i0, j0 = rng.randrange(n), rng.randrange(n)
            size = rng.randint(1, n)
            for i in range(i0, min(n, i0 + size)):
                for j in range(j0, min(n, j0 + rng.randint(1, size))):
                    grid[i][j] = c
        rows = ["".join(r) for r in grid]
    else:
        grid = [["s"] * n for _ in range(n)]
        length = rng.randint(1, n)
        for k in range(length):
            grid[k][n - 1 - k] = "S"
        rows = ["".join(r) for r in grid]
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(rows)))


if __name__ == "__main__":
    main()
