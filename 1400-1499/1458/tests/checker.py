"""Checker: the same number of commands as the reference, every command a
cell of the square, and after all commands every soldier stands the same
way."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    grid = data[1 : 1 + n]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or int(got[0]) != want:
        fail("expected %d commands" % want)
    cells = [int(x) for x in got[1:]]
    if len(cells) != 2 * want:
        fail("expected %d pairs of coordinates" % want)
    row, col = [0] * n, [0] * n
    pressed = set()
    for i, j in zip(cells[0::2], cells[1::2]):
        if not (1 <= i <= n and 1 <= j <= n):
            fail("a cell outside the square")
        row[i - 1] ^= 1
        col[j - 1] ^= 1
        pressed ^= {(i - 1, j - 1)}
    # a soldier turns once for every command in its row or column
    first = None
    for i in range(n):
        for j in range(n):
            turns = row[i] ^ col[j] ^ ((i, j) in pressed)
            state = (grid[i][j] == "B") ^ turns
            if first is None:
                first = state
            elif state != first:
                fail("soldiers still stand differently")


main()
