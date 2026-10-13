"""Strokes: a seed and a mode. Mode 1 gives 100 000 random strokes, mode 2
100 000 strokes near the origin, mode 3 strokes of odd length whose
corners fall on half units."""

import random
import sys

COUNT = 100000
TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    for _ in range(COUNT):
        if mode == 1:
            a = [rng.randint(-TOP, TOP) for _ in range(4)]
        elif mode == 2:
            a = [rng.randint(-3, 3) for _ in range(4)]
        else:
            x, y = rng.randint(-TOP, TOP - 1), rng.randint(-TOP, TOP - 1)
            a = [x, y, x + 1, y] if rng.random() < 0.5 else [x, y, x, y + 1]
        lines.append(" ".join(map(str, a)))
    print("\n".join(lines))


main()
