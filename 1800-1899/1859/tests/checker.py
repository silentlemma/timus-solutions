"""Checker: n lines of six people, everybody exactly once, every line
with four who want a compartment seat and two who want a side seat, and
every two friends on one line."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n, wish, m = int(data[0]), data[1], int(data[2])
    friends = [(int(data[3 + 2 * k]), int(data[4 + 2 * k])) for k in range(m)]
    lines = [line.split() for line in open(output).read().strip().split("\n")]
    if len(lines) != n:
        raise Bad("expected %d lines" % n)
    block = [0] * (6 * n + 1)
    for i, line in enumerate(lines):
        if len(line) != 6 or not all(v.isdigit() for v in line):
            raise Bad("line %d is not six numbers" % (i + 1))
        people = [int(v) for v in line]
        if any(not 1 <= p <= 6 * n or block[p] for p in people):
            raise Bad("line %d repeats somebody or names nobody" % (i + 1))
        for p in people:
            block[p] = i + 1
        if sum(wish[p - 1] == "1" for p in people) != 4:
            raise Bad("line %d does not want four compartment seats" % (i + 1))
    for a, b in friends:
        if block[a] != block[b]:
            raise Bad("friends %d and %d travel apart" % (a, b))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
