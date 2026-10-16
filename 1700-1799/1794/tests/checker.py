"""Checker: one student from 1 to n who, starting the class, lets as
many students as possible speak at the turn they asked for."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, wants = data[0], data[1:]
    got = open(output).read().split()
    if len(got) != 1 or not got[0].isdigit():
        raise Bad("expected one student number")
    start = int(got[0])
    if not 1 <= start <= n:
        raise Bad("student %d is outside 1..%d" % (start, n))
    votes = [0] * (n + 1)
    for i, want in enumerate(wants, start=1):
        votes[(i - want) % n + 1] += 1
    if votes[start] != max(votes):
        raise Bad("student %d pleases %d, but %d is possible" % (start, votes[start], max(votes)))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
