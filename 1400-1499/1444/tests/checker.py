"""Checker: the same count as the reference, a permutation of the pumpkins
that starts with 1, and a walk that never touches its own tracks: the
polyline must be simple. A sweep line finds any touching pair of segments
in O(N log N); a direct O(N^2) test backs it up for small inputs."""

import sys

SHEAR = 4001  # x' = SHEAR x + y keeps every point apart and no segment vertical
SMALL = 600


def fail(reason):
    print(reason)
    sys.exit(1)


def orient(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (v > 0) - (v < 0)


def on_box(a, b, c):
    inside_x = min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
    return inside_x and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])


def touch(p, q, r, s):
    # closed segments pq and rs share a point
    o1, o2, o3, o4 = orient(p, q, r), orient(p, q, s), orient(r, s, p), orient(r, s, q)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    return (
        (o1 == 0 and on_box(p, q, r))
        or (o2 == 0 and on_box(p, q, s))
        or (o3 == 0 and on_box(r, s, p))
        or (o4 == 0 and on_box(r, s, q))
    )


def simple(pts):
    m = len(pts) - 1
    for i in range(m - 1):
        # neighbours share one end and must not fold back on each other
        a, b, c = pts[i], pts[i + 1], pts[i + 2]
        if (
            orient(a, b, c) == 0
            and (b[0] - a[0]) * (c[0] - b[0]) + (b[1] - a[1]) * (c[1] - b[1]) < 0
        ):
            return False
    sh = [(SHEAR * x + y, y) for x, y in pts]
    seg = [tuple(sorted((sh[i], sh[i + 1]))) for i in range(m)]

    def check(i, j):
        if abs(i - j) == 1:
            return True
        return not touch(seg[i][0], seg[i][1], seg[j][0], seg[j][1])

    def side(i, p):
        # the sign of the height of segment i above point p, at the x of p
        (x1, y1), (x2, y2) = seg[i]
        v = y1 * (x2 - x1) + (y2 - y1) * (p[0] - x1) - p[1] * (x2 - x1)
        return (v > 0) - (v < 0)

    def slope_less(i, j):
        (a1, b1), (a2, b2) = seg[i]
        (c1, d1), (c2, d2) = seg[j]
        return (b2 - b1) * (c2 - c1) < (d2 - d1) * (a2 - a1)

    events = []
    for i in range(m):
        events.append((seg[i][0][0], 0, i))
        events.append((seg[i][1][0], 1, i))
    events.sort()
    line = []
    for _, kind, i in events:
        if kind == 0:
            p = seg[i][0]
            lo, hi = 0, len(line)
            while lo < hi:
                mid = (lo + hi) // 2
                c = side(line[mid], p)
                if c < 0 or (c == 0 and slope_less(line[mid], i)):
                    lo = mid + 1
                else:
                    hi = mid
            line.insert(lo, i)
            for k in (lo - 1, lo + 1):
                if 0 <= k < len(line) and not check(i, line[k]):
                    return False
        else:
            p = seg[i][1]
            lo, hi = 0, len(line)
            while lo < hi:
                mid = (lo + hi) // 2
                if side(line[mid], p) < 0:
                    lo = mid + 1
                else:
                    hi = mid
            k = lo
            while k < len(line) and line[k] != i:
                k += 1
            if k == len(line):
                k = line.index(i)
            line.pop(k)
            if 0 < k < len(line) and not check(line[k - 1], line[k]):
                return False
    return True


def brute(pts):
    m = len(pts) - 1
    for i in range(m):
        for j in range(i + 1, m):
            if j == i + 1:
                a, b, c = pts[i], pts[i + 1], pts[i + 2]
                d = (b[0] - a[0]) * (c[0] - b[0]) + (b[1] - a[1]) * (c[1] - b[1])
                if orient(a, b, c) == 0 and d < 0:
                    return False
            elif touch(pts[i], pts[i + 1], pts[j], pts[j + 1]):
                return False
    return True


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n = data[0]
    pts = list(zip(data[1 : 1 + 2 * n : 2], data[2 : 2 + 2 * n : 2]))
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got:
        fail("empty output")
    k = int(got[0])
    if k != want:
        fail("%d pumpkins, expected %d" % (k, want))
    walk = [int(x) for x in got[1:]]
    if len(walk) != k:
        fail("expected %d numbers" % k)
    if walk[0] != 1 or len(set(walk)) != k or not all(1 <= v <= n for v in walk):
        fail("the walk must start at 1 and visit different pumpkins")
    path = [pts[v - 1] for v in walk]
    if not simple(path):
        fail("the walk touches its own tracks")
    if n <= SMALL and not brute(path):
        fail("the walk touches its own tracks (direct test)")


if __name__ == "__main__":
    main()
