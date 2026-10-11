"""A room, a start and an end joined by a real path: a seed and a mode.
The path is a straight segment in the plane of mirrored rooms, from the
start to an integer point; its crossings of the grid lines give the
walls in order. Mode 1 draws small rooms and few hits, mode 2 large
rooms, mode 3 small rooms and close to 1000 hits."""

import random
import sys
from fractions import Fraction

HITS = 1000


def fold(v, size):
    """The coordinate inside the room of a point of the mirrored plane."""
    v %= 2 * size
    return v if v < size else 2 * size - v


def crossings(a, b, size, low, high):
    """Times and walls where the segment from a to b crosses lines k * size."""
    out = []
    if a == b:
        return out
    step = 1 if b > a else -1
    k = a // size + (1 if step > 0 else 0)
    while (k * size - b) * step < 0:
        wall = low if k % 2 == 0 else high
        out.append((Fraction(k * size - a, b - a), wall))
        k += step
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = 1000 if mode == 2 else 30
    while True:
        w, d = rng.randint(2, top), rng.randint(2, top)
        x0, y0 = rng.randint(1, w - 1), rng.randint(1, d - 1)
        span = 6 if mode == 1 else (2 * HITS // 3 if mode == 3 else 60)
        xs, ys = rng.randint(0, span), rng.randint(0, span)
        ex = rng.randint(xs * w, (xs + 1) * w) * rng.choice([-1, 1])
        ey = rng.randint(ys * d, (ys + 1) * d) * rng.choice([-1, 1])
        if ex % w == 0 or ey % d == 0:
            continue
        hits = crossings(x0, ex, w, "L", "R") + crossings(y0, ey, d, "F", "B")
        times = [t for t, _ in hits]
        if len(hits) > HITS or len(set(times)) < len(times):
            continue
        break
    hits.sort()
    seq = "".join(wall for _, wall in hits)
    x1, y1 = fold(ex, w), fold(ey, d)
    sys.stdout.write("%d %d\n%d %d\n%d %d\n%s\n" % (w, d, x0, y0, x1, y1, seq))


if __name__ == "__main__":
    main()
