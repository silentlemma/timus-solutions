"""One program from a seed and a mode: mode 1 a few random segments in
a small box, mode 2 the most segments anywhere, mode 3 the most short
segments, mode 4 the most segments with many U-turns, mode 5 long
segments around a square, fast enough to reach the speed limit; mode 6
1000 connected unit steps with a stop at every corner; mode 7 1000
nearly parallel lattice directions with determinant magnitude one."""

import random
import sys

LIMIT = 1000
MOST = 1000
SMALL = 6


def fits(prev, seg):
    # no two neighbours point the same way; opposite neighbours need a gap
    dx1, dy1 = prev[2] - prev[0], prev[3] - prev[1]
    dx2, dy2 = seg[2] - seg[0], seg[3] - seg[1]
    if dx1 * dy2 - dy1 * dx2 != 0:
        return True
    if dx1 * dx2 + dy1 * dy2 > 0:
        return False
    return dx1 * (seg[1] - prev[3]) - dy1 * (seg[0] - prev[2]) != 0


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        x, y = 0, 0
        segs = []
        for i in range(MOST):
            step = rng.choice((-1, 1))
            nx, ny = (x + step, y) if i % 2 == 0 else (x, y + step)
            segs.append((x, y, nx, ny))
            x, y = nx, ny
        print(MOST)
        for seg in segs:
            print(*seg)
        return
    if mode == 7:
        print(MOST)
        for i in range(MOST):
            x, y = rng.randint(-LIMIT, 0), rng.randint(-LIMIT, LIMIT - 1)
            print(x, y, x + LIMIT - i % 2, y + 1)
        return
    n = rng.randint(1, SMALL) if mode == 1 else MOST
    box = {1: 10, 3: 30}.get(mode, LIMIT)
    segs = []
    corners = [(-LIMIT, -LIMIT), (LIMIT, -LIMIT), (LIMIT, LIMIT), (-LIMIT, LIMIT)]
    while len(segs) < n:
        if mode == 5:
            k = len(segs) % 4
            (x1, y1), (x2, y2) = corners[k], corners[(k + 1) % 4]
            pad = rng.randint(0, 50)
            seg = (x1, y1, x2, y2) if k % 2 == 0 else (x1, y1, x2, y2)
            seg = tuple(v - pad if v > 0 else v + pad for v in seg)
        else:
            seg = tuple(rng.randint(-box, box) for _ in range(4))
            if mode == 4 and segs and rng.random() < 0.5:
                px, py = segs[-1][2] - segs[-1][0], segs[-1][3] - segs[-1][1]
                x, y = rng.randint(-box, box), rng.randint(-box, box)
                seg = (x, y, x - px, y - py)
        if seg[:2] == seg[2:] or max(map(abs, seg)) > LIMIT:
            continue
        if segs and not fits(segs[-1], seg):
            continue
        segs.append(seg)
    print(n)
    for s in segs:
        print(*s)


main()
