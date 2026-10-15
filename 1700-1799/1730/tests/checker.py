"""Checker: No solution exactly when the expected answer says so, and
otherwise a pedigree of at most 10000 lines whose last line has the
given shares, where every line but the last is used in a crossing."""

import sys
from fractions import Fraction

MOST = 10000


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    animals = words[0].split("-")
    target = {}
    for name, text in zip(animals, words[1:]):
        a, b = map(int, text.split("/"))
        target[name] = Fraction(a, b)
    lines = [line.split() for line in open(output).read().strip().split("\n")]
    if open(expected).read().split()[0] == "No":
        if lines != [["No", "solution"]]:
            raise Bad("expected No solution")
        return
    if not lines[0] or not lines[0][0].isdigit():
        raise Bad("expected the number of lines first")
    n = int(lines[0][0])
    rows = lines[1:]
    if not 1 <= n <= MOST or len(rows) != n:
        raise Bad("expected %d lines, between 1 and %d" % (len(rows), MOST))
    shares, used = [], [False] * n
    for k, row in enumerate(rows):
        if len(row) == 1 and row[0] in target:
            shares.append({row[0]: Fraction(1)})
        elif len(row) == 2 and all(w.isdigit() and 1 <= int(w) <= k for w in row):
            x, y = (shares[int(w) - 1] for w in row)
            used[int(row[0]) - 1] = used[int(row[1]) - 1] = True
            mix = {}
            for name in set(x) | set(y):
                mix[name] = (x.get(name, 0) + y.get(name, 0)) / 2
            shares.append(mix)
        else:
            raise Bad("line %d is neither an animal nor two earlier lines" % (k + 1))
    if not all(used[:-1]):
        raise Bad("an ancestor takes part in no crossing")
    final = {name: share for name, share in shares[-1].items() if share}
    if final != target:
        raise Bad("the creature comes out with other shares")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
