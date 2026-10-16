"""Checker: -1 exactly when the expected answer is -1; otherwise the
expected least time, then a path from fighter 1 to fighter n whose
neighbours differ in one digit or by a swap of two digits, with the
stated time equal to the sum of the costs of its steps."""

import sys

DIGITS = 10


class Bad(Exception):
    pass


def step_cost(a, b, cost):
    diff = [p for p in range(DIGITS) if a[p] != b[p]]
    one = len(diff) == 1
    swap = len(diff) == 2 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]]
    if not (one or swap):
        return None
    return cost[diff[0]]


def check(source, expected, output):
    data = open(source).read().split()
    n = int(data[0])
    cost = list(map(int, data[1:1 + DIGITS]))
    numbers = data[1 + DIGITS:1 + DIGITS + n]
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or not all(w.lstrip("-").isdigit() for w in got):
        raise Bad("expected whole numbers")
    if want[0] == "-1" or got[0] == "-1":
        if got != want[:1] or len(got) != 1:
            raise Bad("expected %s, got %s" % (want[0], got[0]))
        return
    if int(got[0]) != int(want[0]):
        raise Bad("time %s, the least is %s" % (got[0], want[0]))
    if len(got) < 2 or len(got) != 2 + int(got[1]):
        raise Bad("the path length does not match the path")
    path = [int(w) for w in got[2:]]
    if path[0] != 1 or path[-1] != n or not all(1 <= v <= n for v in path):
        raise Bad("the path must go from 1 to %d" % n)
    total = 0
    for a, b in zip(path, path[1:]):
        c = step_cost(numbers[a - 1], numbers[b - 1], cost)
        if c is None:
            raise Bad("fighters %d and %d cannot exchange messages" % (a, b))
        total += c
    if total != int(got[0]):
        raise Bad("the path takes %d, not %s" % (total, got[0]))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
