"""Checker: the number of requests must equal the expected minimum, and
carrying them out must leave every computer with the same protocol."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n, m = int(data[0]), int(data[1])
    protocol = data[2 : 2 + n]
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = int(data[2 + n + 2 * i]) - 1, int(data[3 + n + 2 * i]) - 1
        adj[a].append(b)
        adj[b].append(a)
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not got[0].isdigit() or int(got[0]) != want:
        fail("got %s requests, expected %d" % (got[:1], want))
    if len(got) != 1 + 2 * want:
        fail("expected %d requests" % want)
    for r in range(want):
        who, to = got[1 + 2 * r], got[2 + 2 * r]
        if not who.isdigit() or not 1 <= int(who) <= n or to not in ("E", "J"):
            fail("bad request %s %s" % (who, to))
        v = int(who) - 1
        old = protocol[v]
        if old == to:
            continue
        # the command spreads through the computers on the old protocol
        stack, seen = [v], {v}
        while stack:
            x = stack.pop()
            protocol[x] = to
            for u in adj[x]:
                if u not in seen and protocol[u] == old:
                    seen.add(u)
                    stack.append(u)
    if len(set(protocol)) != 1:
        fail("the protocols still differ")


main()
