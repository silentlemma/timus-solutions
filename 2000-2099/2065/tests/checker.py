"""Checker: n integers of absolute value at most 10^6 with at least k
distinct values whose segment sums take exactly k distinct values, the
least possible since every single element is a segment sum."""

import sys

LIMIT = 10 ** 6


class Bad(Exception):
    pass


def check(source, expected, output):
    n, k = map(int, open(source).read().split())
    got = open(output).read().split()
    if len(got) != n or not all(t.lstrip("-").isdigit() for t in got):
        raise Bad("expected %d integers" % n)
    a = [int(t) for t in got]
    if any(abs(v) > LIMIT for v in a):
        raise Bad("a value is too large")
    if len(set(a)) < k:
        raise Bad("fewer than %d distinct values" % k)
    sums = set()
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            sums.add(s)
    if len(sums) != k:
        raise Bad("%d distinct sums, the least is %d" % (len(sums), k))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
