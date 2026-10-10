import sys
from math import hypot, inf


def main():
    it = iter(sys.stdin.read().split())
    walk, metro, n = float(next(it)), float(next(it)), int(next(it))
    pts = [(float(next(it)), float(next(it))) for _ in range(n)]
    linked = [[False] * (n + 2) for _ in range(n + 2)]
    while True:
        a, b = int(next(it)), int(next(it))
        if a == 0 and b == 0:
            break
        linked[a - 1][b - 1] = linked[b - 1][a - 1] = True
    for _ in range(2):
        pts.append((float(next(it)), float(next(it))))
    # nodes: the stations, then A and B; the subway is never slower than
    # walking, so a linked pair always goes by train
    total = n + 2
    start, goal = n, n + 1
    dist = [inf] * total
    prev = [-1] * total
    done = [False] * total
    dist[start] = 0.0
    for _ in range(total):
        u = min((v for v in range(total) if not done[v]), key=dist.__getitem__)
        done[u] = True
        ux, uy = pts[u]
        for v in range(total):
            if not done[v]:
                d = hypot(pts[v][0] - ux, pts[v][1] - uy) / (metro if linked[u][v] else walk)
                if dist[u] + d < dist[v]:
                    dist[v], prev[v] = dist[u] + d, u
    path = []
    v = prev[goal]
    while v != start:
        path.append(v + 1)
        v = prev[v]
    path.reverse()
    print("%.10f" % dist[goal])
    print(" ".join(map(str, [len(path)] + path)))


main()
