import math
import sys

DIM = 3
STEPS = 60  # halvings in each bisection
SPHERE = 1500  # directions tried for the narrowest width

TINY = 1e-13  # where the local search stops
CLOSE = 1e-10  # equal widths, relative to the diameter
ROUNDS = 400  # passes of a local search, which may creep on forever

HELPER = 0.9  # a helper axis closer than this to n gives a poor cross product
GOLDEN = 2.399963229728653  # the golden angle, spreading directions over the sphere


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def comb(a, s, b, t):
    """s * a + t * b"""
    return (s * a[0] + t * b[0], s * a[1] + t * b[1], s * a[2] + t * b[2])


def unit(a):
    norm = math.sqrt(dot(a, a))
    return (a[0] / norm, a[1] / norm, a[2] / norm)


def turn(v, axis, angle):
    """v turned by angle around the unit vector axis (Rodrigues)."""
    c, s = math.cos(angle), math.sin(angle)
    k = dot(axis, v) * (1 - c)
    w = cross(axis, v)
    return (v[0] * c + w[0] * s + axis[0] * k, v[1] * c + w[1] * s + axis[1] * k,
            v[2] * c + w[2] * s + axis[2] * k)


def across(n):
    """Two unit vectors completing n to a right-handed frame."""
    helper = (0.0, 1.0, 0.0) if abs(n[0]) > HELPER else (1.0, 0.0, 0.0)
    a = unit(cross(n, helper))
    return a, cross(n, a)


