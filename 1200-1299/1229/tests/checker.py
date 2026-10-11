"""Checker: N rows of M numbers in which every number marks exactly two
neighbouring cells, and no brick covers the same two cells as a brick of
the first layer. A second layer always exists, so -1 is rejected."""

import sys
from collections import defaultdict


def fail(reason):
    print(reason)
    sys.exit(1)


def bricks(grid):
    cells = defaultdict(list)
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            cells[v].append((i, j))
    return cells


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    n, m = int(data[0]), int(data[1])
    first = [data[2 + i * m : 2 + (i + 1) * m] for i in range(n)]
    tokens = open(output).read().split()
    if len(tokens) != n * m:
        fail("expected %d numbers, got %d" % (n * m, len(tokens)))
    second = [tokens[i * m : (i + 1) * m] for i in range(n)]
    lower = {tuple(sorted(c)) for c in bricks(first).values()}
    for label, cells in bricks(second).items():
        if len(cells) != 2:
            fail("brick %s covers %d cells" % (label, len(cells)))
        (a, b), (c, d) = cells
        if abs(a - c) + abs(b - d) != 1:
            fail("brick %s covers cells that are not neighbours" % label)
        if tuple(sorted(cells)) in lower:
            fail("brick %s lies exactly on a brick of the first layer" % label)


if __name__ == "__main__":
    main()
