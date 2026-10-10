import sys
from math import atan2, hypot, inf, sqrt

SAFE = 0.1
SAME = 1e-9


class Polygon:
    def __init__(self, pts):
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        # the vertices may come in any order, so sort them around the centre
        self.v = sorted(pts, key=lambda p: atan2(p[1] - cy, p[0] - cx))
        k = len(self.v)
        self.edges = []
        for i in range(k):
            (ax, ay), (bx, by) = self.v[i], self.v[(i + 1) % k]
            dx, dy = bx - ax, by - ay
            self.edges.append((ax, ay, dx, dy, dx * dx + dy * dy))
        self.cx, self.cy = cx, cy
        self.r = max(hypot(x - cx, y - cy) for x, y in pts)


def point_edges(px, py, edges, best):
    """The nearest point of the edges to (px, py) if closer than best[0]:
    best becomes [squared distance, edge index, position along the edge]."""
    for i, (ax, ay, dx, dy, d2) in enumerate(edges):
        wx, wy = px - ax, py - ay
        t = wx * dx + wy * dy
        if t <= 0:
            q, t = wx * wx + wy * wy, 0.0
        elif t >= d2:
            ex, ey = wx - dx, wy - dy
            q, t = ex * ex + ey * ey, 1.0
        else:
            c = wx * dy - wy * dx
            q, t = c * c / d2, t / d2
        if q < best[0]:
            best[0], best[1], best[2] = q, i, t


def point_poly(px, py, poly):
    best = [inf, 0, 0.0]
    point_edges(px, py, poly.edges, best)
    return best


def poly_poly(a, b):
    """Squared distance between two polygons and where it is reached on
    each: (squared distance, (edge, position) on a, (edge, position) on b)."""
    best, where = inf, None
    for own, other, flip in ((a, b, False), (b, a, True)):
        for k, (px, py) in enumerate(own.v):
            cur = [best, -1, 0.0]
            point_edges(px, py, other.edges, cur)
            if cur[1] >= 0:
                best = cur[0]
                here, there = (k, 0.0), (cur[1], cur[2])
                where = (there, here) if flip else (here, there)
    return best, where[0], where[1]


def at(poly, pos):
    ax, ay, dx, dy, _ = poly.edges[pos[0]]
    return ax + dx * pos[1], ay + dy * pos[1]


def walk(poly, src, dst):
    """Vertices passed going along the boundary from src to dst, taking the
    direction with fewer of them."""
    k = len(poly.v)
    (i, ti), (j, tj) = src, dst
    fwd = (j - i) % k or (0 if tj >= ti else k)
    back = (i - j) % k or (0 if tj <= ti else k)
    if fwd <= back:
        return [poly.v[(i + 1 + s) % k] for s in range(fwd)]
    return [poly.v[(i - s) % k] for s in range(back)]


def toward(f, p, length):
    d = hypot(p[0] - f[0], p[1] - f[1])
    return f[0] + (p[0] - f[0]) * length / d, f[1] + (p[1] - f[1]) * length / d


def main():
    it = iter(sys.stdin.read().split())
    mouse = (float(next(it)), float(next(it)))
    cheese = (float(next(it)), float(next(it)))
    polys = []
    for _ in range(int(next(it))):
        pts = [(float(next(it)), float(next(it))) for _ in range(int(next(it)))]
        polys.append(Polygon(pts))
    n = len(polys)

    # nodes 0..n-1 are the safe zones around the furniture, n the mouse and
    # n + 1 the cheese; an edge costs the dangerous length between them
    def to_point(p, a):
        return max(0.0, sqrt(point_poly(p[0], p[1], polys[a])[0]) - SAFE)

    start, goal = n, n + 1
    dist = [inf] * (n + 2)
    parent = [-1] * (n + 2)
    done = [False] * (n + 2)
    dist[start] = 0.0
    while True:
        u = min((d, v) for v, d in enumerate(dist) if not done[v])[1]
        if u == goal:
            break
        done[u] = True
        for v in range(n + 2):
            if done[v]:
                continue
            if v == goal and u == start:
                w = hypot(mouse[0] - cheese[0], mouse[1] - cheese[1])
            elif v == goal:
                w = to_point(cheese, u)
            elif u == start:
                w = to_point(mouse, v)
            else:
                a, b = polys[u], polys[v]
                gap = hypot(a.cx - b.cx, a.cy - b.cy) - a.r - b.r - 2 * SAFE
                if dist[u] + gap >= dist[v]:
                    continue
                w = sqrt(poly_poly(a, b)[0]) - 2 * SAFE
            if dist[u] + w < dist[v]:
                dist[v], parent[v] = dist[u] + w, u
    route = [goal]
    while route[-1] != start:
        route.append(parent[route[-1]])
    route.reverse()

    path = [mouse]
    if len(route) == 2:
        path.append(cheese)
    else:
        # step from the mouse onto the nearest point of the first piece
        first = polys[route[1]]
        q, i, t = point_poly(mouse[0], mouse[1], first)
        foot = at(first, (i, t))
        if sqrt(q) > SAFE:
            path.append(toward(foot, mouse, SAFE))
        path.append(foot)
        here = (i, t)
        for a, b in zip(route[1:-2], route[2:-1]):
            pa, pb = polys[a], polys[b]
            _, out_pos, in_pos = poly_poly(pa, pb)
            fa, fb = at(pa, out_pos), at(pb, in_pos)
            path += walk(pa, here, out_pos)
            path += [fa, toward(fa, fb, SAFE), toward(fb, fa, SAFE), fb]
            here = in_pos
        last = polys[route[-2]]
        q, i, t = point_poly(cheese[0], cheese[1], last)
        foot = at(last, (i, t))
        path += walk(last, here, (i, t))
        path.append(foot)
        if sqrt(q) > SAFE:
            path.append(toward(foot, cheese, SAFE))
        path.append(cheese)

    out = [path[0]]
    for p in path[1:]:
        if hypot(p[0] - out[-1][0], p[1] - out[-1][1]) > SAME:
            out.append(p)
    if len(out) == 1:
        out.append(path[-1])
    print(len(out))
    print("\n".join("%.9f %.9f" % p for p in out))


main()
