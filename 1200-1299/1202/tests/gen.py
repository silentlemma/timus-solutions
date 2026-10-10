"""A chain of rectangles: a seed, n and a mode. Mode 1 always leaves a way
through, mode 2 places heights freely so the way may be cut, mode 3 makes
every crossing a single point that zigzags, and mode 4 is mode 1 with the
last crossing closed."""

import random
import sys

SIDE = 100


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    x, rects = 0, []
    low, high = 0, rng.randint(2, SIDE)
    rects.append((0, low, rng.randint(2, SIDE), high))
    x = rects[0][2]
    for i in range(1, n):
        h = rng.randint(2, SIDE)
        if mode == 2:
            y = rng.randint(low - h - 2, high + 2)
        elif mode == 3:
            y = high - 2 if rng.random() < 0.5 else low - h + 2
        elif mode == 4 and i == n - 1:
            y = high
        else:
            y = rng.randint(low - h + 2, high - 2)
        w = rng.randint(2, SIDE)
        rects.append((x, y, x + w, y + h))
        x, low, high = x + w, y, y + h
    lines = [str(n)] + ["%d %d %d %d" % r for r in rects]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
