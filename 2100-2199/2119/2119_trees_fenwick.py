import sys

EDGE_FIELDS = 3  # u, v and the weight


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    head = [-1] * (n + 1)
    nxt = [0] * (2 * n)
    to = [0] * (2 * n)
    wt = [0] * (2 * n)
    pos = 1
    for e in range(0, 2 * (n - 1), 2):
        u, v, w = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        pos += EDGE_FIELDS
        to[e], wt[e], nxt[e], head[u] = v, w, head[u], e
        to[e + 1], wt[e + 1], nxt[e + 1], head[v] = u, w, head[v], e + 1

    tin = [0] * (n + 1)
    parent = [1] * (n + 1)
    depth = [0] * (n + 1)
    order = []
    stack = [1]
    while stack:
        v = stack.pop()
        tin[v] = len(order)
        order.append(v)
        e = head[v]
        while e >= 0:
            u = to[e]
            if u != parent[v]:
                parent[u] = v
                depth[u] = depth[v] + wt[e]
                stack.append(u)
            e = nxt[e]

    # The LCA of u != v is the parent with the smallest preorder number among
    # the vertices in the preorder range (tin[u], tin[v]].
    table = [[tin[parent[v]] for v in order]]
    span = 1
    while span * 2 <= n:
        prev = table[-1]
        table.append([a if a < b else b for a, b in zip(prev, prev[span:])])
        span *= 2
    lg = [0] * (n + 1)
    for i in range(2, n + 1):
        lg[i] = lg[i >> 1] + 1

    def dist(u, v):
        if u == v:
            return 0
        lo, hi = tin[u], tin[v]
        if lo > hi:
            lo, hi = hi, lo
        lo += 1
        k = lg[hi - lo + 1]
        row = table[k]
        x, y = row[lo], row[hi - (1 << k) + 1]
        return depth[u] + depth[v] - 2 * depth[order[x if x < y else y]]

    fen = [0] * (n + 1)
    top = 1 << lg[n]

    def kth(k):
        p = 0
        step = top
        while step:
            if p + step <= n and fen[p + step] < k:
                p += step
                k -= fen[p]
            step >>= 1
        return order[p]

    q = int(data[pos])
    pos += 1
    total = 0
    doubled = 0  # the sum of distances around the marked vertices in preorder
    out = []
    for _ in range(q):
        adding = data[pos] == b"+"
        v = int(data[pos + 1])
        pos += 2
        p = tin[v]
        if not adding:
            i = p + 1
            while i <= n:
                fen[i] -= 1
                i += i & -i
            total -= 1
        if total:
            before = 0
            i = p
            while i:
                before += fen[i]
                i -= i & -i
            a = kth(before if before else total)
            b = kth(before + 1 if before < total else 1)
            change = dist(a, v) + dist(v, b) - dist(a, b)
            doubled += change if adding else -change
        if adding:
            i = p + 1
            while i <= n:
                fen[i] += 1
                i += i & -i
            total += 1
        out.append(doubled >> 1)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
