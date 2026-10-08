"""Checker: each line is a simple cycle of at least 3 vertices of minimal
total length, or "No solution." exactly when the expected answer is."""

import sys

NO_SOLUTION = "No solution."
END_OF_INPUT = -1
MIN_CYCLE = 3
TOKENS_PER_ROAD = 3


def graphs(path):
    data = [int(x) for x in open(path).read().split()]
    pos = 0
    while data[pos] != END_OF_INPUT:
        n, m = data[pos], data[pos + 1]
        pos += 2
        edge = {}
        for _ in range(m):
            a, b, length = data[pos : pos + TOKENS_PER_ROAD]
            pos += TOKENS_PER_ROAD
            key = (min(a, b), max(a, b))
            edge[key] = min(edge.get(key, length), length)
        yield n, edge


def length(cycle, n, edge):
    """Total length of the cycle, or None if it is not a valid tour."""
    if len(cycle) < MIN_CYCLE or len(set(cycle)) != len(cycle):
        return None
    if any(v < 1 or v > n for v in cycle):
        return None
    total = 0
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        key = (min(a, b), max(a, b))
        if key not in edge:
            return None
        total += edge[key]
    return total


def main():
    inp, expected, output = sys.argv[1:4]
    want = open(expected).read().split("\n")
    got = open(output).read().split("\n")
    for i, (n, edge) in enumerate(graphs(inp)):
        line = got[i].strip() if i < len(got) else ""
        if want[i].strip() == NO_SOLUTION:
            if line != NO_SOLUTION:
                print("test %d: expected %s" % (i + 1, NO_SOLUTION))
                sys.exit(1)
            continue
        try:
            total = length([int(x) for x in line.split()], n, edge)
        except ValueError:
            total = None
        if total is None:
            print("test %d: %r is not a simple cycle of the graph" % (i + 1, line))
            sys.exit(1)
        best = length([int(x) for x in want[i].split()], n, edge)
        if total != best:
            print("test %d: length %d, the shortest is %d" % (i + 1, total, best))
            sys.exit(1)


main()
