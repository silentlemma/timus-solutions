"""Checker: No exactly when the expected answer says so; otherwise Yes
and two different minutes for every mage inside the mage's stay, with
no minute shaving more than k mages."""

import sys
from collections import Counter


class Bad(Exception):
    pass


def check(source, expected, output):
    words = [int(w) for w in open(source).read().split()]
    n, k = words[0], words[1]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if want == "No":
        if got != ["No"]:
            raise Bad("not every mage can be shaved, expected No")
        return
    if len(got) != 1 + 2 * n or got[0] != "Yes":
        raise Bad("expected Yes and two minutes for each of %d mages" % n)
    try:
        minutes = [int(w) for w in got[1:]]
    except ValueError:
        raise Bad("a minute is not a whole number")
    busy = Counter()
    for i in range(n):
        t, s = words[2 + 2 * i], words[3 + 2 * i]
        p, q = minutes[2 * i], minutes[2 * i + 1]
        if not t <= p < q <= t + s - 1:
            raise Bad("mage %d is shaved at %d and %d, outside %d..%d" % (i + 1, p, q, t, t + s - 1))
        busy[p] += 1
        busy[q] += 1
    minute, count = max(busy.items(), key=lambda x: x[1])
    if count > k:
        raise Bad("%d mages are shaved at minute %d" % (count, minute))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
