import sys


def main():
    words = map(int, sys.stdin.buffer.read().split())
    n, m, root = next(words), next(words), next(words)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        path = [next(words) for _ in range(next(words))]
        for a, b in zip(path, path[1:]):
            adj[a].append(b)
            adj[b].append(a)
    # depth-first search without recursion, so every other edge joins a
    # vertex to one of its ancestors
    parent = [0] * (n + 1)
    depth = [-1] * (n + 1)
    nxt = [0] * (n + 1)  # the next neighbour to look at
    order = [root]
    depth[root] = 0
    stack = [root]
    while stack:
        v = stack[-1]
        if nxt[v] == len(adj[v]):
            stack.pop()
            continue
        u = adj[v][nxt[v]]
        nxt[v] += 1
        if depth[u] < 0:
            depth[u] = depth[v] + 1
            parent[u] = v
            order.append(u)
            stack.append(u)
    # every non-tree edge closes a cycle with the tree path between its ends
    on_cycle = [False] * (n + 1)  # the edge from v to its parent lies on a cycle
    cycles = [[] for _ in range(n + 1)]  # cycles listed at their top vertex
    for v in range(1, n + 1):
        for u in adj[v]:
            if depth[u] < depth[v] and u != parent[v]:
                members, x = [], v
                while x != u:
                    on_cycle[x] = True
                    members.append(x)
                    x = parent[x]
                cycles[u].append(members)
    # a tree edge to a child of value g is worth g + 1; a cycle fuses into
    # loops on its top vertex: one loop (worth 1) per edge, so its length
    # parity, together with everything hanging from its other vertices
    value = [0] * (n + 1)
    for v in reversed(order):
        g = 0
        for u in adj[v]:
            if parent[u] == v and not on_cycle[u]:
                g ^= value[u] + 1
        for members in cycles[v]:
            g ^= (len(members) + 1) % 2  # a cycle has as many edges as vertices
            for x in members:
                g ^= value[x]
        value[v] = g
    print("First" if value[root] else "Second")


main()
