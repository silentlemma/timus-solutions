import sys


def main():
    words = iter(sys.stdin.buffer.read().split())
    n = int(next(words))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = int(next(words)), int(next(words))
        adj[a].append(b)
        adj[b].append(a)
    # heavy-light decomposition: every cave's heavy child continues its chain,
    # and the chains lie consecutively in one segment tree of maxima
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                depth[u] = depth[v] + 1
                order.append(u)
    size = [1] * (n + 1)
    heavy = [0] * (n + 1)
    for v in reversed(order):
        p = parent[v]
        if p > 0:
            size[p] += size[v]
            if heavy[p] == 0 or size[v] > size[heavy[p]]:
                heavy[p] = v
    head = [0] * (n + 1)
    index = [0] * (n + 1)
    nxt = 0
    for v in order:
        if v == 1 or heavy[parent[v]] != v:
            u = v
            while u:
                head[u] = v
                index[u] = nxt
                nxt += 1
                u = heavy[u]
    width = 1
    while width < n:
        width *= 2
    tree = [0] * (2 * width)

    def seg_max(lo, hi):
        """The largest level at the places lo to hi of the chains."""
        best = 0
        lo += width
        hi += width + 1
        while lo < hi:
            if lo & 1:
                best = max(best, tree[lo])
                lo += 1
            if hi & 1:
                hi -= 1
                best = max(best, tree[hi])
            lo >>= 1
            hi >>= 1
        return best

    out = []
    q = int(next(words))
    for _ in range(q):
        kind, u, v = next(words), int(next(words)), int(next(words))
        if kind == b"I":
            i = index[u] + width
            tree[i] += v
            i >>= 1
            while i:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i >>= 1
            continue
        best = 0
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            best = max(best, seg_max(index[head[u]], index[u]))
            u = parent[head[u]]
        lo, hi = sorted((index[u], index[v]))
        best = max(best, seg_max(lo, hi))
        out.append(best)
    sys.stdout.write("".join("%d\n" % x for x in out))


main()
