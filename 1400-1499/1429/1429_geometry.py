import math
import sys
from array import array

CELL = 1e-3  # distinct crossing points are at least this far apart
SAME = 1e-4  # two estimates of one point are much closer than this


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # a cut made twice is still one cut
    vals = iter(map(int, data[1:]))
    circles = sorted({(next(vals), next(vals), next(vals)) for _ in range(n)})
    k = len(circles)
    parent = list(range(k))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    # the estimates of the crossing points on each circle, in flat arrays:
    # one table of all points would not fit in the memory limit
    xs = [array("d") for _ in range(k)]
    ys = [array("d") for _ in range(k)]
    for i in range(k):
        x1, y1, r1 = circles[i]
        for j in range(i + 1, k):
            x2, y2, r2 = circles[j]
            dx, dy = x2 - x1, y2 - y1
            d2 = dx * dx + dy * dy
            if d2 > (r1 + r2) ** 2 or d2 < (r1 - r2) ** 2:
                continue  # apart, or one inside the other
            # the crossings are p1 + (m * (dx, dy) +- sqrt(K) * (-dy, dx)) / (2 d2), K exact
            m = d2 + r1 * r1 - r2 * r2
            root = math.sqrt((2 * r1) * (2 * r1) * d2 - m * m)
            for sign in (1, -1) if root > 0 else (1,):
                x = x1 + (m * dx - sign * root * dy) / (2 * d2)
                y = y1 + (m * dy + sign * root * dx) / (2 * d2)
                for c in (i, j):
                    xs[c].append(x)
                    ys[c].append(y)
            parent[find(i)] = find(j)
    # on each circle, estimates of one point merge into a group; a group of s
    # estimates is a point on s + 1 circles, so it adds 1 / (s + 1) vertex
    edges = 0
    shared = {}  # circles through a point -> how often such points were seen
    for i in range(k):
        grid = {}
        sizes, seen_x, seen_y = [], [], []
        for x, y in zip(xs[i], ys[i]):
            cx, cy = math.floor(x / CELL), math.floor(y / CELL)
            found = -1
            for gx in (cx - 1, cx, cx + 1):
                for gy in (cy - 1, cy, cy + 1):
                    for p in grid.get((gx, gy), ()):
                        if abs(seen_x[p] - x) < SAME and abs(seen_y[p] - y) < SAME:
                            found = p
            if found < 0:
                grid.setdefault((cx, cy), []).append(len(sizes))
                sizes.append(1)
                seen_x.append(x)
                seen_y.append(y)
            else:
                sizes[found] += 1
        edges += len(sizes) or 1
        for s in sizes or [0]:
            shared[s + 1] = shared.get(s + 1, 0) + 1
        xs[i] = ys[i] = None
    vertices = sum(count // c for c, count in shared.items())
    # Euler's formula for a plane graph: faces = edges - vertices + components + 1,
    # a circle with no crossings counts as one vertex and one edge
    components = sum(1 for i in range(k) if find(i) == i)
    print(edges - vertices + components + 1)


main()
