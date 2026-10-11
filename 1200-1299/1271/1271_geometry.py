import heapq
import math
import sys

CORNERS = 3


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    """Convex hull, counterclockwise, without points on the edges."""
    points = sorted(set(points))
    lower, upper = [], []
    for p in points:
        while len(lower) > 1 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) > 1 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


class Polygon:
    """An open convex polygon: the places where the tanker hits a ship."""

    def __init__(self, vertices):
        self.v = vertices
        xs, ys = [p[0] for p in vertices], [p[1] for p in vertices]
        self.box = (min(xs), max(xs), min(ys), max(ys))
        # every edge normal, with the range of the polygon's projection on it
        self.axes = []
        for i, a in enumerate(vertices):
            b = vertices[(i + 1) % len(vertices)]
            n = (b[1] - a[1], a[0] - b[0])
            proj = [n[0] * p[0] + n[1] * p[1] for p in vertices]
            self.axes.append((n, min(proj), max(proj)))

    def holds(self, p):
        """Whether p is strictly inside."""
        k = len(self.v)
        return all(cross(self.v[i], self.v[(i + 1) % k], p) > 0 for i in range(k))

    def blocks(self, p, q):
        """Whether the segment pq crosses the inside: no axis separates them,
        neither an edge normal nor the normal of pq itself."""
        x0, x1, y0, y1 = self.box
        if max(p[0], q[0]) <= x0 or min(p[0], q[0]) >= x1:
            return False
        if max(p[1], q[1]) <= y0 or min(p[1], q[1]) >= y1:
            return False
        for n, lo, hi in self.axes:
            a, b = n[0] * p[0] + n[1] * p[1], n[0] * q[0] + n[1] * q[1]
            if max(a, b) <= lo or min(a, b) >= hi:
                return False
        n = (q[1] - p[1], p[0] - q[0])
        c = n[0] * p[0] + n[1] * p[1]
        proj = [n[0] * v[0] + n[1] * v[1] for v in self.v]
        return min(proj) < c < max(proj)


def main():
    nums = iter(map(int, sys.stdin.read().split()))
    dx, dy = next(nums), next(nums)
    tanker = [(next(nums), next(nums)) for _ in range(CORNERS)]
    goal = (next(nums), next(nums))
    n = next(nums)
    ships = [[(next(nums), next(nums)) for _ in range(CORNERS)] for _ in range(n)]
    # the tanker is placed by its first corner; offsets of all corners
    ax, ay = tanker[0]
    offsets = [(x - ax, y - ay) for x, y in tanker]
    xlo, xhi = -min(o[0] for o in offsets), dx - max(o[0] for o in offsets)
    ylo, yhi = -min(o[1] for o in offsets), dy - max(o[1] for o in offsets)
    polygons = [
        Polygon(hull([(x - ox, y - oy) for x, y in ship for ox, oy in offsets])) for ship in ships
    ]

    def free(p):
        return xlo <= p[0] <= xhi and ylo <= p[1] <= yhi and not any(g.holds(p) for g in polygons)

    start = tanker[0]
    if not free(goal):
        print(-1)
        return
    if goal == start:
        print("0.000")
        return
    # shortest paths bend only at corners of the forbidden polygons
    points = [start, goal] + sorted({v for g in polygons for v in g.v if free(v)})
    dist = [math.inf] * len(points)
    dist[0] = 0.0
    queue = [(0.0, 0)]
    done = [False] * len(points)
    while queue:
        d, i = heapq.heappop(queue)
        if done[i]:
            continue
        done[i] = True
        if i == 1:
            break
        p = points[i]
        for j, q in enumerate(points):
            if done[j] or q == p:
                continue
            nd = d + math.hypot(q[0] - p[0], q[1] - p[1])
            if nd < dist[j] and not any(g.blocks(p, q) for g in polygons):
                dist[j] = nd
                heapq.heappush(queue, (nd, j))
    print("%.3f" % dist[1] if dist[1] < math.inf else -1)


main()
