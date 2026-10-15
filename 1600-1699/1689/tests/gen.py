"""One test from a seed and a mode: mode 1 a short trough, mode 2 the
largest sizes with short worms, mode 3 the largest sizes with long worms
and a wide barbell, mode 4 worms packed end to end, mode 5 plates wider
than the gap between them, mode 6 a maximal trough whose only empty
two-unit gap is at the right end, mode 7 random slack gaps between 2000
worms with plates separated by less than one worm length."""

import random
import sys

LONGEST = 100000


def worms(rng, g, w, n):
    """At most n worms of length w that do not overlap (they may touch)."""
    starts = sorted(rng.sample(range(0, g - w + 1), min(n, g - w + 1)))
    out, end = [], -1
    for x in starts:
        if x >= end:
            out.append(x)
            end = x + w
    rng.shuffle(out)
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        g, w, b, p = LONGEST, 1, 2, 1
        xs = list(range(g - 2))
        rng.shuffle(xs)
        print(g, w)
        print(b, p)
        print(len(xs))
        print(*xs)
        return
    if mode == 7:
        g, w, b, p, n = LONGEST, 37, 60001, 29990, 2000
        slack = sorted(rng.randint(0, g - n * w) for _ in range(n))
        xs = [i * w + gap for i, gap in enumerate(slack)]
        rng.shuffle(xs)
        print(g, w)
        print(b, p)
        print(len(xs))
        print(*xs)
        return
    if mode == 1:
        g = rng.randint(2, 30)
        w = rng.randint(1, g)
        b = rng.randint(2, g)
        n = rng.randint(1, 10)
    elif mode == 4:
        g, w = LONGEST, rng.randint(1, 5)
        b = rng.randint(2, 1000)
        n = g // w
    else:
        g = LONGEST
        w = rng.randint(1, 3) if mode == 2 else rng.randint(1, 1000)
        b = rng.randint(2, 200) if mode == 2 else rng.randint(1000, LONGEST)
        n = LONGEST
    p = rng.randint(1, b // 2)
    if mode == 5:
        p = b // 2
    if mode == 4:
        xs = [i * w for i in range(g // w)]
        rng.shuffle(xs)
        xs = xs[:LONGEST]
    else:
        xs = worms(rng, g, w, n)
    print(g, w)
    print(b, p)
    print(len(xs))
    print(*xs)


main()
