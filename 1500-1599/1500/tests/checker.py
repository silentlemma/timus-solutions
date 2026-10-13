"""Checker: the number of permits must be the expected smallest one, the
categories different and valid, and their roads must lead from crossing
0 to crossing 1."""

import sys

FIELDS = 3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    k, m = data[0], data[2]
    roads = [tuple(data[3 + FIELDS * i : 3 + FIELDS * (i + 1)]) for i in range(m)]
    want = int(open(expected).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("not integers")
    if not got or got[0] != want:
        fail("expected %d permits" % want)
    chosen = got[1:]
    if len(chosen) != want or len(set(chosen)) != want:
        fail("expected %d different categories" % want)
    if any(not 0 <= c < k for c in chosen):
        fail("no such category")
    allowed = set(chosen)
    seen, stack = {0}, [0]
    while stack:
        u = stack.pop()
        for a, b, c in roads:
            if c in allowed and u in (a, b):
                v = b if u == a else a
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
    if 1 not in seen:
        fail("the categories do not lead from 0 to 1")


main()
