import sys
from collections import deque


def main():
    tok = list(map(int, sys.stdin.buffer.read().split()))
    n = tok[0]
    adj = [set() for _ in range(n)]
    for a, b in zip(tok[1::2], tok[2::2]):
        if a != b and 1 <= a <= n and 1 <= b <= n:
            adj[a - 1].add(b - 1)
            adj[b - 1].add(a - 1)
    adj = [list(s) for s in adj]
    match = [-1] * n
    for v in range(n):
        if match[v] < 0:
            for u in adj[v]:
                if match[u] < 0:
                    match[u], match[v] = v, u
                    break

    def find_path(root):
        """Edmonds' search from an exposed vertex: an alternating tree whose
        odd cycles (blossoms) are shrunk into their base vertex."""
        used = [False] * n
        parent = [-1] * n
        base = list(range(n))
        used[root] = True
        queue = deque([root])

        def lca(a, b):
            seen = [False] * n
            while True:
                a = base[a]
                seen[a] = True
                if match[a] < 0:
                    break
                a = parent[match[a]]
            while True:
                b = base[b]
                if seen[b]:
                    return b
                b = parent[match[b]]

        def mark(v, b, child, blossom):
            while base[v] != b:
                blossom[base[v]] = blossom[base[match[v]]] = True
                parent[v] = child
                child = match[v]
                v = parent[match[v]]

        while queue:
            v = queue.popleft()
            for to in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] >= 0 and parent[match[to]] >= 0):
                    b = lca(v, to)
                    blossom = [False] * n
                    mark(v, b, to, blossom)
                    mark(to, b, v, blossom)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = b
                            if not used[i]:
                                used[i] = True
                                queue.append(i)
                elif parent[to] < 0:
                    parent[to] = v
                    if match[to] < 0:
                        return to, parent
                    used[match[to]] = True
                    queue.append(match[to])
        return -1, parent

    for root in range(n):
        if match[root] < 0 and adj[root]:
            v, parent = find_path(root)
            while v >= 0:
                pv = parent[v]
                nxt = match[pv]
                match[v], match[pv] = pv, v
                v = nxt
    pairs = [(v + 1, match[v] + 1) for v in range(n) if v < match[v]]
    out = [str(2 * len(pairs))] + ["%d %d" % p for p in pairs]
    sys.stdout.write("\n".join(out) + "\n")


main()
