"""Random squares and a point: a seed, n, the coordinate range and a mode.
Mode 0 draws squares by random diagonals, mode 1 copies a few squares by
the symmetries of the grid around P so that many distances tie, mode 2
mixes in squares shrunk to points and squares that contain P."""

import random
import sys

TOP = 9998


def main():
    seed, n, top, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    top = min(top, TOP)
    px, py = rng.randint(-top // 2, top // 2), rng.randint(-top // 2, top // 2)

    def fits(*vals):
        return all(-TOP <= v <= TOP for v in vals)

    def turns(x, y):
        """The eight images of (x, y) under the symmetries of the grid at P."""
        dx, dy = x - px, y - py
        out = []
        for a, b in ((dx, dy), (-dy, dx), (-dx, -dy), (dy, -dx)):
            out += [(px + a, py + b), (px + b, py + a)]
        return out

    squares = []
    while len(squares) < n:
        x1, y1 = rng.randint(-top, top), rng.randint(-top, top)
        x2, y2 = rng.randint(-top, top), rng.randint(-top, top)
        kind = rng.randrange(3) if mode == 2 else 0
        if kind == 1:
            # a square shrunk to a point
            x2, y2 = x1, y1
        elif kind == 2:
            # a square centred at P, so P is inside
            x2, y2 = 2 * px - x1, 2 * py - y1
        if mode == 1:
            first, second = turns(x1, y1), turns(x2, y2)
            for k in rng.sample(range(len(first)), rng.randint(2, len(first))):
                (a, b), (c, d) = first[k], second[k]
                if fits(a, b, c, d) and len(squares) < n:
                    squares.append((a, b, c, d))
        elif fits(x1, y1, x2, y2):
            squares.append((x1, y1, x2, y2))
    rng.shuffle(squares)
    lines = [str(n)] + ["%d %d %d %d" % s for s in squares] + ["%d %d" % (px, py)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
