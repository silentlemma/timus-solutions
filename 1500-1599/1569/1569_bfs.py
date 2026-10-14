import sys
from collections import deque


def main():
    words = iter(sys.stdin.read().split())
    n, m = int(next(words)), int(next(words))
    edges = [(int(next(words)) - 1, int(next(words)) - 1) for _ in range(m)]
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def bfs(sources):
        """Distances from the nearest source and the edges of a tree of
        shortest paths that grows from the sources."""
        dist = [-1] * n
        tree = []
        queue = deque(sources)
        for s in sources:
            dist[s] = 0
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if dist[u] < 0:
                    dist[u] = dist[v] + 1
                    tree.append((v, u))
                    queue.append(u)
        return dist, tree

    dist = [bfs([v])[0] for v in range(n)]
    # the middle of a tree of least diameter is a node or the middle of an edge, and
    # a tree of shortest paths from there has diameter 2 r or 2 r + 1 for the
    # largest distance r from it, and no tree can do better
    best, centre = min((2 * max(dist[v]), (v,)) for v in range(n))
    for a, b in edges:
        reach = 2 * max(min(x, y) for x, y in zip(dist[a], dist[b])) + 1
        if reach < best:
            best, centre = reach, (a, b)
    tree = bfs(list(centre))[1]
    if len(centre) > 1:
        tree.append(centre)
    print("\n".join("%d %d" % (a + 1, b + 1) for a, b in tree))


main()
