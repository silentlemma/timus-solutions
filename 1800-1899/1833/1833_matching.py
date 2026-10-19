import sys
from collections import deque


def max_matching(n, adj):
    # Hopcroft-Karp on the doubled graph: left copies 0 .. n - 1, right
    # copies 0 .. n - 1, adj[u] the right neighbours of left u
    match_left = [-1] * n
    match_right = [-1] * n
    while True:
        dist = [-1] * n
        queue = deque(u for u in range(n) if match_left[u] < 0)
        for u in queue:
            dist[u] = 0
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = match_right[v]
                if w < 0:
                    found = True
                elif dist[w] < 0:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        if not found:
            return match_left, match_right
        it = [0] * n
        for root in range(n):
            if match_left[root] >= 0:
                continue
            # iterative augmenting search along the BFS layers
            path = [root]
            while path:
                u = path[-1]
                if it[u] == len(adj[u]):
                    dist[u] = -1
                    path.pop()
                    continue
                v = adj[u][it[u]]
                it[u] += 1
                w = match_right[v]
                if w < 0:
                    # flip the matching along the path
                    for x in reversed(path):
                        match_left[x], v = v, match_left[x]
                        match_right[match_left[x]] = x
                    break
                if dist[w] == dist[u] + 1:
                    path.append(w)


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n, k, m = next(data), next(data), next(data)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(data) - 1, next(data) - 1
        adj[a].append(b)
        adj[b].append(a)
    # each crew must get at least k between its two members; this linear
    # program has a half-integral optimum, k/2 for each copy of a canoeist
    # in a minimum vertex cover of the doubled bipartite graph
    match_left, match_right = max_matching(n, adj)
    # Konig: left copies unreachable from free left copies by alternating
    # paths, and right copies reachable, form a minimum cover
    seen_left = [False] * n
    seen_right = [False] * n
    queue = deque(u for u in range(n) if match_left[u] < 0)
    for u in queue:
        seen_left[u] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not seen_right[v]:
                seen_right[v] = True
                w = match_right[v]
                if w >= 0 and not seen_left[w]:
                    seen_left[w] = True
                    queue.append(w)
    out = []
    for v in range(n):
        copies = (not seen_left[v]) + seen_right[v]
        out.append(f"{copies * k / 2:.1f}")
    print("\n".join(out))


main()
