"""Checker: one answer per query, 0 exactly when the expected answer is 0,
and otherwise a vertex at the asked distance from the query vertex."""

import sys
from collections import deque


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n, q = int(words[0]), int(words[1])
    adj = [[] for _ in range(n + 1)]
    pos = 2
    for _ in range(n - 1):
        a, b = int(words[pos]), int(words[pos + 1])
        pos += 2
        adj[a].append(b)
        adj[b].append(a)
    # depths and ancestors from vertex 1 give distances through the lowest
    # common ancestor, found by climbing in powers of two
    depth = [-1] * (n + 1)
    parent = [0] * (n + 1)
    depth[1] = 0
    order = deque([1])
    while order:
        v = order.popleft()
        for u in adj[v]:
            if depth[u] < 0:
                depth[u] = depth[v] + 1
                parent[u] = v
                order.append(u)
    up = [parent]
    while (1 << len(up)) <= n:
        last = up[-1]
        up.append([last[last[v]] for v in range(n + 1)])

    def distance(a, b):
        da, db = depth[a], depth[b]
        if da < db:
            a, b = b, a
        gap = abs(da - db)
        for k, level in enumerate(up):
            if gap >> k & 1:
                a = level[a]
        if a != b:
            for level in reversed(up):
                if level[a] != level[b]:
                    a, b = level[a], level[b]
            a = parent[a]
        return da + db - 2 * depth[a]

    want = open(expected).read().split()
    got = open(output).read().split()
    if len(got) != q:
        raise Bad("expected %d answers, got %d" % (q, len(got)))
    for i in range(q):
        v, d = int(words[pos]), int(words[pos + 1])
        pos += 2
        if not got[i].isdigit() or int(got[i]) > n:
            raise Bad("answer %d is not a vertex or 0" % (i + 1))
        u = int(got[i])
        if want[i] == "0":
            if u != 0:
                raise Bad("query %d has no answer, expected 0" % (i + 1))
        elif u == 0 or distance(u, v) != d:
            raise Bad("query %d: vertex %s is not at distance %d" % (i + 1, got[i], d))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
