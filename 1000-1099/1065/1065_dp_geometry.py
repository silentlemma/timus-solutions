import math
import sys


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    coords = data[2:]
    points = list(zip(coords[0::2], coords[1::2]))
    towers, monuments = points[:n], points[n : n + m]
    dist = [[math.dist(a, b) for b in towers] for a in towers]
    best = math.inf
    if m == 0:
        # any convex border contains a triangle of its towers that is not
        # longer, so the best border is the shortest triangle with an area
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if cross(towers[i], towers[j], towers[k]) != 0:
                        best = min(best, dist[i][j] + dist[j][k] + dist[k][i])
    else:
        # the border goes clockwise, so the inside is on the right of every
        # side: a side i -> j may be used when all monuments are strictly right
        ok = [
            [
                i != j and all(cross(towers[i], towers[j], p) < 0 for p in monuments)
                for j in range(n)
            ]
            for i in range(n)
        ]
        # a monument inside rules out degenerate borders; from every first
        # tower, the shortest way around through towers in their order
        for s in range(n):
            way = [math.inf] * n
            way[s] = 0.0
            for step in range(1, n):
                k = (s + step) % n
                for back in range(step):
                    j = (s + back) % n
                    if ok[j][k] and way[j] + dist[j][k] < way[k]:
                        way[k] = way[j] + dist[j][k]
                if ok[k][s]:
                    best = min(best, way[k] + dist[k][s])
    print("%.2f" % best)


main()
