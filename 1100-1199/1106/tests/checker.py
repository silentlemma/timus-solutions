"""Checker: the first team is a set of distinct members given with its size,
and every member, in the first team or not, has a friend on the other side.
Every member has a friend, so a split always exists and 0 is never
accepted."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n = next(tok)
    adj = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        adj[v] = list(iter(lambda: next(tok), 0))
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if not got or got[0] != len(got) - 1 or got[0] == 0:
        fail("a non-empty first team with its size is expected")
    team = set(got[1:])
    if len(team) != got[0] or not all(1 <= v <= n for v in team):
        fail("members must be distinct and in range")
    for v in range(1, n + 1):
        if not any((u in team) != (v in team) for u in adj[v]):
            fail("member %d has no friend in the other team" % v)


main()
