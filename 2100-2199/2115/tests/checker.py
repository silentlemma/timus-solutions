"""Checker: the same verdict as expected; for "Yes", two places whose swap
makes the line sorted one way or the other."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, a = data[0], data[1:]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[0] != "Yes":
        if got != want:
            raise Bad("expected " + " ".join(want))
        return
    if len(got) != 3 or got[0] != "Yes" or not all(w.isdigit() for w in got[1:]):
        raise Bad("expected Yes and two places")
    i, j = int(got[1]) - 1, int(got[2]) - 1
    if not (0 <= i < n and 0 <= j < n) or i == j:
        raise Bad("not two different places")
    a[i], a[j] = a[j], a[i]
    if a != sorted(a) and a != sorted(a, reverse=True):
        raise Bad("the swap does not sort the line")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
