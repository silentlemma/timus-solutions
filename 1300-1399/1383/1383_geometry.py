import sys
from math import gcd

# a pair of frame coordinates, each below 2^24 in size, packed into one
# integer whose order is the order of the pairs: sorting numbers is faster
HALF = 1 << 24
SPAN = 1 << 25


def scaled(values, den):
    """Fractions value / den over their least common denominator: equal
    lists of fractions give equal results."""
    g = gcd(den, *values) if values else den
    return den // g, [v // g for v in values]


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    """Strict convex hull, counterclockwise, of distinct points."""
    pts = sorted(points)
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def in_frame(points, o, e1, e2, keep_order=False):
    """Coordinates of points in the frame o + s e1 + t e2, as a common
    denominator and packed pairs of numerators, sorted unless asked
    otherwise."""
    ox, oy = o
    ax, ay = e1
    bx, by = e2
    d = ax * by - ay * bx
    s = [(x - ox) * by - (y - oy) * bx for x, y in points]
    t = [ax * (y - oy) - ay * (x - ox) for x, y in points]
    g = gcd(d, gcd(*s), gcd(*t))
    packed = [(u // g + HALF) * SPAN + v // g + HALF for u, v in zip(s, t)]
    if not keep_order:
        packed.sort()
    return d // g, packed


def canonical(points):
    """The same for two point lists exactly when an affine map of positive
    determinant takes one onto the other."""
    distinct = set(points)
    if len(distinct) == 1:
        return (0, len(points))
    h = hull(distinct)
    if len(h) == 2:
        # on one line: positions from 0 to 1 between the ends, read either way
        a, b = h
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = dx * dx + dy * dy
        ts = [(x - a[0]) * dx + (y - a[1]) * dy for x, y in points]
        den, forward = scaled(ts, length)
        backward = [den - t for t in forward]
        return (1, den, tuple(min(sorted(forward), sorted(backward))))
    # the frame at hull vertex i: it goes to 0, the next to (1, 0) and the
    # previous to (0, 1); a map of positive determinant keeps the order
    k = len(h)

    def frame(i):
        o = h[i]
        nxt, prv = h[(i + 1) % k], h[i - 1]
        return o, (nxt[0] - o[0], nxt[1] - o[1]), (prv[0] - o[0], prv[1] - o[1])

    shapes = [in_frame(h[i:] + h[:i], *frame(i), keep_order=True) for i in range(k)]
    best = min(shapes)
    keys = [in_frame(points, *frame(i)) for i in range(k) if shapes[i] == best]
    den, packed = min(keys)
    return (2, k, den, tuple(packed))


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pos = 1
    classes = {}
    sizes = {}
    for project in range(1, n + 1):
        m = int(data[pos])
        pos += 1
        pts = [(int(data[pos + 2 * j]), int(data[pos + 2 * j + 1])) for j in range(m)]
        pos += 2 * m
        key = canonical(pts)
        classes.setdefault(key, []).append(project)
        sizes[key] = m
    # smaller projects first, then by the first project of the class
    order = sorted(classes, key=lambda key: (sizes[key], classes[key][0]))
    out = [str(len(order))]
    for key in order:
        out.append(" ".join(map(str, classes[key] + [0])))
    print("\n".join(out))


main()
