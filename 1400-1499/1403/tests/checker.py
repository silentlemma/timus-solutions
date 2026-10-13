"""Checker: distinct orders, each delivered by its deadline when they go
one per day in the given order, with the largest possible total reward."""

import sys


def best(deadline, reward):
    """The largest total, by the most rewarding orders on the latest free days."""
    parent = {}

    def free(d):
        # the latest free day not after d, 0 when none is left
        path = []
        while d in parent:
            path.append(d)
            d = parent[d]
        for p in path:
            parent[p] = d
        return d

    total = 0
    for i in sorted(range(len(reward)), key=lambda i: -reward[i]):
        d = free(min(deadline[i], len(reward)))
        if d > 0:
            parent[d] = d - 1
            total += reward[i]
    return total


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n = data[0]
    deadline, reward = data[1 : 1 + 2 * n : 2], data[2 : 2 + 2 * n : 2]
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if not got or len(got) != 1 + got[0]:
        fail("expected the count and that many orders")
    order = got[1:]
    if len(set(order)) != len(order) or any(not 1 <= i <= n for i in order):
        fail("orders must be distinct and between 1 and N")
    for day, i in enumerate(order, 1):
        if day > deadline[i - 1]:
            fail("order %d is late" % i)
    if sum(reward[i - 1] for i in order) != best(deadline, reward):
        fail("the reward is not the largest")


main()
