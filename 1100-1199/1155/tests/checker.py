"""Checker: IMPOSSIBLE exactly when the two sides of the cube hold
different totals, which no operation changes; otherwise at most 1000
operations on neighbouring chambers, no chamber ever below zero, and all
chambers empty at the end."""

import sys

EDGES = {
    frozenset(e) for e in ["AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"]
}
EVEN = "ACFH"
CELLS = "ABCDEFGH"
LIMIT = 1000


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    count = dict(zip(CELLS, map(int, open(inp).read().split())))
    possible = sum(count[c] for c in EVEN) == sum(count[c] for c in CELLS if c not in EVEN)
    lines = open(output).read().split()
    if lines == ["IMPOSSIBLE"]:
        if possible:
            fail("the duons can be removed")
        return
    if not possible:
        fail("expected IMPOSSIBLE")
    if len(lines) > LIMIT:
        fail("%d operations, more than %d" % (len(lines), LIMIT))
    for op in lines:
        if len(op) != 3 or frozenset(op[:2]) not in EDGES or op[0] == op[1] or op[2] not in "+-":
            fail("bad operation %s" % op)
        step = 1 if op[2] == "+" else -1
        for c in op[:2]:
            count[c] += step
            if count[c] < 0:
                fail("chamber %s goes below zero at %s" % (c, op))
    if any(count.values()):
        fail("duons remain")


if __name__ == "__main__":
    main()
