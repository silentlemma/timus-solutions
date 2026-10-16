"""Checker: -1 exactly when the expected answer is -1; otherwise a count
and that many distinct pairs of different students from 1 to n, with
no three students having the same number of friends."""

import sys
from collections import Counter

MOST_ALIKE = 2


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read().split()[0])
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["-1"]:
        if got != ["-1"]:
            raise Bad("no friendships fit, expected -1")
        return
    if not got or not all(w.isdigit() for w in got):
        raise Bad("expected whole numbers")
    k = int(got[0])
    if len(got) != 1 + 2 * k:
        raise Bad("expected %d pairs" % k)
    degree = Counter()
    seen = set()
    for t in range(k):
        a, b = int(got[1 + 2 * t]), int(got[2 + 2 * t])
        if not (1 <= a <= n and 1 <= b <= n) or a == b:
            raise Bad("pair %d is not two different students" % (t + 1))
        pair = (min(a, b), max(a, b))
        if pair in seen:
            raise Bad("students %d and %d are listed twice" % pair)
        seen.add(pair)
        degree[a] += 1
        degree[b] += 1
    alike = Counter(degree[v] for v in range(1, n + 1))
    value, count = max(alike.items(), key=lambda x: x[1])
    if count > MOST_ALIKE:
        raise Bad("%d students have %d friends each" % (count, value))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
