"""Checker: as many inns as the expected answer, then a walk of that
many distinct inns from 1 to n, starting at inn 1, where of every two
neighbours one divides the other."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read().split()[0])
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not all(w.isdigit() for w in got):
        raise Bad("expected whole numbers")
    count, walk = int(got[0]), [int(w) for w in got[1:]]
    if count != want:
        raise Bad("%d inns, but %d can be visited" % (count, want))
    if len(walk) != count:
        raise Bad("the walk has %d inns instead of %d" % (len(walk), count))
    if walk[0] != 1:
        raise Bad("the walk must start at inn 1")
    if len(set(walk)) != count or not all(1 <= v <= n for v in walk):
        raise Bad("the inns must be distinct and between 1 and %d" % n)
    for a, b in zip(walk, walk[1:]):
        if a % b and b % a:
            raise Bad("neither of %d and %d divides the other" % (a, b))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
