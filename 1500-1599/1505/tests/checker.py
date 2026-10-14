"""Checker: the cost must equal the expected one, or both answers must be
"Impossible". The new flows must list every pipe of every station once,
stay non-negative, cost exactly the printed amount (each unit above a
pipe's capacity costs its d), deliver one more unit into station N, keep
every transit station's outflow at least its inflow, and raise it above
the old surplus by at most the one unit of a well."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def stations(text, n):
    """The descriptions of the n stations, split at their final dots."""
    parts = text.split(".")
    if len(parts) < n + 1 or parts[n].strip():
        fail("expected %d station lines ending with dots" % n)
    return parts[:n]


def main():
    source, expected, output = sys.argv[1:4]
    head, _, rest = open(source).read().lstrip().partition("\n")
    n = int(head)
    pipes = {}  # (from, to) -> [capacity, old flow, cost]
    order = []
    for i, line in enumerate(stations(rest, n), 1):
        for quad in line.split(","):
            if quad.strip():
                a, b, c, d = map(int, quad.split())
                pipes[(i, a)] = [b, c, d]
                order.append((i, a))
    want = open(expected).read().split()
    text = open(output).read().strip()
    if want[0] == "Impossible" or text.startswith("Impossible"):
        if text != want[0]:
            fail("expected %s, got %s" % (want[0], text[:20]))
        return
    first, _, rest = text.partition("\n")
    if first.strip() != want[0]:
        fail("cost %s, expected %s" % (first.strip(), want[0]))
    flow = {}
    for i, line in enumerate(stations(rest, n), 1):
        for pair in line.split(","):
            if not pair.strip():
                continue
            fields = pair.split()
            if len(fields) != 2 or not all(f.isdigit() for f in fields):
                fail("bad pair %r in line %d" % (pair, i))
            a, f = map(int, fields)
            if (i, a) not in pipes or (i, a) in flow:
                fail("pipe %d -> %d is unknown or repeated" % (i, a))
            flow[(i, a)] = f
    if len(flow) != len(pipes):
        fail("some pipes are missing")
    spent = sum(max(0, flow[p] - pipes[p][0]) * pipes[p][2] for p in order)
    if spent != int(want[0]):
        fail("the flows cost %d, expected %s" % (spent, want[0]))
    old, new = [0] * (n + 1), [0] * (n + 1)  # outflow minus inflow
    for (i, a), (_, c, _) in pipes.items():
        old[i] += c
        old[a] -= c
        new[i] += flow[(i, a)]
        new[a] -= flow[(i, a)]
    if new[n] != old[n] - 1:
        fail("station %d gets %d more units, expected 1" % (n, old[n] - new[n]))
    for i in range(1, n):
        if new[i] < 0 or new[i] > old[i] + (old[i] > 0):
            fail("station %d pumps out %d more than it gets" % (i, new[i]))


main()
