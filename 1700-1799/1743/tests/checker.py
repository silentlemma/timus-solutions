"""Checker: NO exactly when the expected answer says so, and otherwise
YES and the same dominoes, each possibly turned over, with the left
column non-decreasing and the right one non-increasing."""

import sys
from collections import Counter


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    pieces = Counter(tuple(sorted((int(words[1 + 2 * i]), int(words[2 + 2 * i]))))
                     for i in range(n))
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if want == "NO":
        if got != ["NO"]:
            raise Bad("the dominoes cannot be sorted, expected NO")
        return
    if not got or got[0] != "YES" or len(got) != 1 + 2 * n:
        raise Bad("expected YES and %d dominoes" % n)
    rows = [(int(got[1 + 2 * i]), int(got[2 + 2 * i])) for i in range(n)]
    if Counter(tuple(sorted(r)) for r in rows) != pieces:
        raise Bad("the dominoes are not the given ones")
    for (a, b), (c, d) in zip(rows, rows[1:]):
        if a > c or b < d:
            raise Bad("the columns are not sorted at %d %d / %d %d" % (a, b, c, d))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
