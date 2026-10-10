"""Checker: the printed difference, then M lines of box numbers. Every box
from 1 to N goes to exactly one general, the printed difference equals
the gap between the richest and the poorest general, and it is at most
K, the largest result the emperor accepts."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = open(inp).read().split()
    n, m, k = int(tok[0]), int(tok[1]), int(tok[2])
    value = [int(x) for x in tok[3 : 3 + n]]
    lines = open(output).read().split("\n")
    try:
        told = int(lines[0])
        groups = [[int(x) for x in lines[1 + g].split()] for g in range(m)]
    except (IndexError, ValueError):
        fail("expected the difference and %d lines of box numbers" % m)
    if any(line.strip() for line in lines[1 + m :]):
        fail("extra output after %d generals" % m)
    seen = [False] * (n + 1)
    for group in groups:
        for b in group:
            if not 1 <= b <= n or seen[b]:
                fail("box %d is out of range or given twice" % b)
            seen[b] = True
    if not all(seen[1:]):
        fail("some box is not given")
    gold = [sum(value[b - 1] for b in group) for group in groups]
    gap = max(gold) - min(gold)
    if told != gap:
        fail("printed %d, but the gap is %d" % (told, gap))
    if gap > k:
        fail("the gap %d is above K = %d" % (gap, k))


if __name__ == "__main__":
    main()
