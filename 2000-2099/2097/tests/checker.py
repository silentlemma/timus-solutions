"""Checker: -1 exactly when expected; otherwise a slope and a start where the
new slope is similar, with the same smallest |a| as the expected answer."""

import sys


class Bad(Exception):
    pass


def similarity(x, slopes, slope, start):
    # the parameter a of a similar section, or None
    if not 1 <= slope <= len(slopes):
        return None
    y = slopes[slope - 1]
    m = len(x) - 1
    if start < 0 or start + m >= len(y):
        return None
    d = [x[i] - y[start + i] for i in range(m + 1)]
    a = d[1] - d[0]
    if any(d[i] != d[0] + a * i for i in range(m + 1)):
        return None
    return a


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, m = data[0], data[1]
    x = data[2:3 + m]
    pos = 3 + m
    slopes = []
    for _ in range(n):
        length = data[pos]
        slopes.append(data[pos + 1:pos + 2 + length])
        pos += 2 + length
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["-1"]:
        if got != ["-1"]:
            raise Bad("expected -1")
        return
    if len(got) != 2 or not all(w.lstrip("-").isdigit() for w in got):
        raise Bad("expected a slope and a start")
    best = similarity(x, slopes, int(want[0]), int(want[1]))
    a = similarity(x, slopes, int(got[0]), int(got[1]))
    if a is None:
        raise Bad("the section is not similar")
    if abs(a) != abs(best):
        raise Bad("|a| is %d, expected %d" % (abs(a), abs(best)))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
