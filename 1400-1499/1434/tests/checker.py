"""Checker: -1 exactly when the reference prints -1; otherwise the same
smallest number of rides and a list of that many plus one stops from A
to B in which every two neighbours lie on a common route."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    pos = 2
    on_stop = {}
    for r in range(n):
        k = int(data[pos])
        for st in data[pos + 1 : pos + 1 + k]:
            on_stop.setdefault(int(st), set()).add(r)
        pos += 1 + k
    a, b = int(data[pos]), int(data[pos + 1])
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got:
        fail("empty output")
    if int(got[0]) != want:
        fail("cost %s, expected %d" % (got[0], want))
    if want == -1:
        if len(got) != 1:
            fail("nothing may follow -1")
        return
    path = [int(x) for x in got[1:]]
    if len(path) != want + 1:
        fail("expected %d stops on the route" % (want + 1))
    if path[0] != a or path[-1] != b:
        fail("the route must go from A to B")
    for u, v in zip(path, path[1:]):
        if not on_stop.get(u, set()) & on_stop.get(v, set()):
            fail("no bus goes from %d to %d" % (u, v))


main()
