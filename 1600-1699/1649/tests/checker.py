"""Checker: No exactly when expected; otherwise every cell settled once and
the settling gives the picture."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n, m = int(data[0]), int(data[1])
    want = [int(w) for w in data[2 : 2 + n * m]]
    expect = open(expected).read().split()
    got = open(output).read().split()
    if not got or got[0] not in ("Yes", "No"):
        fail("expected Yes or No")
    if expect[0] == "No" or got[0] == "No":
        if got[0] != expect[0]:
            fail("expected %s" % expect[0])
        return
    if len(got) != 1 + 2 * n * m or not all(w.isdigit() for w in got[1:]):
        fail("expected %d cells" % (n * m))
    count = [0] * (n * m)
    for k in range(n * m):
        r, c = int(got[1 + 2 * k]) - 1, int(got[2 + 2 * k]) - 1
        if not (0 <= r < n and 0 <= c < m):
            fail("cell %d %d is off the canvas" % (r + 1, c + 1))
        if count[r * m + c]:
            fail("cell %d %d is settled twice" % (r + 1, c + 1))
        count[r * m + c] = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and count[nr * m + nc]:
                count[nr * m + nc] = count[nr * m + nc] % 4 + 1
    for v in range(n * m):
        if count[v] != want[v]:
            fail("cell %d %d ends with %d, the picture has %d" % (v // m + 1, v % m + 1, count[v], want[v]))


main()
