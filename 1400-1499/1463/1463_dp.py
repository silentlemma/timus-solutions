import sys

FIELDS = 3  # a link: two cities and its joy


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    joy = [0] + [int(x) for x in data[2 : 2 + n]]
    links = data[2 + n :]
    adj = [[] for _ in range(n + 1)]
    for i in range(k):
        a, b, c = (int(x) for x in links[FIELDS * i : FIELDS * (i + 1)])
        adj[a].append((b, c))
        adj[b].append((a, c))
    # down[v]: the best route that starts at v and goes away from its parent,
    # nxt[v] the next city on it; the routes are in a forest, so each tree once
    down, nxt = joy[:], [0] * (n + 1)
    parent = [-1] * (n + 1)
    best, ends = -1, None
    for root in range(1, n + 1):
        if parent[root] != -1:
            continue
        parent[root] = 0
        order, stack = [], [root]
        while stack:
            v = stack.pop()
            order.append(v)
            for w, _ in adj[v]:
                if parent[w] == -1:
                    parent[w] = v
                    stack.append(w)
        for v in reversed(order):
            first = second = (0, 0)  # (value through a child, the child)
            for w, c in adj[v]:
                if w != parent[v]:
                    option = (c + down[w], w)
                    if option > first:
                        first, second = option, first
                    elif option > second:
                        second = option
            down[v], nxt[v] = joy[v] + first[0], first[1]
            if joy[v] + first[0] + second[0] > best:
                best, ends = joy[v] + first[0] + second[0], (v, first[1], second[1])
    v, a, b = ends
    left, right = [], []
    while a:
        left.append(a)
        a = nxt[a]
    while b:
        right.append(b)
        b = nxt[b]
    route = left[::-1] + [v] + right
    print(best)
    print(len(route))
    print(" ".join(map(str, route)))


main()
