"""Rectangles in the first quadrant that do not overlap: a seed, N, the
side of the grid cell each rectangle lives in, and a mode. Mode 0 gives
random delays, mode 1 delays all above the desert's, mode 2 delays mostly
below it. L is just past the farthest corner."""

import math
import random
import sys

LIMIT = 32000


def main():
    seed, n, cell, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    side = math.isqrt(n - 1) + 1
    spots = rng.sample([(i, j) for i in range(side) for j in range(side)], n)
    c0 = rng.randint(2, LIMIT - 1)
    lines = [str(n)]
    far = 0
    for i, j in spots:
        x1 = 1 + i * cell + rng.randint(0, cell // 2 - 1)
        y1 = 1 + j * cell + rng.randint(0, cell // 2 - 1)
        x2 = x1 + rng.randint(1, cell // 2)
        y2 = y1 + rng.randint(1, cell // 2)
        if mode == 1:
            c = rng.randint(c0 + 1, LIMIT)
        elif mode == 2:
            c = rng.randint(1, c0 - 1) if rng.random() < 0.8 else rng.randint(c0, LIMIT)
        else:
            c = rng.randint(1, LIMIT)
        lines.append("%d %d %d %d %d" % (x1, y1, x2, y2, c))
        far = max(far, math.hypot(x2, y2))
    assert far + 1 < LIMIT, "the rectangles must fit within reach of L"
    lines.append("%d %d" % (c0, min(LIMIT, int(far) + rng.randint(1, 10))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
