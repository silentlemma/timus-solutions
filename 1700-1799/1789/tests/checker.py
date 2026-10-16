"""Checker: a count of at most 1000 and that many pedestals from 1 to n.
The set of pedestals where the artifact may still be is followed: a
touch removes its pedestal, then every other place moves to a
neighbour. The set must become empty."""

import sys

MOST_TOUCHES = 1000


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read().split()[0])
    got = open(output).read().split()
    if not got or not all(w.isdigit() for w in got):
        raise Bad("expected whole numbers")
    m = int(got[0])
    if m > MOST_TOUCHES:
        raise Bad("%d touches, more than %d" % (m, MOST_TOUCHES))
    if len(got) != 1 + m:
        raise Bad("expected %d pedestals" % m)
    possible = set(range(1, n + 1))
    for t, word in enumerate(got[1:]):
        p = int(word)
        if not 1 <= p <= n:
            raise Bad("touch %d is at pedestal %d, outside 1..%d" % (t + 1, p, n))
        possible.discard(p)
        possible = {q + d for q in possible for d in (-1, 1) if 1 <= q + d <= n}
    if possible:
        raise Bad("the artifact may still be at pedestal %d" % min(possible))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
