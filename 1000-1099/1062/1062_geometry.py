import sys

STAGES = 3
# the sides of the triangle x > 0, y > 0, x + y < 1 as a*x + b*y + c < 0,
# in boundary order
TRIANGLE = [(0, -1, 0), (1, 1, -1), (-1, 0, 0)]


def vertex(p, q):
    """The corner of lines p and q, all shifted by eps: numerators of x and y
    as (value, eps coefficient), and the common denominator."""
    (ap, bp, cp), (aq, bq, cq) = p, q
    det = ap * bq - aq * bp
    return -cp * bq + cq * bp, bp - bq, cp * aq - cq * ap, aq - ap, det


def side(v, line):
    """-1, 0 or 1: where corner v lies against line + eps, for a tiny eps."""
    x0, xe, y0, ye, det = v
    a, b, c = line
    t0 = a * x0 + b * y0 + c * det
    t1 = a * xe + b * ye + det
    if det < 0:
        t0, t1 = -t0, -t1
    if t0:
        return -1 if t0 < 0 else 1
    return (t1 > 0) - (t1 < 0)


def clip(edges, line):
    """Cut the polygon (its lines in boundary order) by line + eps <= 0."""
    m = len(edges)
    sides = [side(vertex(edges[k - 1], edges[k]), line) for k in range(m)]
    # edge k runs from corner k to corner k + 1; it stays if part of it is inside
    keep = [min(sides[k], sides[(k + 1) % m]) < 0 for k in range(m)]
    if not any(keep):
        return []
    start = keep.index(True)
    out = []
    for step in range(m):
        k = (start + step) % m
        if not keep[k]:
            continue
        out.append(edges[k])
        nxt = (k + 1) % m
        # the boundary leaves the half-plane before the next kept edge
        if not keep[nxt] or sides[nxt] > 0:
            out.append(line)
    return out if len(out) >= STAGES else []


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    speeds = [data[1 + STAGES * i : 1 + STAGES * (i + 1)] for i in range(n)]
    out = []
    for si in speeds:
        # with u_k = length_k / si_k > 0, athlete i beats j when
        # sum (sj_k - si_k) / sj_k * u_k < 0; times sj_1 sj_2 sj_3 this has
        # integer coefficients below 10^12
        edges = TRIANGLE
        for sj in speeds:
            if sj is si:
                continue
            prod = sj[0] * sj[1] * sj[2]
            g = [(sj[k] - si[k]) * (prod // sj[k]) for k in range(STAGES)]
            # u_3 = 1 - x - y on the triangle
            line = (g[0] - g[2], g[1] - g[2], g[2])
            if line[0] == line[1] == 0:
                if line[2] >= 0:
                    edges = []
                    break
                continue
            edges = clip(edges, line)
            if not edges:
                break
        out.append("Yes" if edges else "No")
    print("\n".join(out))


main()
