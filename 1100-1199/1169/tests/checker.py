"""Checker: -1 exactly when the stored answer is -1; otherwise distinct
connections between distinct computers that join all N of them and have
exactly K critical pairs, counted through the bridges of the network."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def bridge_parts(n, edges):
    # sizes of the parts left when every bridge is removed, by lowlinks
    adj = [[] for _ in range(n + 1)]
    for idx, (a, b) in enumerate(edges):
        adj[a].append((b, idx))
        adj[b].append((a, idx))
    order, low = [0] * (n + 1), [0] * (n + 1)
    bridges = set()
    counter = 1
    order[1] = low[1] = counter
    stack = [(1, -1, iter(adj[1]))]
    while stack:
        v, via, it = stack[-1]
        for u, idx in it:
            if idx == via:
                continue
            if order[u]:
                low[v] = min(low[v], order[u])
            else:
                counter += 1
                order[u] = low[u] = counter
                stack.append((u, idx, iter(adj[u])))
                break
        else:
            stack.pop()
            if stack:
                parent = stack[-1][0]
                low[parent] = min(low[parent], low[v])
                if low[v] > order[parent]:
                    bridges.add(via)
    if 0 in order[1:]:
        fail("the network is not connected")
    seen = [False] * (n + 1)
    sizes = []
    for start in range(1, n + 1):
        if not seen[start]:
            seen[start] = True
            todo, size = [start], 0
            while todo:
                v = todo.pop()
                size += 1
                for u, idx in adj[v]:
                    if idx not in bridges and not seen[u]:
                        seen[u] = True
                        todo.append(u)
            sizes.append(size)
    return sizes


def main():
    inp, ans, output = sys.argv[1:4]
    n, k = map(int, open(inp).read().split())
    want_none = open(ans).read().split() == ["-1"]
    got = open(output).read().split()
    if want_none or got == ["-1"]:
        if got != ["-1"] or not want_none:
            fail("expected %s" % ("-1" if want_none else "a network"))
        return
    try:
        nums = [int(x) for x in got]
    except ValueError:
        fail("not numbers")
    if len(nums) % 2:
        fail("an odd number of values")
    edges = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
    if any(not (1 <= a <= n and 1 <= b <= n) or a == b for a, b in edges):
        fail("a connection with a bad computer")
    if len({(min(a, b), max(a, b)) for a, b in edges}) != len(edges):
        fail("a connection made twice")
    sizes = bridge_parts(n, edges)
    critical = n * (n - 1) // 2 - sum(s * (s - 1) // 2 for s in sizes)
    if critical != k:
        fail("%d critical pairs instead of %d" % (critical, k))


if __name__ == "__main__":
    main()
