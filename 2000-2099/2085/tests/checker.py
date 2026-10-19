"""Checker: "No solution" exactly when the expected output says so; otherwise
two projects whose path in the tree uses every technology exactly once."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, m = data[0], data[1]
    pos = 2
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = data[pos], data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    techs = [None]
    for _ in range(n):
        a = data[pos]
        techs.append(data[pos + 1:pos + 1 + a])
        pos += 1 + a
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[0] == "No":
        if got != ["No", "solution"]:
            raise Bad("expected No solution")
        return
    if len(got) != 2 or not all(w.isdigit() for w in got):
        raise Bad("expected two projects")
    s, t = int(got[0]), int(got[1])
    if not (1 <= s <= n and 1 <= t <= n):
        raise Bad("no such project")
    parent = [0] * (n + 1)
    parent[s] = -1
    stack = [s]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                stack.append(u)
    used = [0] * (m + 1)
    v = t
    while v != -1:
        for x in techs[v]:
            used[x] += 1
        v = parent[v]
    if any(c != 1 for c in used[1:]):
        raise Bad("the path does not use every technology exactly once")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
