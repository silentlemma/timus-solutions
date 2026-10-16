"""Checker: 0 exactly when the expected answer is 0; otherwise every
strip once, signed when turned over, with each green line ending where
the next one starts and all of them on one straight line."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    words = [int(w) for w in open(source).read().split()]
    h, n = words[0], words[1]
    strips = [(words[2 + 2 * i], words[3 + 2 * i]) for i in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["0"]:
        if got != ["0"]:
            raise Bad("the strips cannot make one line, expected 0")
        return
    try:
        order = [int(w) for w in got]
    except ValueError:
        raise Bad("expected whole numbers")
    if len(order) != n or sorted(abs(v) for v in order) != list(range(1, n + 1)):
        raise Bad("expected every strip exactly once")
    ends = []
    for v in order:
        l, r = strips[abs(v) - 1]
        ends.append((l, r) if v > 0 else (h - r, h - l))
    for (a, b), (c, d) in zip(ends, ends[1:]):
        if b != c:
            raise Bad("a line ends at %d and the next starts at %d" % (b, c))
        if d - c != b - a:
            raise Bad("the lines bend")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
