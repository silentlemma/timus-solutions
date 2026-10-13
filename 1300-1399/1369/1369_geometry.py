import math
import sys
from array import array

SCALE = 30  # decimal digits kept after the point
LANDMARKS = 1024  # evenly spread start points for the walks

# error bounds of the floating-point filters
ORIENT_ERR = 3.3306690621773722e-16
IN_CIRCLE_ERR = 1.1102230246251565e-15

# EPS = 2^-24 on squared distances, times 10^(2 * SCALE), an integer, and
# EPS_AT[c] the same bound for values times 10^(2 * c), rounded up
EPS_BITS = 24
EPS = 10 ** (2 * SCALE) >> EPS_BITS
EPS_AT = [-(-EPS // 10 ** (2 * (SCALE - c))) for c in range(SCALE + 1)]
EPS_FLOAT = 2.0**-EPS_BITS

# a difference of squared distances in doubles errs by less than this
SLACK = 1e-6
RELATIVE_SLACK = 1e-12
CORNERS = 3  # half-edges of a triangle
QUARTERS = 4  # the pseudo-angle of the hull hash runs through four quarters
HALF = 60  # an exact coordinate is kept as two ints: high << HALF | low
LOW_MASK = (1 << HALF) - 1
POW10 = [10**i for i in range(SCALE + 1)]


def parse_fixed(s):
    """a decimal number times 10^SCALE, digits beyond that dropped"""
    if "e" in s or "E" in s:  # rare: an exponent
        mantissa, _, e = s.replace("E", "e").partition("e")
        negative = mantissa[:1] == "-"
        whole, _, frac = mantissa.lstrip("+-").partition(".")
        digits = whole + frac
        shift = SCALE - len(frac) + int(e)
        if shift >= 0:
            v = int(digits or "0") * 10**shift
        else:
            v = int(digits[: max(0, len(digits) + shift)] or "0")
        return -v if negative else v
    negative = s[0] == "-"
    if negative or s[0] == "+":
        s = s[1:]
    dot = s.find(".")
    if dot < 0:
        v = int(s) * POW10[SCALE]
    else:
        frac = s[dot + 1 : dot + 1 + SCALE]
        v = int(s[:dot] + frac or "0") * POW10[SCALE - len(frac)]
    return -v if negative else v


def parse_scaled(s):
    """(the decimal s times 10^f, f): f significant digits after the point, at most SCALE"""
    if "e" in s or "E" in s:
        return parse_fixed(s), SCALE
    dot = s.find(".")
    if dot < 0:
        return int(s), 0
    frac = s[dot + 1 : dot + 1 + SCALE].rstrip("0")  # zeros at the end add nothing
    digits = s[:dot] + frac
    return int(digits) if digits.strip("+-") else 0, len(frac)


def truncated(s):
    """s without the digits after the point that parse_fixed drops"""
    dot = s.find(".")
    if dot < 0 or len(s) - dot - 1 <= SCALE or "e" in s or "E" in s:
        return s
    return s[: dot + 1 + SCALE]


def runs(idx, f):
    """the ranges [a, b) of idx with equal f"""
    a = 0
    while a < len(idx):
        b = a + 1
        while b < len(idx) and f[idx[b]] == f[idx[a]]:
            b += 1
        if b - a > 1:
            yield a, b
        a = b


def lex_order(idx, f1, f2, e1h, e1l, e2h, e2l):
    """idx sorted by the exact (e1, e2), mostly by the doubles f1 and f2"""
    idx.sort(key=f1.__getitem__)
    for a, b in runs(idx, f1):
        run = idx[a:b]
        i = run[0]
        if any(e1h[j] != e1h[i] or e1l[j] != e1l[i] for j in run):
            run.sort(key=lambda j: (e1h[j], e1l[j], e2h[j], e2l[j]))
        else:
            run.sort(key=f2.__getitem__)
            for c, d in runs(run, f2):
                run[c:d] = sorted(run[c:d], key=lambda j: (e2h[j], e2l[j]))
        idx[a:b] = run
    return idx


def main():
    tokens = (t for line in sys.stdin.buffer for t in line.decode().split())  # line by line
    m = int(next(tokens))
    # exact coordinates as high and low parts, to keep the memory small
    rxh, rxl, ryh, ryl = array("q"), array("q"), array("q"), array("q")
    rfx, rfy = array("d"), array("d")
    kept = array("b")  # the digits after the point of each cockroach
    digits = 0  # the most digits after the point among the cockroaches
    for _ in range(m):
        tx, ty = next(tokens), next(tokens)
        if len(tx) > SCALE:
            tx = truncated(tx)
        if len(ty) > SCALE:
            ty = truncated(ty)
        x, dx = parse_scaled(tx)
        y, dy = parse_scaled(ty)
        if dx < dy:
            x *= POW10[dy - dx]
        elif dy < dx:
            y *= POW10[dx - dy]
            dy = dx
        kept.append(dy)
        if dy > digits:
            digits = dy
        rxh.append(x >> HALF)
        rxl.append(x & LOW_MASK)
        ryh.append(y >> HALF)
        ryl.append(y & LOW_MASK)
        rfx.append(float(tx))
        rfy.append(float(ty))
    # the cockroaches keep only the digits they have, for shorter exact predicates
    for i in range(m):
        if kept[i] < digits:
            scale = POW10[digits - kept[i]]
            for arr_h, arr_l in ((rxh, rxl), (ryh, ryl)):
                v = ((arr_h[i] << HALF) | arr_l[i]) * scale
                arr_h[i], arr_l[i] = v >> HALF, v & LOW_MASK
    kept = None
    n = int(next(tokens))
    if n == 0:
        return
    # equal points become one, keeping all their cockroaches; equal decimals
    # have equal doubles, so they meet in the order
    order = lex_order(list(range(m)), rfx, rfy, rxh, rxl, ryh, ryl)
    xh, xl, yh, yl = array("q"), array("q"), array("q"), array("q")
    fx, fy = array("d"), array("d")
    first, ids = array("i"), array("i")  # the cockroaches of point v: ids[first[v]:first[v + 1]]
    for pos, i in enumerate(order):
        if (
            not xh
            or fx[-1] != rfx[i]
            or fy[-1] != rfy[i]
            or (xh[-1], xl[-1], yh[-1], yl[-1]) != (rxh[i], rxl[i], ryh[i], ryl[i])
        ):
            xh.append(rxh[i])
            xl.append(rxl[i])
            yh.append(ryh[i])
            yl.append(ryl[i])
            fx.append(rfx[i])
            fy.append(rfy[i])
            first.append(pos)
        ids.append(i + 1)
    first.append(m)
    order = rxh = rxl = ryh = ryl = rfx = rfy = None  # free the unsorted copies
    k = len(xh)
    if all(-1 <= h <= 0 for h in xh) and all(-1 <= h <= 0 for h in yh):
        # every value fits a machine word: one array each
        xq = array("q", ((xh[i] << HALF) | xl[i] for i in range(k)))
        yq = array("q", ((yh[i] << HALF) | yl[i] for i in range(k)))
        ex, ey = xq.__getitem__, yq.__getitem__
    else:

        def ex(i):
            return (xh[i] << HALF) | xl[i]

        def ey(i):
            return (yh[i] << HALF) | yl[i]

    # Each predicate is evaluated in floating point first; when the result is
    # within the rounding error, it is recomputed exactly on the decimals.
    def orient(a, b, c):
        lhs = (fx[a] - fx[c]) * (fy[b] - fy[c])
        rhs = (fy[a] - fy[c]) * (fx[b] - fx[c])
        det, err = lhs - rhs, ORIENT_ERR * abs(lhs + rhs)
        if det > err:
            return 1
        if det < -err:
            return -1
        d = (ex(a) - ex(c)) * (ey(b) - ey(c)) - (ey(a) - ey(c)) * (ex(b) - ex(c))
        return (d > 0) - (d < 0)

    def in_circle(a, b, c, d):
        """d lies strictly inside the circle through a, b, c (counterclockwise)"""
        xd, yd = fx[d], fy[d]
        adx, ady = fx[a] - xd, fy[a] - yd
        bdx, bdy = fx[b] - xd, fy[b] - yd
        cdx, cdy = fx[c] - xd, fy[c] - yd
        bc1, bc2 = bdx * cdy, cdx * bdy
        ca1, ca2 = cdx * ady, adx * cdy
        ab1, ab2 = adx * bdy, bdx * ady
        al, bl, cl = adx * adx + ady * ady, bdx * bdx + bdy * bdy, cdx * cdx + cdy * cdy
        det = al * (bc1 - bc2) + bl * (ca1 - ca2) + cl * (ab1 - ab2)
        permanent = (
            (abs(bc1) + abs(bc2)) * al + (abs(ca1) + abs(ca2)) * bl + (abs(ab1) + abs(ab2)) * cl
        )
        err = IN_CIRCLE_ERR * permanent
        if det > err:
            return True
        if det < -err:
            return False
        xd, yd = ex(d), ey(d)
        adx, ady = ex(a) - xd, ey(a) - yd
        bdx, bdy = ex(b) - xd, ey(b) - yd
        cdx, cdy = ex(c) - xd, ey(c) - yd
        al, bl, cl = adx * adx + ady * ady, bdx * bdx + bdy * bdy, cdx * cdx + cdy * cdy
        return (
            al * (bdx * cdy - cdx * bdy)
            + bl * (cdx * ady - adx * cdy)
            + cl * (adx * bdy - bdx * ady)
            > 0
        )

    # Delaunay by a sweep: points join the visible edges of the counterclockwise
    # hull by distance from a seed circle, and flips restore Delaunay. Triangles
    # are triples in tri, at most 2k - 5; half[e] is the twin of half-edge e, or -1.
    tri = array("i", [0]) * (CORNERS * max(1, 2 * k))
    half = array("i", [-1]) * len(tri)
    used = 0  # the half-edges in use
    stack = []

    def link(e, f):
        half[e] = f
        if f >= 0:
            half[f] = e

    def add_triangle(a, b, c, ea, eb, ec):
        nonlocal used
        t = used
        used += CORNERS
        tri[t], tri[t + 1], tri[t + 2] = a, b, c
        link(t, ea)
        link(t + 1, eb)
        link(t + 2, ec)
        return t

    def triangulate():
        cx0 = (min(fx) + max(fx)) / 2
        cy0 = (min(fy) + max(fy)) / 2
        i0 = min(range(k), key=lambda i: (fx[i] - cx0) ** 2 + (fy[i] - cy0) ** 2)
        i1 = min(
            (i for i in range(k) if i != i0),
            key=lambda i: (fx[i] - fx[i0]) ** 2 + (fy[i] - fy[i0]) ** 2,
        )
        best_r, i2 = float("inf"), -1
        for i in range(k):  # the smallest circle through i0, i1 and a third point
            if i == i0 or i == i1 or orient(i0, i1, i) == 0:
                continue
            r = circumradius2(i0, i1, i)
            if r < best_r:
                best_r, i2 = r, i
        if orient(i0, i1, i2) < 0:
            i1, i2 = i2, i1
        ccx, ccy = circumcentre(i0, i1, i2)
        order = sorted(range(k), key=lambda i: (fx[i] - ccx) ** 2 + (fy[i] - ccy) ** 2)
        size = max(1, math.isqrt(k))  # the hull hash: buckets by angle around the centre

        def bucket(i):
            dx, dy = fx[i] - ccx, fy[i] - ccy
            p = dx / (abs(dx) + abs(dy) or 1.0)
            angle = (QUARTERS - 1 - p if dy > 0 else 1 + p) / QUARTERS  # grows with the angle
            return int(angle * size) % size

        nxt_h, prv_h, edge_h = array("i", [0]) * k, array("i", [0]) * k, array("i", [0]) * k
        hull_hash = array("i", [-1]) * size
        nxt_h[i0], prv_h[i1], nxt_h[i1], prv_h[i2], nxt_h[i2], prv_h[i0] = i1, i0, i2, i1, i0, i2
        add_triangle(i0, i1, i2, -1, -1, -1)
        edge_h[i0], edge_h[i1], edge_h[i2] = 0, 1, 2  # the half-edge from v to its successor
        for i in (i0, i1, i2):
            hull_hash[bucket(i)] = i

        def legalize(e):
            depth = 0
            while True:
                f = half[e]
                e0 = e - e % CORNERS
                er = e0 + (e + 2) % CORNERS
                if f < 0:
                    if depth == 0:
                        return er
                    depth -= 1
                    e = stack[depth]
                    continue
                f0 = f - f % CORNERS
                el = e0 + (e + 1) % CORNERS
                fl = f0 + (f + 2) % CORNERS
                p0, pr, pl, p1 = tri[er], tri[e], tri[el], tri[fl]
                if in_circle(p0, pr, pl, p1):  # flip the shared edge
                    tri[e] = p1
                    tri[f] = p0
                    hfl = half[fl]
                    if hfl < 0:  # the hull edge from p1 is now e
                        edge_h[p1] = e
                    link(e, hfl)
                    link(f, half[er])
                    link(er, fl)
                    fr = f0 + (f + 1) % CORNERS
                    if depth < len(stack):
                        stack[depth] = fr
                    else:
                        stack.append(fr)
                    depth += 1
                else:
                    if depth == 0:
                        return er
                    depth -= 1
                    e = stack[depth]

        for i in order:
            if i == i0 or i == i1 or i == i2:
                continue
            key = bucket(i)
            start = -1
            for j in range(size):  # a hull vertex near the angle of i
                start = hull_hash[(key + j) % size]
                if start >= 0 and start != nxt_h[start]:
                    break
            start = prv_h[start]
            e = start
            while orient(e, nxt_h[e], i) >= 0:  # find an edge that i sees
                e = nxt_h[e]
                if e == start:
                    e = -1
                    break
            if e < 0:
                raise ValueError("no visible hull edge")
            t0 = add_triangle(e, i, nxt_h[e], -1, -1, edge_h[e])
            edge_h[i] = legalize(t0 + 2)
            edge_h[e] = t0
            n0 = nxt_h[e]
            while orient(n0, nxt_h[n0], i) < 0:  # forward along the visible edges
                q = nxt_h[n0]
                t0 = add_triangle(n0, i, q, edge_h[i], -1, edge_h[n0])
                edge_h[i] = legalize(t0 + 2)
                nxt_h[n0] = n0  # removed from the hull
                n0 = q
            if e == start:  # and backward
                while orient(prv_h[e], e, i) < 0:
                    q = prv_h[e]
                    t0 = add_triangle(q, i, e, -1, edge_h[e], edge_h[q])
                    legalize(t0 + 2)
                    edge_h[q] = t0
                    nxt_h[e] = e
                    e = q
            prv_h[i] = e
            nxt_h[e] = prv_h[n0] = i
            nxt_h[i] = n0
            hull_hash[key] = i
            hull_hash[bucket(e)] = e

    def circumradius2(a, b, c):
        dx, dy = fx[b] - fx[a], fy[b] - fy[a]
        ex2, ey2 = fx[c] - fx[a], fy[c] - fy[a]
        bl, cl = dx * dx + dy * dy, ex2 * ex2 + ey2 * ey2
        d = dx * ey2 - dy * ex2
        if d == 0:
            return float("inf")
        x = (ey2 * bl - dy * cl) / (2 * d)
        y = (dx * cl - ex2 * bl) / (2 * d)
        return x * x + y * y

    def circumcentre(a, b, c):
        dx, dy = fx[b] - fx[a], fy[b] - fy[a]
        ex2, ey2 = fx[c] - fx[a], fy[c] - fy[a]
        bl, cl = dx * dx + dy * dy, ex2 * ex2 + ey2 * ey2
        d = dx * ey2 - dy * ex2
        return fx[a] + (ey2 * bl - dy * cl) / (2 * d), fy[a] + (dx * cl - ex2 * bl) / (2 * d)

    # the graph: the triangulation plus the neighbours in the order by x, as
    # adjacency lists adj[start[v]:start[v + 1]], where an edge may repeat.
    # Inner half-edges come with their twins; pairs go both ways.
    pairs = array("i")
    for v in range(k - 1):  # neighbours by x; on a line, all edges
        pairs.extend((v, v + 1))
    collinear = all(orient(0, 1, i) == 0 for i in range(2, k))
    if k > 2 and not collinear:
        triangulate()
        for e in range(used):
            if half[e] < 0:  # a hull edge
                pairs.extend((tri[e], tri[e + 1 if e % CORNERS < 2 else e - 2]))
    start = array("i", [0]) * (k + 1)
    for e in range(used):
        if half[e] >= 0:
            start[tri[e] + 1] += 1
    for a in pairs:
        start[a + 1] += 1
    for v in range(k):
        start[v + 1] += start[v]
    at = array("i", start)
    adj = array("i", [0]) * start[k]
    for e in range(used):
        if half[e] >= 0:
            a = tri[e]
            adj[at[a]] = tri[e + 1 if e % CORNERS < 2 else e - 2]
            at[a] += 1
    for j in range(0, len(pairs), 2):
        a, b = pairs[j], pairs[j + 1]
        adj[at[a]] = b
        at[a] += 1
        adj[at[b]] = a
        at[b] += 1
    pairs = at = None
    del tri[:], half[:]

    # the answer: the nearest point and every point closer than it plus EPS,
    # found by a search through the graph from it
    marks = min(LANDMARKS, k)
    landmark = [i * (k - 1) // max(1, marks - 1) for i in range(marks)]
    seen = array("i", [0]) * k
    prev = 0
    out = []
    for stamp in range(1, n + 1):
        tx, ty = next(tokens), next(tokens)
        x, y = float(tx), float(ty)
        # the exact sweet, parsed when doubles cannot decide: the point times
        # pu and the sweet in units of 10^-c, then the bound in those units
        exact_q = []

        def exact_dist(i):
            if not exact_q:
                qx, cx = parse_scaled(tx)
                qy, cy = parse_scaled(ty)
                c = max(digits, cx, cy)
                exact_q.extend((qx * POW10[c - cx], qy * POW10[c - cy]))
                exact_q.extend((POW10[c - digits], EPS_AT[c]))
            pu = exact_q[2]
            return (ex(i) * pu - exact_q[0]) ** 2 + (ey(i) * pu - exact_q[1]) ** 2

        def closer(fa, fb, a, b, shift):
            """dist2(a) < dist2(b) + shift, in doubles when they can tell"""
            diff = fa - fb - shift * EPS_FLOAT
            slack = SLACK + RELATIVE_SLACK * (fa + fb)
            if diff > slack:
                return False
            if diff < -slack:
                return True
            if a == b:
                return shift > 0
            return exact_dist(a) < exact_dist(b) + shift * exact_q[-1]

        cur = prev
        bd = (fx[cur] - x) ** 2 + (fy[cur] - y) ** 2
        for v in landmark:
            d = (fx[v] - x) ** 2 + (fy[v] - y) ** 2
            if d < bd:
                cur, bd = v, d
        while True:  # a walk on floating point
            best = cur
            for j in range(start[cur], start[cur + 1]):
                u = adj[j]
                d = (fx[u] - x) ** 2 + (fy[u] - y) ** 2
                if d < bd:
                    best, bd = u, d
            if best == cur:
                break
            cur = best
        while True:  # an exact walk
            best = cur
            for j in range(start[cur], start[cur + 1]):
                u = adj[j]
                fu = (fx[u] - x) ** 2 + (fy[u] - y) ** 2
                if closer(fu, bd, u, best, 0):
                    best, bd = u, fu
            if best == cur:
                break
            cur = best
        prev = cur
        queue = [cur]
        seen[cur] = stamp
        answer = []
        for v in queue:
            fv = (fx[v] - x) ** 2 + (fy[v] - y) ** 2
            if not closer(fv, bd, v, cur, 1):
                continue
            answer.extend(ids[first[v] : first[v + 1]])
            for j in range(start[v], start[v + 1]):
                u = adj[j]
                if seen[u] != stamp:
                    seen[u] = stamp
                    queue.append(u)
        answer.sort()
        out.append(" ".join(map(str, answer)))
    sys.stdout.write("\n".join(out) + "\n")


main()
