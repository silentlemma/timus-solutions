import math
import sys

EPS = 1e-7


def circles(a, ra, b, rb):
    """The common points of two circles."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    d2 = dx * dx + dy * dy
    if d2 == 0:
        return []
    along = (d2 + ra * ra - rb * rb) / (2 * d2)
    h2 = ra * ra / d2 - along * along
    if h2 < -EPS:
        return []
    h = math.sqrt(max(0.0, h2))
    x, y = a[0] + dx * along, a[1] + dy * along
    return [(x - dy * h, y + dx * h), (x + dy * h, y - dx * h)]


def line_circle(nx, ny, c, centre, radius):
    """The common points of the line nx * x + ny * y = c (unit normal) and
    a circle."""
    off = nx * centre[0] + ny * centre[1] - c
    h2 = radius * radius - off * off
    if h2 < -EPS:
        return []
    h = math.sqrt(max(0.0, h2))
    x, y = centre[0] - nx * off, centre[1] - ny * off
    return [(x - ny * h, y + nx * h), (x + ny * h, y - nx * h)]


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    small, big = int(data[1 + 2 * n]), int(data[2 + 2 * n])
    turn = sum(pts[i - 1][0] * pts[i][1] - pts[i][0] * pts[i - 1][1] for i in range(n))
    side = 1 if turn > 0 else -1
    edges = []
    for i in range(n):
        (ax, ay), (bx, by) = pts[i - 1], pts[i]
        length = math.hypot(bx - ax, by - ay)
        # outward unit normal
        nx, ny = side * (by - ay) / length, -side * (bx - ax) / length
        edges.append((ax, ay, bx - ax, by - ay, nx, ny, nx * ax + ny * ay))

    reach = (big + EPS) ** 2
    keep = (small - EPS) ** 2

    def fits(p):
        x, y = p
        for vx, vy in pts:
            if (x - vx) ** 2 + (y - vy) ** 2 > reach:
                return False
        outside = False
        for ax, ay, ex, ey, nx, ny, c in edges:
            if nx * x + ny * y > c:
                outside = True
            t = ((x - ax) * ex + (y - ay) * ey) / (ex * ex + ey * ey)
            t = min(1.0, max(0.0, t))
            if (x - ax - t * ex) ** 2 + (y - ay - t * ey) ** 2 < keep:
                return False
        return outside

    # the goat's area is where the discs of radius R around the vertices meet,
    # and when any of it is far enough from the bed, so is one of its corners
    # or a crossing of its boundary with the boundary of the bed grown by r
    for i in range(n):
        for j in range(n):
            found = []
            if i < j:
                found += circles(pts[i], big, pts[j], big)
            found += circles(pts[i], big, pts[j], small)
            ax, ay, ex, ey, nx, ny, c = edges[j]
            found += line_circle(nx, ny, c + small, pts[i], big)
            for p in found:
                if fits(p):
                    print("%.6f %.6f" % p)
                    return
    print("No solution")


main()