def main():
    data = sys.stdin.read().split()
    count = int(data[0])
    ints = [tuple(int(w) for w in data[1 + DIM * i:1 + DIM * (i + 1)]) for i in range(count)]
    pts = [tuple(float(c) for c in p) for p in ints]

    def width(u):
        proj = [u[0] * x + u[1] * y + u[2] * z for x, y, z in pts]
        return max(proj) - min(proj)

    def spread(frame):
        ws = [width(u) for u in frame]
        return max(ws) - min(ws)

    def show(frame):
        print("\n".join(" ".join("%.15f" % c for c in u) for u in frame))

    # Accept the initial coordinate frame when its box is already a cube.
    aligned = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
    ws = [width(u) for u in aligned]
    if ws[0] == ws[1] == ws[2]:
        show(aligned)
        return

    # the shape of the swarm, decided exactly on the integers
    base = ints[0]
    diffs = [tuple(p[k] - base[k] for k in range(DIM)) for p in ints[1:]]
    first = next(d for d in diffs if any(d))
    normal = next((cross(first, d) for d in diffs if any(cross(first, d))), None)
    if normal is None:
        # all on a line of direction d: an axis at angle acos(1/sqrt 3) to the
        # line each, so the three widths are the length over sqrt 3
        d = unit(first)
        u, v = across(d)
        r3, r2, r6 = 1 / math.sqrt(DIM), 1 / math.sqrt(2), 1 / math.sqrt(2 * DIM)
        show([comb(comb(d, r3, u, r2), 1, v, r6), comb(comb(d, r3, u, -r2), 1, v, r6),
              comb(d, r3, v, -2 * r6)])
        return
    flat = all(dot(normal, d) == 0 for d in diffs)

    # widest direction: the diameter, where no other width can be larger
    far = max(((p, q) for p in ints for q in ints), key=lambda pq: sum(
        (pq[0][k] - pq[1][k]) ** 2 for k in range(DIM)))
    n_max = unit(tuple(float(far[0][k] - far[1][k]) for k in range(DIM)))
    # narrowest direction: the normal of a flat swarm, else a search
    if flat:
        n_min = unit(tuple(float(c) for c in normal))
    else:
        best = None
        for i in range(SPHERE):
            z = 1 - (2 * i + 1) / (2 * SPHERE)
            r = math.sqrt(1 - z * z)
            u = (r * math.cos(GOLDEN * i), r * math.sin(GOLDEN * i), z)
            w = width(u)
            if best is None or w < best[0]:
                best = (w, u)
        w_min, n_min = best
        step = 2 * math.pi / math.sqrt(SPHERE)
        for _ in range(ROUNDS):
            if step <= TINY:
                break
            a, b = across(n_min)
            moved = False
            for axis in (a, b, unit(comb(a, 1, b, 1)), unit(comb(a, 1, b, -1))):
                for sign in (1, -1):
                    cand = unit(turn(n_min, axis, sign * step))
                    w = width(cand)
                    if w < w_min:
                        w_min, n_min, moved = w, cand, True
            if not moved:
                step /= 2

    # frames along the great circle from n_min to n_max: the third axis is
    # the turned n, the first two the turned a0, b0 rotated by phi
    hinge = cross(n_min, n_max)
    if dot(hinge, hinge) < TINY:
        hinge = across(n_min)[0]
    hinge = unit(hinge)
    angle = math.acos(max(-1.0, min(1.0, dot(n_min, n_max))))
    a0, b0 = across(n_min)

    def frame(t, phi):
        n = turn(n_min, hinge, angle * t)
        a, b = turn(a0, hinge, angle * t), turn(b0, hinge, angle * t)
        c, s = math.cos(phi), math.sin(phi)
        return [comb(a, c, b, s), comb(a, -s, b, c), n]

    def balance(t):
        """phi in [0, pi/2] with equal first two widths: the difference
        changes sign over a quarter turn, as the axes swap places."""
        def diff(phi):
            f = frame(t, phi)
            return width(f[0]) - width(f[1])
        lo, hi = 0.0, math.pi / 2
        if diff(lo) > 0:
            lo, hi = hi, lo
        for _ in range(STEPS):
            mid = (lo + hi) / 2
            if diff(mid) > 0:
                hi = mid
            else:
                lo = mid
        return (lo + hi) / 2

    def gap(t):
        f = frame(t, balance(t))
        return width(f[2]) - width(f[0]), f

    # try equalizing the third width; the candidate is checked afterwards
    lo, hi = 0.0, 1.0
    for _ in range(STEPS):
        mid = (lo + hi) / 2
        if gap(mid)[0] < 0:
            lo = mid
        else:
            hi = mid
    result = gap((lo + hi) / 2)[1]
    scale = max(1.0, width(n_max))

    if spread(result) > CLOSE * scale:
        # A nonzero winding encloses equal widths; unlike local minima,
        # it survives subdivision. Quaternions keep every frame orthogonal.
        def axes(q):
            w, x, y, z = q
            return [(1 - 2 * (y * y + z * z), 2 * (x * y + w * z), 2 * (x * z - w * y)),
                    (2 * (x * y - w * z), 1 - 2 * (x * x + z * z), 2 * (y * z + w * x)),
                    (2 * (x * z + w * y), 2 * (y * z - w * x), 1 - 2 * (x * x + y * y))]

        found = None

        def vertex(q):
            nonlocal found
            f = axes(q)
            ws = [width(u) for u in f]
            if max(ws) - min(ws) <= CLOSE * scale:
                found = f
            return q, (ws[0] - ws[2], ws[1] - ws[2])

        def middle(a, b):
            q = tuple(x + y for x, y in zip(a[0], b[0]))
            norm = math.sqrt(sum(x * x for x in q))
            return vertex(tuple(x / norm for x in q))

        def edge(a, b):
            if found is not None:
                return 0.0
            distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(a[0], b[0])))
            u, v = a[1], b[1]
            # Each residual changes by at most 4 * diameter * chord length.
            if max(abs(u[0]), abs(u[1])) > 4 * scale * distance:
                return math.atan2(u[0] * v[1] - u[1] * v[0], u[0] * v[0] + u[1] * v[1])
            m = middle(a, b)
            return edge(a, m) + edge(m, b)

        def winding(a, b, c):
            return edge(a, b) + edge(b, c) + edge(c, a)

        # The boundary cycles the axes, so its winding cannot be zero.
        rim = [vertex(q) for q in ((1.0, 0.0, 0.0, 0.0),
               (-0.5, 0.5, 0.5, 0.5), (-0.5, -0.5, -0.5, -0.5))]
        r2 = 1 / math.sqrt(2)
        center = vertex((0.0, r2, -r2, 0.0))
        triangle = None
        for i in range(DIM):
            tri = (center, rim[i], rim[(i + 1) % DIM])
            if abs(winding(*tri)) > math.pi:
                triangle = tri
                break
        while found is None:
            a, b, c = triangle
            ab, bc, ca = middle(a, b), middle(b, c), middle(c, a)
            for tri in ((a, ab, ca), (ab, b, bc), (ca, bc, c), (ab, bc, ca)):
                if abs(winding(*tri)) > math.pi:
                    triangle = tri
                    break
        result = found
    show(result)


main()
