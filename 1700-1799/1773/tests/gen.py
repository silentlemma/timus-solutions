"""One test from a seed and a mode: mode 1 up to 6 strips cut from a line
or drawn at random, mode 2 50 000 strips cut from a sloping line and
shuffled, half of them turned over, mode 3 the same for a flat line,
mode 4 like mode 2 with one strip spoilt, mode 5 a few strips cut from
a steep line, mode 6 50 000 equally steep strips whose total rise
exceeds both the wall height and the signed 32-bit range."""

import random
import sys

FEW = 6
SMALL_H = 10
MOST = 50000
TALL = 100000
STEEP = 1000
HALF = 0.5


def cut(rng, h, n, d):
    low = max(0, -n * d)
    high = min(h, h - n * d)
    y0 = rng.randint(low, high)
    strips = []
    for i in range(n):
        l, r = y0 + i * d, y0 + (i + 1) * d
        if rng.random() < HALF:
            l, r = h - r, h - l
        strips.append((l, r))
    rng.shuffle(strips)
    return strips


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        h, n = rng.randint(1, SMALL_H), rng.randint(1, FEW)
        d = rng.randint(-(h // n), h // n)
        if rng.random() < HALF:
            strips = cut(rng, h, n, d)
        else:
            strips = [(rng.randint(0, h), rng.randint(0, h)) for _ in range(n)]
    elif mode == 5:
        h, n = TALL, rng.randint(2, TALL // STEEP)
        strips = cut(rng, h, n, rng.choice((1, -1)) * rng.randint(1, h // n))
    elif mode == 6:
        h, n = TALL, MOST
        d = rng.choice((1, -1)) * rng.randint(TALL - STEEP, TALL)
        low, high = max(0, -d), min(h, h - d)
        strips = []
        for _ in range(n):
            l = rng.randint(low, high)
            strips.append((l, l + d))
    else:
        h, n = TALL, MOST
        d = 0 if mode == 3 else rng.choice((1, -1)) * rng.randint(1, h // n)
        strips = cut(rng, h, n, d)
        if mode == 4:
            i = rng.randrange(n)
            l, r = strips[i]
            shift = 1 if max(l, r) < h else -1
            strips[i] = (l + shift, r + shift)
    print(h, len(strips))
    for l, r in strips:
        print(l, r)


main()
