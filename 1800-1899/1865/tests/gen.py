"""An island from a seed and a mode: mode 1 small, 2 the largest island
with a small lighthouse, 3 the largest island with a lighthouse that
leaves just enough room, 4 a long thin island, 5 a large island with a
lighthouse of random size and place."""

import random
import sys

MOST = 10 ** 6
SMALL = 12
THIN = 3


def island(rng, mode):
    if mode == 1:
        w, h = rng.randint(THIN, SMALL), rng.randint(THIN, SMALL)
    elif mode == 4:
        w, h = rng.choice([(THIN, MOST), (MOST, THIN), (MOST - 1, 4), (4, MOST - 1)])
    elif mode == 5:
        w, h = rng.randint(THIN, MOST), rng.randint(THIN, MOST)
    else:
        w, h = MOST, MOST
    if w * h % 2:
        h -= 1
    return w, h


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    w, h = island(rng, mode)
    top = min(w, h) - 2
    if mode == 2:
        d = rng.randint(1, SMALL)
    elif mode == 3:
        # d * d + h + w - x - d - 1 close to w * h / 2 with x = 1
        d = int((w * h // 2 - h - w) ** 0.5)
        d = max(1, min(top, d + rng.randint(-1, 1)))
    else:
        d = rng.randint(1, top)
    x = rng.randint(1, w - d - 1)
    y = rng.randint(1, h - d - 1)
    print(w, h)
    print(x, y, d)


main()
