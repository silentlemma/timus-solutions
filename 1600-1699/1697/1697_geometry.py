import sys
from functools import cmp_to_key
from itertools import combinations

DIM = 3  # coordinates of the sniper
FIELDS = 5  # lx ly rx ry h
AREA = 3  # corners of a polygon with an inside

SIDES = 4  # the wall constraints come first


def blocked_interval(s, a, b, box):
    """The open interval of t for which the shot from S to A + t (B - A)
    passes through the inside of the box, as fractions (num_l, den_l,
    num_r, den_r), or None. A point of the shot is S + u (A - S) +
    v (B - A) with v = u t, so the box pulls back to a convex polygon in
    (u, v); its vertices come from pairs of boundary lines, in integers."""
    sx, sy, sz = s
    lx, ly, rx, ry, h = box
    ax, ay = a[0] - sx, a[1] - sy
    dx, dy = b[0] - a[0], b[1] - a[1]
    # constraints p u + q v >= c on the closed polygon
    cons = [(ax, dx, lx - sx), (-ax, -dx, sx - rx), (ay, dy, ly - sy), (-ay, -dy, sy - ry),
            (1, 0, 0), (-1, 0, -1),  # 0 <= u <= 1
            (1, 1, 0), (2, -1, 0)]  # -1 <= t <= 2 keeps the polygon bounded
    if any(p == 0 and q == 0 and c >= 0 for p, q, c in cons[:SIDES]):
        return None  # the plane of the shots holds a wall or misses the box
    if sz > 0:
        cons.append((sz, 0, sz - h))  # below the roof: sz (1 - u) <= h
    points = set()
    for (p1, q1, c1), (p2, q2, c2) in combinations(cons, 2):
        den = p1 * q2 - p2 * q1
        if den == 0:
            continue
        u, v = c1 * q2 - c2 * q1, p1 * c2 - p2 * c1
        if den < 0:
            den, u, v = -den, -u, -v
        if all(p * u + q * v >= c * den for p, q, c in cons):
            points.add((u, v, den))
    # the polygon has an inside exactly when it has three different corners
    distinct = []
    for u, v, den in points:
        if not any(u * d2 == u2 * den and v * d2 == v2 * den for u2, v2, d2 in distinct):
            distinct.append((u, v, den))
    if len(distinct) < AREA:
        return None
    # t = v / u, and u > 0 at every corner, as S is outside the box
    lo_n, lo_d = distinct[0][1], distinct[0][0]
    hi_n, hi_d = lo_n, lo_d
    for u, v, _ in distinct:
        if v * lo_d < lo_n * u:
            lo_n, lo_d = v, u
        if v * hi_d > hi_n * u:
            hi_n, hi_d = v, u
    return lo_n, lo_d, hi_n, hi_d


def main():
    words = iter(int(w) for w in sys.stdin.read().split())
    s = [next(words) for _ in range(DIM)]
    a = (next(words), next(words))
    b = (next(words), next(words))
    n = next(words)
    boxes = [[next(words) for _ in range(FIELDS)] for _ in range(n)]
    gaps = [g for g in (blocked_interval(s, a, b, box) for box in boxes) if g]
    # the free times form a closed set whose first point is 0 or the right
    # end of some blocked interval
    candidates = [(0, 1)] + [(hn, hd) for _, _, hn, hd in gaps if 0 <= hn <= hd]
    candidates.sort(key=cmp_to_key(lambda f, g: f[0] * g[1] - g[0] * f[1]))
    for tn, td in candidates:
        if not any(ln * td < tn * ld and tn * hd < hn * td for ln, ld, hn, hd in gaps):
            x = a[0] + (b[0] - a[0]) * tn / td
            y = a[1] + (b[1] - a[1]) * tn / td
            print("%.10f %.10f" % (x, y))
            return
    print("Impossible")


main()
