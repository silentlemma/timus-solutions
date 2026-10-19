import sys
from array import array
from collections import deque

UNREACHED = -2
UNKNOWN = -1


def solve(values, offsets, edges):
    entry = array("i", [UNREACHED]) * len(values)
    entry[0] = 0
    pending = deque([0])
    while pending:
        vertex = pending.popleft()
        offered = values[vertex] or entry[vertex]
        for at in range(offsets[vertex], offsets[vertex + 1]):
            target = edges[at]
            old = entry[target]
            merged = offered if old == UNREACHED else old if old == offered else UNKNOWN
            if old != merged:
                entry[target] = merged
                pending.append(target)
    return entry


def read_case(tokens):
    n = next(tokens)
    values = array("i")
    offsets = array("i", [0])
    edges = array("i")
    for _ in range(n):
        values.append(next(tokens))
        degree = next(tokens)
        edges.extend(next(tokens) - 1 for _ in range(degree))
        offsets.append(len(edges))
    return values, offsets, edges


def word(value):
    if value == UNKNOWN:
        return "unknown"
    return str(value) if value else "sober"


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    values, offsets, edges = read_case(tokens)
    del tokens
    entry = solve(values, offsets, edges)
    lines = [word(before) + " " + word(value or before) for before, value in zip(entry, values)]
    sys.stdout.write("\n".join(lines) + "\n")
