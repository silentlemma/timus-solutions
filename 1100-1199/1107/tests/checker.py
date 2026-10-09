"""Checker: YES and one shop from 1 to M per set, with no two similar sets
in one shop. Multisets are compared through a random additive hash: a set
and the sets one removal or one replacement away share the hash of the
set with one item removed. An answer always exists, so NO is rejected."""

import random
import sys

MASK = (1 << 64) - 1


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    lines = open(inp).read().split("\n")
    n, k, m = map(int, lines[0].split())
    sets = [list(map(int, line.split()))[1:] for line in lines[1 : k + 1]]
    weight = [random.getrandbits(64) for _ in range(n + 1)]
    got = open(output).read().split()
    if not got or got[0] != "YES":
        fail("an assignment always exists")
    if len(got) != k + 1 or not all(x.isdigit() and 1 <= int(x) <= m for x in got[1:]):
        fail("expected one shop from 1 to M per set")
    shop = [int(x) for x in got[1:]]
    whole = {}
    smaller = {}
    for i, items in enumerate(sets):
        h = sum(weight[x] for x in items) & MASK
        whole.setdefault((shop[i], h), []).append(i)
        for x in set(items):
            smaller.setdefault((shop[i], (h - weight[x]) & MASK), []).append(i)
    for key, owners in smaller.items():
        # one removal: a whole set equals another set minus one item
        for j in whole.get(key, []):
            fail("sets %d and %d share shop %d" % (owners[0] + 1, j + 1, key[0]))
        # one replacement: two different sets of one size share a removal
        if len(owners) > 1:
            fail("sets %d and %d share shop %d" % (owners[0] + 1, owners[1] + 1, key[0]))


main()
