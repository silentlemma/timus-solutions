"""Checker: "Impossible" exactly when the reference says so; otherwise a
results table (0 on the diagonal, each match 3-0, 0-3 or 1-1) under which
every captain's statements are either all true or all false."""

import sys

RESULTS = {(3, 0), (0, 3), (1, 1)}


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n = data[0]
    said = [data[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["Impossible"]:
        if got != ["Impossible"]:
            fail("expected Impossible")
        return
    if got == ["Impossible"]:
        fail("a tournament exists")
    if len(got) != n * n:
        fail("expected an %d x %d table" % (n, n))
    try:
        table = [[int(got[i * n + j]) for j in range(n)] for i in range(n)]
    except ValueError:
        fail("not integers")
    for i in range(n):
        if table[i][i] != 0:
            fail("row %d: a team does not play itself" % (i + 1))
        for j in range(i + 1, n):
            if (table[i][j], table[j][i]) not in RESULTS:
                fail("teams %d and %d: impossible result" % (i + 1, j + 1))
    for i in range(n):
        truths = {(said[i][j] == 1) == (table[i][j] > 0) for j in range(n) if said[i][j] >= 0}
        if len(truths) > 1:
            fail("captain %d both lies and tells the truth" % (i + 1))


main()
