import sys
from collections import deque


def max_matching(adj, n):
    """Hopcroft-Karp: BFS layers from the free left vertices, then
    vertex-disjoint shortest augmenting paths found by an iterative DFS."""
    m = len(adj)
    match_l, match_r = [-1] * m, [-1] * n
    for v in range(m):
        for u in adj[v]:
            if match_r[u] < 0:
                match_l[v], match_r[u] = u, v
                break
    while True:
        dist = [-1] * m
        queue = deque(v for v in range(m) if match_l[v] < 0)
        for v in queue:
            dist[v] = 0
        found = False
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                w = match_r[u]
                if w < 0:
                    found = True
                elif dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        if not found:
            return sum(1 for u in match_l if u >= 0)
        it = [0] * m
        for root in range(m):
            if match_l[root] >= 0:
                continue
            path = [root]
            while path:
                v = path[-1]
                if it[v] == len(adj[v]):
                    dist[v] = -1
                    path.pop()
                    continue
                u = adj[v][it[v]]
                it[v] += 1
                w = match_r[u]
                if w < 0:
                    # flip the path: every left vertex on it takes its next edge
                    for x in reversed(path):
                        y = adj[x][it[x] - 1]
                        match_l[x], match_r[y] = y, x
                    break
                if dist[w] == dist[v] + 1:
                    path.append(w)


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    m, n, k = next(tok), next(tok), next(tok)
    adj = [[] for _ in range(m)]
    for _ in range(k):
        a, b = next(tok), next(tok)
        adj[a - 1].append(b - 1)
    # a minimum edge cover takes a maximum matching and one more edge for
    # every vertex the matching leaves uncovered
    print(m + n - max_matching(adj, n))


main()
