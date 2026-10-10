"""Checker: one colour per door listed in every row, each room with as many
G as Y doors give or take one, and for every pair of rooms the doors
between them green on exactly one side: the G marks of the two rows on
those doors add up to the number of doors (so it does not matter which
mention of a repeated door goes with which). A colouring always exists, so
Impossible is rejected."""

import sys
from collections import Counter


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n = next(tok)
    rows = [[next(tok) for _ in range(next(tok))] for _ in range(n)]
    lines = open(output).read().split("\n")
    if lines and lines[0].strip() == "Impossible":
        fail("a colouring always exists")
    green = Counter()
    for u in range(n):
        got = lines[u].split() if u < len(lines) else []
        if len(got) != len(rows[u]) or set(got) - {"G", "Y"}:
            fail("room %d needs %d colours G or Y" % (u + 1, len(rows[u])))
        if abs(got.count("G") - got.count("Y")) > 1:
            fail("room %d is unbalanced" % (u + 1))
        for v, c in zip(rows[u], got):
            green[(u + 1, v)] += c == "G"
    doors = Counter()
    for u in range(n):
        for v in rows[u]:
            doors[(min(u + 1, v), max(u + 1, v))] += 1
    for (a, b), count in doors.items():
        if a == b:
            continue
        if count % 2 or green[(a, b)] + green[(b, a)] != count // 2:
            fail("the doors between %d and %d are not green on one side each" % (a, b))


main()
