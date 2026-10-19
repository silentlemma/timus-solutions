"""Checker: the total utility as in the expected output, and an order of all
tasks that really earns it."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    x, n = data[0], data[1]
    a, b = data[2:2 + n], data[2 + n:2 + 2 * n]
    best = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != n + 1 or not all(w.isdigit() for w in got):
        raise Bad("expected the utility and %d task numbers" % n)
    if int(got[0]) != best:
        raise Bad("expected utility %d, got %s" % (best, got[0]))
    order = [int(w) for w in got[1:]]
    if sorted(order) != list(range(1, n + 1)):
        raise Bad("not a permutation of the tasks")
    debt, total = x, 0
    for i in order:
        debt = max(0, debt - a[i - 1])
        total += max(0, b[i - 1] - debt)
    if total != best:
        raise Bad("the order earns %d" % total)


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
