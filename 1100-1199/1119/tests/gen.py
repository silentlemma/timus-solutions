"""Random grids: a seed, N, M, K and a mode. Mode 0 scatters diagonal
blocks anywhere, mode 1 puts them near the main diagonal of the grid so
that long chains exist, mode 2 puts them on one row and one column, where
a chain can use only one of a row."""

import random
import sys

SPREAD = 3


def main():
    seed, n, m, k, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    blocks = []
    for _ in range(k):
        if mode == 1:
            t = rng.random()
            x = min(n, max(1, round(t * n) + rng.randint(-SPREAD, SPREAD)))
            y = min(m, max(1, round(t * m) + rng.randint(-SPREAD, SPREAD)))
        elif mode == 2:
            x, y = (rng.randint(1, n), 1) if rng.random() < 0.5 else (1, rng.randint(1, m))
        else:
            x, y = rng.randint(1, n), rng.randint(1, m)
        blocks.append((x, y))
    lines = ["%d %d" % (n, m), str(k)] + ["%d %d" % b for b in blocks]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
