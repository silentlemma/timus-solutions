import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    pos = 2
    for _ in range(n - 1):
        a, b = int(data[pos]), int(data[pos + 1])
        pos += 2
        adj[a].append(b)
        adj[b].append(a)
    asks = [[] for _ in range(n + 1)]
    dist = [0] * q
    for i in range(q):
        asks[int(data[pos])].append(i)
        dist[i] = int(data[pos + 1])
        pos += 2
    answer = [0] * q
    path = [0] * (n + 1)

    # walk the tree from root in preorder: when a vertex is reached, path
    # holds its ancestors by depth, so a query at it with d <= depth is
    # answered at once; returns the deepest vertex
    def walk(root):
        depth = [-1] * (n + 1)
        depth[root] = 0
        deepest = root
        stack = [root]
        while stack:
            v = stack.pop()
            dv = depth[v]
            path[dv] = v
            if dv > depth[deepest]:
                deepest = v
            for i in asks[v]:
                if answer[i] == 0 and dist[i] <= dv:
                    answer[i] = path[dv - dist[i]]
            for u in adj[v]:
                if depth[u] < 0:
                    depth[u] = dv + 1
                    stack.append(u)
        return deepest

    # the farthest vertex from any vertex is an end of a diameter, and the
    # walk from vertex 1 ends at one end, the walk from there at the other
    a = walk(1)
    b = walk(a)
    walk(b)
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


main()
