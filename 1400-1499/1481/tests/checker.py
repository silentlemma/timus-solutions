"""Checker: the order always exists, so the output must use every weight
once, each on L or R, and after every step the heavier pan must be the
one the record shows."""

import sys

SURRENDER = "I'm too stupid to solve this problem"


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    weights = sorted(int(x) for x in data[1 : n + 1])
    record = data[n + 1]
    text = open(output).read()
    if SURRENDER in text:
        fail("an order always exists")
    tokens = text.split()
    if len(tokens) != 2 * n:
        fail("expected %d lines of a weight and a pan" % n)
    used = []
    balance = 0
    for i in range(n):
        try:
            w = int(tokens[2 * i])
        except ValueError:
            fail("line %d: not a weight" % (i + 1))
        pan = tokens[2 * i + 1]
        if pan not in ("L", "R"):
            fail("line %d: the pan must be L or R" % (i + 1))
        used.append(w)
        balance += w if pan == "L" else -w
        shown = "L" if balance > 0 else "R" if balance < 0 else "E"
        if shown != record[i]:
            fail("after step %d the scale shows %s, not %s" % (i + 1, shown, record[i]))
    if sorted(used) != weights:
        fail("the weights are not the given set")


main()
