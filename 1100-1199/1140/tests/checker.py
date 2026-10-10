"""Checker: m, then m segments of a direction X, Y or Z and a nonzero length
that lead from the last cell back to the centre, with the fewest cells.
In coordinates along X and Z a step along Y is (1, 1); the fewest steps
from (p, q) to the centre are max(|p|, |q|) when p and q have the same
sign and |p| + |q| otherwise."""

import sys

STEP = {"X": (1, 0), "Y": (1, 1), "Z": (0, 1)}


def fail(reason):
    print(reason)
    sys.exit(1)


def distance(p, q):
    return max(abs(p), abs(q)) if p * q >= 0 else abs(p) + abs(q)


def main():
    inp, _, output = sys.argv[1:4]
    tok = open(inp).read().split()
    p = q = 0
    for k in range(int(tok[0])):
        dx, dy = STEP[tok[1 + 2 * k]]
        length = int(tok[2 + 2 * k])
        p, q = p + dx * length, q + dy * length
    best = distance(p, q)
    got = open(output).read().split()
    try:
        m = int(got[0])
        segs = [(got[1 + 2 * k], int(got[2 + 2 * k])) for k in range(m)]
    except (IndexError, ValueError):
        fail("expected m and m segments")
    if len(got) != 1 + 2 * m:
        fail("extra output")
    cells = 0
    for d, length in segs:
        if d not in STEP or length == 0:
            fail("bad segment %s %d" % (d, length))
        dx, dy = STEP[d]
        p, q = p + dx * length, q + dy * length
        cells += abs(length)
    if (p, q) != (0, 0):
        fail("the route ends at (%d, %d), not at the centre" % (p, q))
    if cells != best:
        fail("the route has %d steps, the shortest has %d" % (cells, best))


if __name__ == "__main__":
    main()
