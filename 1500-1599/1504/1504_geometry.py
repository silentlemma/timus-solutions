import math
import sys

EPS = 1e-9
BOX = 2  # the starting cell is a square of half-side BOX * R around the table
SPAN = 4  # a piece cuts a cell only within twice its reach: squared, 4 times


def clip(poly, mx, my, dx, dy):
    """The part of the convex polygon with (p - m) . d <= 0."""
    out = []
    n = len(poly)
    for k in range(n):
        px, py = poly[k]
        qx, qy = poly[(k + 1) % n]
        sp = (px - mx) * dx + (py - my) * dy
        sq = (qx - mx) * dx + (qy - my) * dy
        if sp <= 0:
            out.append((px, py))
        if (sp < 0 < sq) or (sq < 0 < sp):
            t = sp / (sp - sq)
            out.append((px + t * (qx - px), py + t * (qy - py)))
    return out


def seat(pieces, i, r):
    """A point of the table edge where piece i is the nearest, or None.

    The points nearer to piece i than to any other form its Voronoi cell,
    a convex polygon around the piece; it reaches the edge exactly when
    its farthest vertex from the centre is at least R away."""
    cx, cy = pieces[i][0], pieces[i][1]
    side = BOX * r
    poly = [(-side, -side), (side, -side), (side, side), (-side, side)]
    dist = [(x - cx) ** 2 + (y - cy) ** 2 for x, y, _ in pieces]
    limit = r * r - EPS
    for j in sorted(range(len(pieces)), key=dist.__getitem__):
        if j == i:
            continue
        # a piece farther than twice the cell's reach cannot cut it
        reach = max((x - cx) ** 2 + (y - cy) ** 2 for x, y in poly)
        if dist[j] > SPAN * reach:
            break
        x, y = pieces[j][0], pieces[j][1]
        poly = clip(poly, (x + cx) / 2, (y + cy) / 2, x - cx, y - cy)
        if not poly or max(x * x + y * y for x, y in poly) < limit:
            return None
    vx, vy = max(poly, key=lambda p: p[0] * p[0] + p[1] * p[1])
    # the segment from the piece to that vertex lies in the cell and
    # crosses the edge: solve |c + t (v - c)| = R
    ux, uy = vx - cx, vy - cy
    a = ux * ux + uy * uy
    b = cx * ux + cy * uy
    c = cx * cx + cy * cy - r * r
    t = min(1.0, (-b + math.sqrt(max(0.0, b * b - a * c))) / a)
    px, py = cx + t * ux, cy + t * uy
    norm = math.hypot(px, py)
    return px * r / norm, py * r / norm


def main():
    data = sys.stdin.read().split()
    r, k = float(data[0]), int(data[1])
    rows = iter(data[2:])
    pieces = [(float(x), float(y), int(w)) for x, y, w in zip(rows, rows, rows)]
    for i in sorted(range(k), key=lambda i: -pieces[i][2]):
        point = seat(pieces, i, r)
        if point:
            print("%.10f %.10f" % point)
            return


main()
