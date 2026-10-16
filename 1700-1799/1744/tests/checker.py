"""Checker: n (n - 1) / 2 days, the most possible, each with three
different soldiers from 1 to n, and no pair on duty together more than
three times."""

import sys
from collections import Counter
from itertools import combinations

MOST_TOGETHER = 3
PER_DAY = 3


class Bad(Exception):
    pass


def check(source, output):
    n = int(open(source).read().split()[0])
    got = open(output).read().split()
    days = n * (n - 1) // 2
    if not got or not got[0].isdigit() or int(got[0]) != days:
        raise Bad("expected %d days" % days)
    if len(got) != 1 + PER_DAY * days:
        raise Bad("expected three soldiers a day")
    together = Counter()
    for d in range(days):
        team = [int(w) for w in got[1 + PER_DAY * d:1 + PER_DAY * (d + 1)]]
        if len(set(team)) != PER_DAY or not all(1 <= s <= n for s in team):
            raise Bad("day %d is not three different soldiers" % (d + 1))
        for pair in combinations(sorted(team), 2):
            together[pair] += 1
    worst = max(together.values())
    if worst > MOST_TOGETHER:
        raise Bad("a pair is on duty together %d times" % worst)


def main():
    try:
        check(sys.argv[1], sys.argv[3])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
