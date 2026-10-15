import sys

HEADER = 4  # n, m, s, t


def reach(start, adj, alive):
    seen = [False] * len(adj)
    seen[start] = True
    stack = [start]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if alive[u] and not seen[u]:
                seen[u] = True
                stack.append(u)
    return seen


def main():
    data = sys.stdin.buffer.read().split()
    n, m, s, t = (int(w) for w in data[:HEADER])
    s, t = s - 1, t - 1
    ends = [int(w) - 1 for w in data[HEADER:HEADER + 2 * m]]
    edges = list(zip(ends[::2], ends[1::2]))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        radj[b].append(a)
    # only vertices on some path from s to t matter; they form whole
    # strongly connected components
    every = [True] * n
    from_s = reach(s, adj, every)
    if not from_s[t]:
        print(0)
        return
    to_t = reach(t, radj, every)
    alive = [from_s[v] and to_t[v] for v in range(n)]
    # Kosaraju: finishing order on the graph, then the reversed graph in
    # reverse finishing order numbers the components in topological order
    order = []
    done = [False] * n
    for root in range(n):
        if not alive[root] or done[root]:
            continue
        done[root] = True
        stack = [(root, 0)]
        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                stack[-1] = (v, i + 1)
                u = adj[v][i]
                if alive[u] and not done[u]:
                    done[u] = True
                    stack.append((u, 0))
            else:
                stack.pop()
                order.append(v)
    comp = [-1] * n
    count = 0
    for root in reversed(order):
        if comp[root] >= 0:
            continue
        comp[root] = count
        stack = [root]
        while stack:
            v = stack.pop()
            for u in radj[v]:
                if alive[u] and comp[u] < 0:
                    comp[u] = count
                    stack.append(u)
        count += 1
    size = [0] * count
    inside = [0] * count
    for v in range(n):
        if alive[v]:
            size[comp[v]] += 1
    out = [[] for _ in range(count)]
    for a, b in edges:
        if alive[a] and alive[b]:
            if comp[a] == comp[b]:
                inside[comp[a]] += 1
            else:
                out[comp[a]].append(comp[b])
    # a component with more arcs than vertices holds two cycles, and paths grow
    # exponentially; otherwise each cyclic component is one simple cycle, and
    # paths through c of them number about N^(c - 1)
    if any(inside[c] > size[c] for c in range(count)):
        print(-1)
        return
    # best[c]: the most cycles on a path from s into component c; arcs go
    # from lower to higher numbers, so one pass in order settles it
    best = [0] * count
    for c in range(count):
        best[c] += 1 if inside[c] == size[c] else 0
        for d in out[c]:
            best[d] = max(best[d], best[c])
    print(max(0, best[comp[t]] - 1))


main()
