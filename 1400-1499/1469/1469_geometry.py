import sys

SHEAR = 20001  # x' = SHEAR x + y keeps all points apart and no segment vertical
FIELDS = 4  # a cigarette: x1, y1, x2, y2


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


def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    n = data[0]
    raw = [data[1 + FIELDS * i : 1 + FIELDS * (i + 1)] for i in range(n)]
    plain = [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in raw]
    # Shamos-Hoey: sweep a vertical line over the sheared plane, keep the
    # segments it crosses ordered by height, and test only neighbours
    seg = [tuple(sorted(((SHEAR * x1 + y1, y1), (SHEAR * x2 + y2, y2)))) for x1, y1, x2, y2 in raw]

    def side(i, p):
        # the sign of the height of segment i above point p, at the x of p
        (x1, y1), (x2, y2) = seg[i]
        v = y1 * (x2 - x1) + (y2 - y1) * (p[0] - x1) - p[1] * (x2 - x1)
        return (v > 0) - (v < 0)

    def slope_less(i, j):
        (a1, b1), (a2, b2) = seg[i]
        (c1, d1), (c2, d2) = seg[j]
        return (b2 - b1) * (c2 - c1) < (d2 - d1) * (a2 - a1)

    def meet(i, j):
        if touch(plain[i][0], plain[i][1], plain[j][0], plain[j][1]):
            print("YES")
            print(i + 1, j + 1)
            sys.exit()

    # at one x, segments starting there come before those ending there
    events = sorted(
        [(s[0][0], 0, i) for i, s in enumerate(seg)] + [(s[1][0], 1, i) for i, s in enumerate(seg)]
    )
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
            if lo > 0:
                meet(i, line[lo - 1])
            if lo + 1 < len(line):
                meet(i, line[lo + 1])
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
            if 0 < k < len(line):
                meet(line[k - 1], line[k])
    print("NO")


main()
