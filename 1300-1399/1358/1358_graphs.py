import sys

STEP = 2  # columns two apart keep every pair of points farther than 1
LIMIT = 999  # the leftmost column, so that 1000 columns fit in [-999, 999]


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        adj[a].append(b)
        adj[b].append(a)
    # column = preorder index, row = depth: the subtrees of the vertices on
    # one row take disjoint ranges of columns, so no two wires cross
    x, y = [0] * (n + 1), [0] * (n + 1)
    seen = [False] * (n + 1)
    seen[1] = True
    stack, order = [1], 0
    while stack:
        v = stack.pop()
        x[v] = order * STEP - LIMIT
        order += 1
        for u in reversed(adj[v]):
            if not seen[u]:
                seen[u] = True
                y[u] = y[v] + 1
                stack.append(u)
    print("\n".join("%d %d" % (x[v], y[v]) for v in range(1, n + 1)))


main()
