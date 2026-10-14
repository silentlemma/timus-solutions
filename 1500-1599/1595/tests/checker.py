"""Checker: distinct positive terms up to 10^13, at most 2N of them, all of
1..N among them, and every first k terms adding up to a multiple of k."""

import sys

TOP = 10**13


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    n = int(open(source).read())
    words = open(output).read().split()
    if not words or not all(w.isdigit() for w in words):
        fail("expected positive integers")
    terms = [int(w) for w in words]
    if len(terms) > 2 * n:
        fail("%d terms, more than 2N" % len(terms))
    if len(set(terms)) != len(terms):
        fail("a term repeats")
    if any(t < 1 or t > TOP for t in terms):
        fail("a term is out of range")
    if not set(range(1, n + 1)) <= set(terms):
        fail("not every number from 1 to N appears")
    total = 0
    for k, t in enumerate(terms, 1):
        total += t
        if total % k:
            fail("the first %d terms add up to %d" % (k, total))


main()
