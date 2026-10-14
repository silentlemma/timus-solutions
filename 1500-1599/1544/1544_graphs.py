import sys
from collections import deque


def main():
    words = iter(sys.stdin.read().split())
    n, m = int(next(words)), int(next(words))
    protocol = [next(words) for _ in range(n)]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = int(next(words)) - 1, int(next(words)) - 1
        adj[a].append(b)
        adj[b].append(a)
    # glue neighbours with the same protocol into regions
    region = [-1] * n
    regions = 0
    for s in range(n):
        if region[s] < 0:
            region[s] = regions
            stack = [s]
            while stack:
                v = stack.pop()
                for u in adj[v]:
                    if region[u] < 0 and protocol[u] == protocol[v]:
                        region[u] = regions
                        stack.append(u)
            regions += 1
    near = [set() for _ in range(regions)]
    for v in range(n):
        for u in adj[v]:
            if region[u] != region[v]:
                near[region[v]].add(region[u])
    # switching a region merges it with all its neighbours, so switching the
    # same region again and again takes its eccentricity in steps, and no
    # plan does better than the radius of the region graph
    best, centre = regions, 0
    for start in range(regions):
        dist = [-1] * regions
        dist[start] = 0
        queue = deque([start])
        while queue:
            r = queue.popleft()
            for q in near[r]:
                if dist[q] < 0:
                    dist[q] = dist[r] + 1
                    queue.append(q)
        if max(dist) < best:
            best, centre = max(dist), start
    computer = region.index(centre)
    current = protocol[computer]
    out = [str(best)]
    for _ in range(best):
        current = "E" if current == "J" else "J"
        out.append("%d %s" % (computer + 1, current))
    print("\n".join(out))


main()
