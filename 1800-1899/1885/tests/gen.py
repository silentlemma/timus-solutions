"""Flight limits from a seed and a mode: mode 1 any valid limits, 2 a
climb at x reaches h in time, 3 it does not, 4 h = t v, the plane must
climb at full speed."""

import random
import sys

LOW_H, HIGH_H = 5000, 12000
LOW_T, HIGH_T = 50, 1200
FAST = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        h = rng.randint(LOW_H, HIGH_H)
        t = rng.randint(LOW_T, HIGH_T)
        x = rng.randint(1, FAST - 1)
        v = rng.randint(x + 1, FAST)
        if mode == 4:
            if h % t or not x < h // t <= FAST:
                continue
            v = h // t
            if x >= v:
                continue
        if h > t * v:
            continue
        if mode == 2 and h > t * x or mode == 3 and h <= t * x:
            continue
        break
    print(h, t, v, x)


main()
