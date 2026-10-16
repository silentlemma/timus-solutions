"""Checker: NO exactly when the expected answer says so; otherwise YES
and one part per bar, none negative or above the bar's weight, with
the weight and the gold of the parts within 1e-6 of the order."""

import sys

LIMIT = 1e-6
SLACK = 1e-9
SCALE = 1000


class Bad(Exception):
    pass


def check(source, expected, output):
    v = [int(w) for w in open(source).read().split()]
    n, need, fineness = v[0], v[1], v[2]
    mass, purity = v[3::2], v[4::2]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if want == "NO":
        if got != ["NO"]:
            raise Bad("the bar cannot be cast, expected NO")
        return
    if len(got) != n + 1 or got[0] != "YES":
        raise Bad("expected YES and %d parts" % n)
    try:
        parts = [float(w) for w in got[1:]]
    except ValueError:
        raise Bad("a part is not a number")
    for i, x in enumerate(parts):
        if not -SLACK <= x <= mass[i] + SLACK:
            raise Bad("part %d is %.10f, outside 0..%d" % (i + 1, x, mass[i]))
    if abs(sum(parts) - need) >= LIMIT:
        raise Bad("the parts weigh %.10f instead of %d" % (sum(parts), need))
    gold = sum(x * p / SCALE for x, p in zip(parts, purity))
    if abs(gold - need * fineness / SCALE) >= LIMIT:
        raise Bad("the parts hold %.10f grams of gold instead of %.10f"
                  % (gold, need * fineness / SCALE))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
