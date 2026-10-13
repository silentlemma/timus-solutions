import itertools
import math
import sys

CORNERS = 3
WIDE = 2 * math.pi / 3  # 120 degrees
EPS = 1e-12
ROOT3 = math.sqrt(3) / 2  # the height of a unit equilateral triangle
PINS = 4
# the pairs that share an extra point, each way round
PAIRINGS = ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (2, 3, 0, 1), (1, 3, 0, 2), (1, 2, 0, 3))


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def fermat(p):
    # the point with the least total distance to three points (see 1451)
    for i, j in itertools.combinations(range(CORNERS), 2):
        if dist(p[i], p[j]) < EPS:
            return p[i]
    angle, side = [], []
    for i in range(CORNERS):
        a, b, c = p[i], p[(i + 1) % CORNERS], p[(i + 2) % CORNERS]
        ux, uy, wx, wy = b[0] - a[0], b[1] - a[1], c[0] - a[0], c[1] - a[1]
        angle.append(math.atan2(abs(ux * wy - uy * wx), ux * wx + uy * wy))
        side.append(dist(b, c))
    for i in range(CORNERS):
        if angle[i] >= WIDE:
            return p[i]
    w = [side[i] / math.sin(angle[i] + math.pi / CORNERS) for i in range(CORNERS)]
    total = sum(w)
    return (
        sum(w[i] * p[i][0] for i in range(CORNERS)) / total,
        sum(w[i] * p[i][1] for i in range(CORNERS)) / total,
    )


def apexes(a, b):
    # the two equilateral triangles on the segment ab
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    return [(mx - dy * ROOT3, my + dx * ROOT3), (mx + dy * ROOT3, my - dx * ROOT3)]


def shortest(p):
    best = math.inf
    # trees without extra points: the best spanning tree
    edges = sorted((dist(p[i], p[j]), i, j) for i, j in itertools.combinations(range(len(p)), 2))
    group = list(range(len(p)))

    def root(x):
        while group[x] != x:
            x = group[x]
        return x

    mst = 0.0
    for d, i, j in edges:
        if root(i) != root(j):
            group[root(i)] = root(j)
            mst += d
    best = min(best, mst)
    # one extra point joining three pins, the fourth wired to one of the four
    for trio in itertools.combinations(range(len(p)), CORNERS):
        s = fermat([p[i] for i in trio])
        star = sum(dist(s, p[i]) for i in trio)
        (rest,) = set(range(len(p))) - set(trio)
        link = min(dist(p[rest], q) for q in [p[i] for i in trio] + [s])
        best = min(best, star + link)
    # two extra points, {a, b} on one and {c, d} on the other: the Melzak
    # construction gives both, and the real length of that tree is a candidate
    for a, b, c, d in PAIRINGS:
        for e in apexes(p[a], p[b]):
            s2 = fermat([e, p[c], p[d]])
            s1 = fermat([p[a], p[b], s2])
            tree = dist(s1, p[a]) + dist(s1, p[b]) + dist(s1, s2) + dist(s2, p[c]) + dist(s2, p[d])
            best = min(best, tree)
    return best


def main():
    v = [int(x) for x in sys.stdin.read().split()]
    out = []
    coords = v[1:]
    for t in range(v[0]):
        pins = coords[2 * PINS * t : 2 * PINS * (t + 1)]
        out.append("%.6f" % shortest(list(zip(pins[0::2], pins[1::2]))))
    print("\n".join(out))


main()
