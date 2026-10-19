"""Checker: the smallest largest group as expected, and two different courses
that really give it."""

import sys

GROUPS = 4


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n, m = int(data[0]), int(data[1])
    rows = [data[2 + i * m:2 + (i + 1) * m] for i in range(n)]
    best = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != 3 or not all(w.isdigit() for w in got):
        raise Bad("expected a size and two courses")
    if int(got[0]) != best:
        raise Bad("expected %d, got %s" % (best, got[0]))
    a, b = int(got[1]), int(got[2])
    if a == b or not (1 <= a <= m and 1 <= b <= m):
        raise Bad("not two different courses")
    count = [0] * GROUPS
    for r in rows:
        count[2 * (r[a - 1] == "1") + (r[b - 1] == "1")] += 1
    if max(count) != best:
        raise Bad("the courses give %d" % max(count))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
