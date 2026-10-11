import sys


def main():
    it = iter(map(int, sys.stdin.read().split()))
    m, n, s = next(it), next(it), next(it)
    parent = list(range(m + 1))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    adj = [[] for _ in range(m + 1)]
    for _ in range(n):
        p, q, r = next(it), next(it), next(it)
        a, b = find(p), find(q)
        if a == b:
            # a cycle, a loop or a second road: drive round it as long as needed
            print("YES")
            return
        parent[a] = b
        adj[p].append((q, r))
        adj[q].append((p, r))

    def farthest(start):
        dist = {start: 0}
        stack = [start]
        while stack:
            v = stack.pop()
            for u, r in adj[v]:
                if u not in dist:
                    dist[u] = dist[v] + r
                    stack.append(u)
        far = max(dist, key=dist.get)
        return far, dist[far], dist

    # a forest: the longest route is a diameter of one of its trees
    best, seen = 0, set()
    for v in range(1, m + 1):
        if v not in seen:
            end, _, part = farthest(v)
            seen.update(part)
            best = max(best, farthest(end)[1])
    print("YES" if best >= s else "NO")


main()
