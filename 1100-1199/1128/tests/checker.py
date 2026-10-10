"""Checker: a group of distinct children with its size, which is the
smaller part of the split (or, at equal sizes, the part with child 1), and
every child has at most one enemy in its own part. A split always exists,
so NO SOLUTION is rejected."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n = next(tok)
    enemies = [[next(tok) for _ in range(next(tok))] for _ in range(n)]
    text = open(output).read().split()
    if not text or not text[0].isdigit():
        fail("a split always exists")
    got = [int(x) for x in text]
    if got[0] != len(got) - 1:
        fail("the count does not match the children listed")
    group = set(got[1:])
    if len(group) != got[0] or not all(1 <= v <= n for v in group):
        fail("children must be distinct and in range")
    if 2 * len(group) > n or (2 * len(group) == n and 1 not in group):
        fail("the listed group is not the smaller one")
    for v in range(1, n + 1):
        same = sum((u in group) == (v in group) for u in enemies[v - 1])
        if same > 1:
            fail("child %d has %d enemies in its group" % (v, same))


main()
