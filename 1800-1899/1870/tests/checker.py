"""Checker: "No" exactly when the expected output says so; otherwise
"Yes" and a permutation of 1..n with no two queens on one diagonal of
the torus, that is with all x + y and all x - y different modulo n."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read())
    impossible = open(expected).read().split() == ["No"]
    words = open(output).read().split()
    if words == ["No"]:
        if not impossible:
            raise Bad("a placement exists")
        return
    if impossible:
        raise Bad("no placement exists")
    if len(words) != n + 1 or words[0] != "Yes" or not all(v.isdigit() for v in words[1:]):
        raise Bad("expected Yes and %d numbers" % n)
    rows = [int(v) for v in words[1:]]
    if sorted(rows) != list(range(1, n + 1)):
        raise Bad("two queens share a row")
    if len({(x + y) % n for x, y in enumerate(rows)}) != n:
        raise Bad("two queens share a diagonal")
    if len({(x - y) % n for x, y in enumerate(rows)}) != n:
        raise Bad("two queens share an anti-diagonal")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
