"""A town and bombs: a seed, N, M, K and a mode. Mode 1 is an open town
with bombs in random cells; mode 2 scatters buildings at random, which
splits the town into parts, and puts bombs in any free cell; mode 3 is a
winding street between walls with alternating gaps, bombs at random
along it. Speeds are drawn between 0.02 and 9.99."""

import random
import sys

DENSE = 0.4


def main():
    seed, n, m, k, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    if mode == 1:
        rows = [["."] * n for _ in range(m)]
    elif mode == 2:
        rows = [["#" if rng.random() < DENSE else "." for _ in range(n)] for _ in range(m)]
    else:
        rows = []
        for r in range(m):
            if r % 2:
                gap = n - 1 if (r // 2) % 2 == 0 else 0
                rows.append(["." if c == gap else "#" for c in range(n)])
            else:
                rows.append(["."] * n)
    cells = [(x, y) for y in range(m) for x in range(n) if rows[y][x] == "."]
    if not cells:
        rows[0][0] = "."
        cells = [(0, 0)]
    speed = rng.randint(2, 999) / 100
    start = rng.choice(cells)
    bombs = [rng.choice(cells) for _ in range(k)]
    lines = ["%d %d %d %.2f" % (n, m, k, speed)] + ["".join(r) for r in rows]
    lines += ["%d %d" % (x + 1, y + 1) for x, y in [start] + bombs]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
