"""Checker: INCORRECT exactly when the expected answer says so, and
otherwise CORRECT and every match once, with the points adding up to the
table."""

import sys

POINTS = {"<": (0, 3), "<=": (1, 2), ">=": (2, 1), ">": (3, 0)}


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    table = [int(w) for w in words[1:n + 1]]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if want == "INCORRECT":
        if got != ["INCORRECT"]:
            raise Bad("no season ends like this, expected INCORRECT")
        return
    games = n * (n - 1) // 2
    if not got or got[0] != "CORRECT" or len(got) != 1 + 3 * games:
        raise Bad("expected CORRECT and %d matches" % games)
    score = [0] * n
    seen = set()
    for g in range(games):
        a, sign, b = got[1 + 3 * g:4 + 3 * g]
        if not (a.isdigit() and b.isdigit()) or sign not in POINTS:
            raise Bad("match %d is not in the form i ? j" % (g + 1))
        i, j = int(a) - 1, int(b) - 1
        if not (0 <= i < n and 0 <= j < n) or i == j:
            raise Bad("match %d names wrong teams" % (g + 1))
        pair = (min(i, j), max(i, j))
        if pair in seen:
            raise Bad("teams %d and %d play twice" % (i + 1, j + 1))
        seen.add(pair)
        score[i] += POINTS[sign][0]
        score[j] += POINTS[sign][1]
    if score != table:
        raise Bad("the points do not match the table")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
