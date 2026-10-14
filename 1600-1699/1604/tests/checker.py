"""Checker: every sign used exactly as many times as made, and as few equal
neighbours as possible, which is max(0, 2m - n - 1) for the largest
count m: the other n - m signs can split the commonest kind into at most
n - m + 1 runs."""

import sys
from collections import Counter


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    k = int(data[0])
    counts = [int(c) for c in data[1 : k + 1]]
    n = sum(counts)
    got = open(output).read().split()
    if len(got) != n or not all(w.isdigit() for w in got):
        fail("expected %d sign numbers" % n)
    order = [int(w) for w in got]
    have = Counter(order)
    if any(have[t] != counts[t - 1] for t in range(1, k + 1)) or sum(have.values()) != n:
        fail("the signs do not match the ones made")
    equal = sum(1 for a, b in zip(order, order[1:]) if a == b)
    best = max(0, 2 * max(counts) - n - 1)
    if equal != best:
        fail("%d equal neighbours, %d possible" % (equal, best))


main()
