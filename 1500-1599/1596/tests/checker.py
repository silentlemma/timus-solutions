"""Checker: "No solution" exactly when N·M is odd; otherwise N rows of M
directions from 1 to 8 that, followed from the top left cell, visit every
cell once and come back to it."""

import sys

MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    n, m = (int(x) for x in open(source).read().split())
    got = open(output).read().split()
    if n * m % 2:
        if got != ["No", "solution"]:
            fail("expected No solution")
        return
    if len(got) != n * m or not all(w in "12345678" and len(w) == 1 for w in got):
        fail("expected %d directions from 1 to 8" % (n * m))
    step = [int(w) - 1 for w in got]
    seen = bytearray(n * m)
    r = c = 0
    for _ in range(n * m):
        cell = r * m + c
        if seen[cell]:
            fail("cell (%d, %d) is visited twice" % (r + 1, c + 1))
        seen[cell] = 1
        dr, dc = MOVES[step[cell]]
        r, c = r + dr, c + dc
        if not (0 <= r < n and 0 <= c < m):
            fail("the knight leaves the board")
    if (r, c) != (0, 0):
        fail("the tour does not come back to the start")


main()
