"""Segments: a seed and a mode. Mode 1 gives a few short segments on a
small M, mode 2 99999 random segments with M = 5000, mode 3 unit
segments that need 5000 pieces, mode 4 many segments with one gap
inside [0, M], mode 5 long segments that mostly stick out of [0, M]."""

import random
import sys

COUNT = 99999
LIMIT = 50000
TOP = 5000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    segments = []
    if mode == 1:
        m = rng.randint(1, 20)
        for _ in range(rng.randint(1, 12)):
            left = rng.randint(-5, m)
            segments.append((left, left + rng.randint(1, 8)))
    elif mode == 2:
        m = TOP
        for _ in range(COUNT):
            left = rng.randint(-LIMIT, LIMIT - 1)
            segments.append((left, min(LIMIT, left + rng.randint(1, 300))))
    elif mode == 3:
        m = TOP
        segments = [(x, x + 1) for x in range(m)]
        segments += [(x, x + 1) for x in rng.sample(range(m), m // 2)]
    elif mode == 4:
        m = TOP
        gap = rng.randint(1, m - 1)
        while len(segments) < COUNT // 2:
            left = rng.randint(-LIMIT, LIMIT - 1)
            right = min(LIMIT, left + rng.randint(1, 200))
            if right <= gap or left >= gap + 1:
                segments.append((left, right))
    else:
        m = TOP
        for _ in range(rng.randint(1, 1000)):
            left = rng.randint(-LIMIT, LIMIT - 1)
            segments.append((left, rng.randint(left + 1, LIMIT)))
    rng.shuffle(segments)
    print(m)
    for left, right in segments:
        print(left, right)
    print(0, 0)


main()
