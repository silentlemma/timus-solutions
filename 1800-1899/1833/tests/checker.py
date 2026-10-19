"""Checker: n non-negative premiums, each prize crew getting at least k
in total, and the sum equal to the least possible one taken from the
expected answer, all up to 10^-6 per premium."""

import sys

EPS = 1e-6


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, k, m = data[0], data[1], data[2]
    crews = [(data[3 + 2 * i] - 1, data[4 + 2 * i] - 1) for i in range(m)]
    want = sum(map(float, open(expected).read().split()))
    try:
        got = [float(w) for w in open(output).read().split()]
    except ValueError:
        raise Bad("expected numbers")
    if len(got) != n:
        raise Bad("expected %d premiums, got %d" % (n, len(got)))
    if min(got) < -EPS:
        raise Bad("a negative premium")
    for a, b in crews:
        if got[a] + got[b] < k - 2 * EPS:
            raise Bad("crew %d %d gets %.6f" % (a + 1, b + 1, got[a] + got[b]))
    if sum(got) > want + n * EPS:
        raise Bad("total %.6f, the least is %.6f" % (sum(got), want))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
