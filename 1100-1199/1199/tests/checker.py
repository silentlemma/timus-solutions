"""Checker: the path starts at the mouse and ends at the cheese, has at most
1000 vertices, every segment is wholly dangerous or wholly safe apart from
a tiny tolerance, and its dangerous length matches the reference's. The
safe part of a segment is found exactly: around each piece of furniture it
is one interval, the hull of where the segment meets the polygon, the
strips along its sides and the discs around its corners."""

import sys
from math import atan2, hypot

# points exactly 10 cm away are safe; the slack absorbs rounding
SAFE = 0.1 + 1e-7
LIMIT = 1000
TOL = 1e-3
END_TOL = 1.5e-4


def fail(reason):
    print(reason)
    sys.exit(1)


def read_input(path):
    data = open(path).read().split()
    mouse = (float(data[0]), float(data[1]))
    cheese = (float(data[2]), float(data[3]))
    n, pos = int(data[4]), 5
    polys = []
    for _ in range(n):
        k = int(data[pos])
        pts = [(float(data[pos + 1 + 2 * j]), float(data[pos + 2 + 2 * j])) for j in range(k)]
        pos += 1 + 2 * k
        cx = sum(p[0] for p in pts) / k
        cy = sum(p[1] for p in pts) / k
        pts.sort(key=lambda p: atan2(p[1] - cy, p[0] - cx))
        r = max(hypot(x - cx, y - cy) for x, y in pts)
        polys.append((pts, cx, cy, r))
    return mouse, cheese, polys


def clip(lo, hi, cons):
    """Narrows [lo, hi] by constraints alpha + beta * t >= 0."""
    for alpha, beta in cons:
        if abs(beta) < 1e-15:
            if alpha < 0:
                return None
        elif beta > 0:
            lo = max(lo, -alpha / beta)
        else:
            hi = min(hi, -alpha / beta)
        if lo > hi:
            return None
    return lo, hi


def safe_interval(a, d, poly):
    """The parameters t with a + t * d within SAFE of the polygon."""
    pts, _, _, _ = poly
    k = len(pts)
    pieces = []
    inside = []
    for i in range(k):
        (px, py), (qx, qy) = pts[i], pts[(i + 1) % k]
        ex, ey = qx - px, qy - py
        wx, wy = a[0] - px, a[1] - py
        cross_a = ex * wy - ey * wx
        cross_d = ex * d[1] - ey * d[0]
        inside.append((cross_a, cross_d))
        length = hypot(ex, ey)
        dot_a, dot_d = wx * ex + wy * ey, d[0] * ex + d[1] * ey
        strip = [
            (dot_a, dot_d),
            (length * length - dot_a, -dot_d),
            (SAFE * length - cross_a, -cross_d),
            (SAFE * length + cross_a, cross_d),
        ]
        pieces.append(clip(-1e18, 1e18, strip))
        # the disc around the corner: |w + t d|^2 <= SAFE^2
        qa = d[0] * d[0] + d[1] * d[1]
        qb = 2 * (wx * d[0] + wy * d[1])
        qc = wx * wx + wy * wy - SAFE * SAFE
        disc = qb * qb - 4 * qa * qc
        if qa > 0 and disc >= 0:
            root = disc**0.5
            pieces.append(((-qb - root) / (2 * qa), (-qb + root) / (2 * qa)))
    pieces.append(clip(-1e18, 1e18, inside))
    pieces = [p for p in pieces if p is not None]
    if not pieces:
        return None
    lo = max(0.0, min(p[0] for p in pieces))
    hi = min(1.0, max(p[1] for p in pieces))
    return (lo, hi) if lo < hi else None


def danger(path, polys, check):
    total = 0.0
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        d = (b[0] - a[0], b[1] - a[1])
        length = hypot(*d)
        if length == 0:
            continue
        spans = []
        for poly in polys:
            _, cx, cy, r = poly
            # skip furniture whose bounding circle is far from the segment
            t = ((cx - a[0]) * d[0] + (cy - a[1]) * d[1]) / (length * length)
            t = min(1.0, max(0.0, t))
            if hypot(a[0] + t * d[0] - cx, a[1] + t * d[1] - cy) > r + 2 * SAFE:
                continue
            span = safe_interval(a, d, poly)
            if span:
                spans.append(span)
        spans.sort()
        covered, end = 0.0, 0.0
        for lo, hi in spans:
            lo = max(lo, end)
            if hi > lo:
                covered += hi - lo
                end = hi
        safe = covered * length
        if check and TOL < safe < length - TOL:
            fail("segment %d is partly safe: %.6f of %.6f" % (i + 1, safe, length))
        total += length - safe
    return total


def read_path(path, mouse, cheese, check):
    try:
        tokens = open(path).read().split()
        count = int(tokens[0])
        values = [float(t) for t in tokens[1:]]
    except (ValueError, IndexError):
        fail("not a count and numbers")
    if count < 1 or count > LIMIT or len(values) != 2 * count:
        fail("expected between 1 and %d points, as many as announced" % LIMIT)
    pts = [(values[2 * i], values[2 * i + 1]) for i in range(count)]
    for want, got, name in ((mouse, pts[0], "mouse"), (cheese, pts[-1], "cheese")):
        if check and hypot(want[0] - got[0], want[1] - got[1]) > END_TOL:
            fail("the path does not end at the %s" % name)
    return pts


def main():
    inp, ans, output = sys.argv[1:4]
    mouse, cheese, polys = read_input(inp)
    best = danger(read_path(ans, mouse, cheese, False), polys, False)
    got = danger(read_path(output, mouse, cheese, True), polys, True)
    if got > best + TOL:
        fail("dangerous length %.6f, but %.6f is possible" % (got, best))
    if got < best - TOL:
        fail("dangerous length %.6f beats the reference %.6f" % (got, best))


if __name__ == "__main__":
    main()
