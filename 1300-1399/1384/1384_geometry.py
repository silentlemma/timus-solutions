import itertools
import math
import sys

EPS = 1e-9
SITES = 3  # sites that meet at a candidate centre


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    pts = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]
    edges = [(pts[i], pts[(i + 1) % n]) for i in range(n)]
    # each edge as a line n . p + c, positive inside the counterclockwise polygon
    lines = []
    for (ax, ay), (bx, by) in edges:
        length = math.hypot(bx - ax, by - ay)
        nx, ny = -(by - ay) / length, (bx - ax) / length
        lines.append((nx, ny, -(nx * ax + ny * ay)))
    # only reflex vertices can be the nearest point of the fence from inside
    reflex = []
    for i in range(n):
        (ax, ay), (bx, by), (cx, cy) = pts[i - 1], pts[i], pts[(i + 1) % n]
        if (bx - ax) * (cy - by) - (by - ay) * (cx - bx) < 0:
            reflex.append((bx, by))

    def distance(px, py):
        """Distance from an inner point to the fence, or -1 outside."""
        inside, best = False, math.inf
        for (ax, ay), (bx, by) in edges:
            if (ay > py) != (by > py) and px < ax + (py - ay) * (bx - ax) / (by - ay):
                inside = not inside
            dx, dy = bx - ax, by - ay
            t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
            best = min(best, math.hypot(px - ax - t * dx, py - ay - t * dy))
        return best if inside else -1.0

    candidates = []
    # three lines: n_i . p + c_i = r for all three, a linear system
    for (a1, b1, c1), (a2, b2, c2), (a3, b3, c3) in itertools.combinations(lines, SITES):
        det = a1 * (b2 - b3) - b1 * (a2 - a3) + (a2 * b3 - a3 * b2)
        if abs(det) < EPS:
            continue
        # columns (a, b, -1) and right-hand side -c, solved by Cramer's rule
        rx = -c1 * (b2 - b3) - b1 * (-c2 + c3) + (-c2 * b3 + c3 * b2)
        ry = a1 * (-c2 + c3) + c1 * (a2 - a3) + (a2 * -c3 + a3 * c2)
        candidates.append((rx / det, ry / det))

    def on_circle(ox, oy, ux, uy, base, slope, vx, vy):
        """Points o + t u whose distance to v equals base + slope t."""
        # |o + t u - v|^2 = (base + slope t)^2, or qa t^2 + 2 hb t + qc = 0
        wx, wy = ox - vx, oy - vy
        qa = ux * ux + uy * uy - slope * slope
        hb = wx * ux + wy * uy - base * slope
        qc = wx * wx + wy * wy - base * base
        disc = hb * hb - qa * qc
        if disc < -EPS * (hb * hb + abs(qa * qc)):
            return []
        # the stable form of the roots, also when qa is next to zero
        q = -(hb + math.copysign(math.sqrt(max(0.0, disc)), hb))
        roots = []
        if abs(qa) > EPS:
            roots.append(q / qa)
        if abs(q) > EPS:
            roots.append(qc / q)
        return [(ox + t * ux, oy + t * uy) for t in roots]

    # two lines and a reflex vertex: on the bisector, as far from the vertex
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(lines, 2):
        da, db, dc = a1 - a2, b1 - b2, c1 - c2
        norm = da * da + db * db
        if norm < EPS:
            continue
        ox, oy = -dc * da / norm, -dc * db / norm  # a point of the bisector
        ux, uy = -db, da
        for vx, vy in reflex:
            base, slope = a1 * ox + b1 * oy + c1, a1 * ux + b1 * uy
            candidates += on_circle(ox, oy, ux, uy, base, slope, vx, vy)
    # a line and two reflex vertices: on their perpendicular bisector
    for (v1x, v1y), (v2x, v2y) in itertools.combinations(reflex, 2):
        ox, oy = (v1x + v2x) / 2, (v1y + v2y) / 2
        ux, uy = -(v2y - v1y), v2x - v1x
        for a1, b1, c1 in lines:
            base, slope = a1 * ox + b1 * oy + c1, a1 * ux + b1 * uy
            candidates += on_circle(ox, oy, ux, uy, base, slope, v1x, v1y)
    # three reflex vertices: the centre of their circle
    for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(reflex, SITES):
        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if abs(d) < EPS:
            continue
        s1, s2, s3 = x1 * x1 + y1 * y1, x2 * x2 + y2 * y2, x3 * x3 + y3 * y3
        candidates.append(
            (
                (s1 * (y2 - y3) + s2 * (y3 - y1) + s3 * (y1 - y2)) / d,
                (s1 * (x3 - x2) + s2 * (x1 - x3) + s3 * (x2 - x1)) / d,
            )
        )
    print("%.2f" % max(0.0, max((distance(x, y) for x, y in candidates), default=0.0)))


main()
