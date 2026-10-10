"""Random mosaics: a seed, M, N and a mode. Mode 0 shuffles all pieces,
mode 1 starts sorted and swaps pieces only inside many small separate
groups of boxes, mode 2 starts sorted and swaps a few random pairs."""

import random
import sys

GROUP = 3


def main():
    seed, m, n, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    boxes = [[b + 1] * n for b in range(m)]
    if mode == 0:
        pieces = [p for box in boxes for p in box]
        rng.shuffle(pieces)
        boxes = [pieces[b * n : (b + 1) * n] for b in range(m)]
    else:
        swaps = rng.randint(1, m) if mode == 2 else m
        for _ in range(swaps):
            a = rng.randrange(m)
            if mode == 1:
                base = a - a % GROUP
                b = min(m - 1, base + rng.randrange(GROUP))
            else:
                b = rng.randrange(m)
            i, j = rng.randrange(n), rng.randrange(n)
            boxes[a][i], boxes[b][j] = boxes[b][j], boxes[a][i]
    lines = ["%d %d" % (m, n)] + [" ".join(map(str, box)) for box in boxes]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
