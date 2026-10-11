"""A map: a seed, W, H and a mode. Mode 1 is random noise; mode 2 nests
square rings of land and sea around the middle, with small islands in
some of the seas; mode 3 scatters small rectangular islands in an open
sea. The drowning point is a random sea cell."""

import random
import sys

NOISE = 0.45
SPACE = 5


def main():
    seed, w, h, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    g = [["." for _ in range(w)] for _ in range(h)]
    if mode == 1:
        g = [["#" if rng.random() < NOISE else "." for _ in range(w)] for _ in range(h)]
    elif mode == 2:
        for d in range(1, min(w, h) // 2):
            ring = "#" if d % 2 else "."
            for x in range(d, w - d):
                g[d][x] = g[h - 1 - d][x] = ring
            for y in range(d, h - d):
                g[y][d] = g[y][w - 1 - d] = ring
        for _ in range(w * h // (SPACE * SPACE)):
            y, x = rng.randrange(h), rng.randrange(w)
            if g[y][x] == "." and all(
                g[y + dy][x + dx] == "."
                for dy in (-1, 0, 1)
                for dx in (-1, 0, 1)
                if 0 <= y + dy < h and 0 <= x + dx < w
            ):
                g[y][x] = "#"
    else:
        for _ in range(w * h // (SPACE * SPACE)):
            y0, x0 = rng.randrange(h), rng.randrange(w)
            y1, x1 = min(h, y0 + rng.randint(1, SPACE)), min(w, x0 + rng.randint(1, SPACE))
            for y in range(y0, y1):
                for x in range(x0, x1):
                    g[y][x] = "#"
    seas = [(x, y) for y in range(h) for x in range(w) if g[y][x] == "."]
    if not seas:
        g[0][0] = "."
        seas = [(0, 0)]
    x, y = rng.choice(seas)
    lines = ["%d %d %d %d" % (w, h, x + 1, y + 1)] + ["".join(row) for row in g]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
