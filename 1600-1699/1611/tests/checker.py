"""Checker: the least number of fined friends and good conductors, then m
(at most k) and m distinct places in the new line for the friends; the
fines of that line must add up to the printed number. Any best line is
accepted."""

import sys

STEP = 10


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    words = open(source).read().split()
    n, k = int(words[0]), int(words[1])
    good = words[2]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) < 2 or not all(w.lstrip("-").isdigit() for w in got):
        fail("expected numbers")
    total, m = int(got[0]), int(got[1])
    places = [int(w) for w in got[2:]]
    if total != want:
        fail("%d fined instead of %d" % (total, want))
    if not 0 <= m <= k or len(places) != m or len(set(places)) != m:
        fail("bad list of friends")
    if any(not 1 <= p <= n + m for p in places):
        fail("a place outside the line")
    friends = set(places)
    fined, conductor = 0, 0
    for place in range(1, n + m + 1):
        if place in friends:
            fined += place % STEP == 0
        else:
            fined += place % STEP == 0 and good[conductor] == "1"
            conductor += 1
    if fined != total:
        fail("this line fines %d, not %d" % (fined, total))


main()
