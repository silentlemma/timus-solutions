import sys

INF = float("inf")
HEADER = 3  # n, k and m come first
ROAD = 3  # a road is "h.d - h.d", three words


def main():
    data = sys.stdin.read().split()
    n, k, m = int(data[0]), int(data[1]), int(data[2])
    size = (k + 1) * n  # door d of house h is h * n + d
    road = [[INF] * size for _ in range(size)]
    pos = HEADER
    for _ in range(m):
        (h1, d1), (h2, d2) = (map(int, data[pos + side].split(".")) for side in (0, 2))
        u, v = h1 * n + d1, h2 * n + d2
        road[u][v] = road[v][u] = 1
        pos += ROAD
    source, sink = int(data[pos]), int(data[pos + 1])

    def outer_distances(inside):
        """Distances between the doors of the outer house when walking
        through an inner house from door i to door j costs inside[i][j]."""
        weight = [row[:] for row in road]
        for h in range(1, k + 1):
            base = h * n
            for i in range(n):
                for j in range(n):
                    if inside[i][j] < weight[base + i][base + j]:
                        weight[base + i][base + j] = inside[i][j]
        result = []
        for s in range(n):
            # Dijkstra on the dense graph, O(size^2)
            dist = [INF] * size
            done = [False] * size
            dist[s] = 0
            for _ in range(size):
                u, best = -1, INF
                for v in range(size):
                    if not done[v] and dist[v] < best:
                        u, best = v, dist[v]
                if u < 0:
                    break
                done[u] = True
                row = weight[u]
                for v in range(size):
                    if best + row[v] < dist[v]:
                        dist[v] = best + row[v]
            result.append(dist[:n])
        return result

    # Round t allows paths nested t houses deep; the distances only shrink,
    # and once a round changes nothing, no later round will.
    inside = outer_distances([[INF] * n for _ in range(n)])
    while True:
        nxt = outer_distances(inside)
        if nxt == inside:
            break
        inside = nxt
    answer = inside[source][sink]
    print("no solution" if answer == INF else answer)


main()
