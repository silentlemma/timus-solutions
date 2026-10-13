import sys
from array import array

EDGE_FIELDS = 3  # u v w


def main():
    # all numbers go into flat arrays at once, so that the words of the
    # input are freed before the tables are built
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    after = 1 + EDGE_FIELDS * (n - 1)
    us, vs, ws = (
        array("i", map(int, data[1 + k : after : EDGE_FIELDS])) for k in range(EDGE_FIELDS)
    )
    m = int(data[after])
    queries = array("i", map(int, data[after + 1 : after + 1 + 2 * m]))
    del data

    # adjacency lists packed into one array (both directions of each edge)
    start = [0] * (n + 1)
    for u in us:
        start[u + 1] += 1
    for v in vs:
        start[v + 1] += 1
    for i in range(n):
        start[i + 1] += start[i]
    fill = start[:]
    adj = [0] * (2 * (n - 1))
    weight = [0] * (2 * (n - 1))
    for u, v, w in zip(us, vs, ws):
        adj[fill[u]] = v
        weight[fill[u]] = w
        fill[u] += 1
        adj[fill[v]] = u
        weight[fill[v]] = w
        fill[v] += 1

    # Euler tour from vertex 0: a vertex is written on entry and after each child
    parent = [-1] * n
    depth = [0] * n
    dist = [0] * n
    first = [0] * n
    tour = [0]
    pointer = start[:n]
    stack = [0]
    while stack:
        v = stack[-1]
        p = pointer[v]
        if p < start[v + 1]:
            pointer[v] = p + 1
            u = adj[p]
            if u == parent[v]:
                continue
            parent[u] = v
            depth[u] = depth[v] + 1
            dist[u] = dist[v] + weight[p]
            first[u] = len(tour)
            tour.append(u)
            stack.append(u)
        else:
            stack.pop()
            if stack:
                tour.append(stack[-1])

    # sparse table of minima over keys depth * n + vertex, in flat integer
    # rows: rows of Python integers would not fit in the memory limit
    level = array("q", [depth[v] * n + v for v in tour])
    table = [level]
    span = 1
    while 2 * span <= len(tour):
        prev = table[-1]
        level = array("q", [a if a < b else b for a, b in zip(prev, prev[span:])])
        table.append(level)
        span *= 2

    out = []
    for i in range(0, 2 * m, 2):
        a, b = queries[i], queries[i + 1]
        lo, hi = first[a], first[b]
        if lo > hi:
            lo, hi = hi, lo
        k = (hi - lo + 1).bit_length() - 1
        row = table[k]
        x, y = row[lo], row[hi - (1 << k) + 1]
        lca = (x if x < y else y) % n
        out.append(dist[a] + dist[b] - 2 * dist[lca])
    sys.stdout.write("".join("%d\n" % d for d in out))


main()
