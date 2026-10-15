"""Checker: NO exactly when the expected answer says so, and otherwise
YES and n counts from 0 to k whose subset sums all differ, so that one
weighing tells the platinum bags apart."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    n, k = (int(w) for w in open(source).read().split()[:2])
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if want == "NO":
        if got != ["NO"]:
            raise Bad("expected NO")
        return
    if not got or got[0] != "YES" or len(got) != n + 1:
        raise Bad("expected YES and %d counts" % n)
    try:
        counts = [int(w) for w in got[1:]]
    except ValueError:
        raise Bad("the counts are not integers")
    if any(not 0 <= c <= k for c in counts):
        raise Bad("a count is outside 0 .. %d" % k)
    reach = 1
    for c in counts:
        if reach & (reach << c):
            raise Bad("two sets of platinum bags weigh the same")
        reach |= reach << c


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
