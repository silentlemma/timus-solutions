import math
import sys

BOX = 2  # the starting cell is a square of half-side BOX * R around the disk
SPAN = 4  # a site cuts a cell only within twice its reach: squared, 4 times
EPS = 1e-9


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


def inside(poly, x, y):
    """Whether (x, y) lies in the convex polygon, counterclockwise."""
    n = len(poly)
    for k in range(n):
        px, py = poly[k]
        qx, qy = poly[(k + 1) % n]
        if (qx - px) * (y - py) - (qy - py) * (x - px) < -EPS:
            return False
    return True


def farthest(poly, cx, cy, r):
    """The largest distance from (cx, cy) to a point of the polygon that
    lies in the disk of radius r around the origin."""
    best = 0.0
    n = len(poly)
    for k in range(n):
        px, py = poly[k]
        qx, qy = poly[(k + 1) % n]
        if px * px + py * py <= r * r:
            best = max(best, math.hypot(px - cx, py - cy))
        # where the edge crosses the circle: |p + t (q - p)| = r
        ux, uy = qx - px, qy - py
        a = ux * ux + uy * uy
        b = px * ux + py * uy
        c = px * px + py * py - r * r
        disc = b * b - a * c
        if a > 0 and disc >= 0:
            for t in ((-b - math.sqrt(disc)) / a, (-b + math.sqrt(disc)) / a):
                if 0 <= t <= 1:
                    best = max(best, math.hypot(px + t * ux - cx, py + t * uy - cy))
    # on an arc inside the cell the distance peaks at the circle point
    # opposite the site, if that point is in the cell
    norm = math.hypot(cx, cy)
    ox, oy = (-r * cx / norm, -r * cy / norm) if norm > 0 else (r, 0.0)
    if inside(poly, ox, oy):
        best = max(best, math.hypot(ox - cx, oy - cy))
    return best


def main():
    data = sys.stdin.read().split()
    n, r = int(data[0]), int(data[1])
    coords = iter(map(int, data[2 : 2 + 2 * n]))
    sites = list(zip(coords, coords))
    side = BOX * r
    answer = 0.0
    for cx, cy in sites:
        poly = [(-side, -side), (side, -side), (side, side), (-side, side)]
        dist = sorted(((x - cx) ** 2 + (y - cy) ** 2, x, y) for x, y in sites)
        for d, x, y in dist:
            if d == 0:
                continue  # the site itself, or another one at the same point
            reach = max((px - cx) ** 2 + (py - cy) ** 2 for px, py in poly)
            if d > SPAN * reach:
                break
            poly = clip(poly, (x + cx) / 2, (y + cy) / 2, x - cx, y - cy)
        answer = max(answer, farthest(poly, cx, cy, r))
    print("%.8f" % answer)


main()
