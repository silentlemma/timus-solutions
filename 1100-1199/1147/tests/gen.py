"""Rectangles on a sheet: a seed, A, B, N, the number of colours and a
mode. Mode 0 places random rectangles, mode 1 thin strips across the whole
sheet, mode 2 nested rectangles shrinking towards the middle, mode 3 many
small squares on distinct coordinates."""

import random
import sys


def main():
    seed, a, b, n, colours, mode = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    rects = []
    for k in range(n):
        if mode == 1:
            if k % 2:
                x1, x2 = sorted(rng.sample(range(a + 1), 2))
                y1, y2 = 0, b
            else:
                y1, y2 = sorted(rng.sample(range(b + 1), 2))
                x1, x2 = 0, a
        elif mode == 2:
            dx, dy = a * k // (2 * n), b * k // (2 * n)
            x1, y1, x2, y2 = dx, dy, a - dx, b - dy
        elif mode == 3:
            x1, y1 = rng.randrange(a), rng.randrange(b)
            x2, y2 = min(a, x1 + rng.randint(1, 3)), min(b, y1 + rng.randint(1, 3))
        else:
            x1, x2 = sorted(rng.sample(range(a + 1), 2))
            y1, y2 = sorted(rng.sample(range(b + 1), 2))
        rects.append("%d %d %d %d %d" % (x1, y1, x2, y2, rng.randint(1, colours)))
    sys.stdout.write("%d %d %d\n%s\n" % (a, b, n, "\n".join(rects)))


if __name__ == "__main__":
    main()
