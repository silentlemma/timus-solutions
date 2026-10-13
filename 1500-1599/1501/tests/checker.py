"""Checker: "Impossible" exactly when the reference says so; otherwise 2N
digits 1 and 2, N of each, such that after every move the red and the
black piles differ by at most one card."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    piles = [list(data[1]), list(data[2])]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["Impossible"]:
        if got != ["Impossible"]:
            fail("expected Impossible")
        return
    if got == ["Impossible"]:
        fail("an order exists")
    if len(got) != 1 or len(got[0]) != 2 * n or set(got[0]) - {"1", "2"}:
        fail("expected one line of %d digits 1 and 2" % (2 * n))
    taken = [0, 0]
    red = black = 0
    for move in got[0]:
        p = int(move) - 1
        if taken[p] == n:
            fail("pile %d is already empty" % (p + 1))
        if piles[p][taken[p]] == "1":
            red += 1
        else:
            black += 1
        taken[p] += 1
        if abs(red - black) > 1:
            fail("the piles differ by more than one card")


main()
