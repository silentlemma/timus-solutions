"""Checker: the profit must equal the reference's, and the listed people
must be distinct, as many as the profit pays for, and never more than M
on board between any two stops."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n, m, k, price = (int(x) for x in data[:4])
    trips = [(int(data[4 + 2 * i]), int(data[5 + 2 * i])) for i in range(k)]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got:
        fail("empty output")
    if int(got[0]) != want:
        fail("profit %s, expected %d" % (got[0], want))
    people = [int(x) for x in got[1:]]
    if len(people) * price != want:
        fail("%d people do not pay %d" % (len(people), want))
    if len(set(people)) != len(people) or any(not 1 <= p <= k for p in people):
        fail("people must be distinct numbers from 1 to K")
    change = [0] * (n + 2)
    for p in people:
        s, f = trips[p - 1]
        change[s] += 1
        change[f] -= 1
    load = 0
    for stop in range(1, n + 1):
        load += change[stop]
        if load > m:
            fail("%d people ride after stop %d" % (load, stop))


main()
