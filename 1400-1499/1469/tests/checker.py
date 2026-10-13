"""Checker: "NO" exactly when the reference says so; otherwise "YES" and
two different cigarette numbers whose segments share a point."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def orient(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (v > 0) - (v < 0)


def on_box(a, b, c):
    inside_x = min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
    return inside_x and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])


def touch(p, q, r, s):
    o1, o2, o3, o4 = orient(p, q, r), orient(p, q, s), orient(r, s, p), orient(r, s, q)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    return (
        (o1 == 0 and on_box(p, q, r))
        or (o2 == 0 and on_box(p, q, s))
        or (o3 == 0 and on_box(r, s, p))
        or (o4 == 0 and on_box(r, s, q))
    )


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n = data[0]
    v = data[1:]
    seg = [((v[4 * i], v[4 * i + 1]), (v[4 * i + 2], v[4 * i + 3])) for i in range(n)]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if not got or got[0] != want:
        fail("expected %s" % want)
    if want == "NO":
        if len(got) != 1:
            fail("nothing may follow NO")
        return
    if len(got) != 3:
        fail("expected two numbers after YES")
    i, j = int(got[1]), int(got[2])
    if not (1 <= i <= n and 1 <= j <= n) or i == j:
        fail("two different cigarettes are needed")
    if not touch(seg[i - 1][0], seg[i - 1][1], seg[j - 1][0], seg[j - 1][1]):
        fail("cigarettes %d and %d do not meet" % (i, j))


main()
