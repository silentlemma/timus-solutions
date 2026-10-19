import sys
from collections import deque

LONGEST = 50  # experience is from 1 to 50 years


def distances(adj, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def main():
    v = list(map(int, sys.stdin.read().split()))
    n, p = v[0], v[1]
    adj = [[] for _ in range(p + 1)]
    pairs = iter(v[2:])
    for a, b in zip(pairs, pairs):
        adj[a].append(b)
        adj[b].append(a)
    # the two pilots of a flight differ by exactly one year, so a component
    # must be bipartite; within it no two pilots differ by more than their
    # distance, and BFS layers from one end of a diameter reach it
    comps, seen = [], [False] * (p + 1)
    for s in range(1, p + 1):
        if not seen[s]:
            dist = distances(adj, s)
            if any((dist[a] - dist[b]) % 2 == 0 for a in dist for b in adj[a]):
                print(-1)
                return
            for u in dist:
                seen[u] = True
            comps.append(list(dist))
    years = [0] * (p + 1)
    if len(comps) == 1:
        best = max((distances(adj, s) for s in comps[0]), key=lambda d: max(d.values()))
        for u, d in best.items():
            years[u] = 1 + d
        print(max(best.values()))
    else:
        # separate groups: one alternates 1 and 2, the others 49 and 50
        for k, comp in enumerate(comps):
            for u, d in distances(adj, comp[0]).items():
                years[u] = 1 + d % 2 if k == 0 else LONGEST - d % 2
        print(LONGEST - 1)
    print(*years[1:])


main()
