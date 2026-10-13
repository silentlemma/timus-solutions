"""Checker: "NO" exactly when the reference says so; otherwise "YES" and
an N by N matrix of integers from 0 to 100 with the given row and column
sums."""

import sys

CAP = 100


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    rows = list(map(int, data[1 : 1 + n]))
    cols = list(map(int, data[1 + n : 1 + 2 * n]))
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if not got:
        fail("empty output")
    if got[0] != want:
        fail("expected %s, got %s" % (want, got[0]))
    if want == "NO":
        if len(got) != 1:
            fail("nothing may follow NO")
        return
    if len(got) != 1 + n * n:
        fail("expected %d numbers after YES" % (n * n))
    cells = [int(x) for x in got[1:]]
    if any(not 0 <= x <= CAP for x in cells):
        fail("a credit outside 0..100")
    matrix = [cells[i * n : (i + 1) * n] for i in range(n)]
    if [sum(r) for r in matrix] != rows:
        fail("row sums differ")
    if [sum(matrix[i][j] for i in range(n)) for j in range(n)] != cols:
        fail("column sums differ")


main()
