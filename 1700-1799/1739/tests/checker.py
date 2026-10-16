"""Checker: IMPOSSIBLE exactly when the expected answer says so, and
otherwise a plan of at most 20000 actions that gets every fruit out,
with each exit's aroma a whole multiple of 256, each spray used at most
once, and as few exits as the expected plan."""

import sys
from fractions import Fraction

MOST = 20000
SAFE = 256
DEODORANT = Fraction(3, 4)
PERFUME = Fraction(11, 10)


class Bad(Exception):
    pass


def exits(lines):
    return sum(1 for line in lines if line.split()[:1] == ["take"])


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    aroma = [Fraction(int(x)) for x in words[1:n + 1]]
    want = open(expected).read().strip().split("\n")
    got = open(output).read().strip().split("\n")
    if want[0].strip() == "IMPOSSIBLE":
        if [g.strip() for g in got] != ["IMPOSSIBLE"]:
            raise Bad("expected IMPOSSIBLE")
        return
    if not got[0].strip().isdigit() or int(got[0]) != len(got) - 1:
        raise Bad("the number of actions does not match")
    actions = got[1:]
    if len(actions) > MOST:
        raise Bad("more than %d actions" % MOST)
    outside = [False] * n
    factor = [Fraction(1)] * n
    sprayed = set()
    for line in actions:
        parts = line.split()
        if not parts:
            raise Bad("an empty action")
        if parts[0] in ("dearomatize", "aromatize"):
            if len(parts) != 2 or not parts[1].isdigit() or not 1 <= int(parts[1]) <= n:
                raise Bad("bad action: %s" % line)
            if parts[0] in sprayed:
                raise Bad("%s used twice" % parts[0])
            sprayed.add(parts[0])
            factor[int(parts[1]) - 1] *= DEODORANT if parts[0] == "dearomatize" else PERFUME
            continue
        if parts[0] not in ("take", "return") or not all(p.isdigit() for p in parts[1:]):
            raise Bad("bad action: %s" % line)
        k, fruit = int(parts[1]), [int(p) - 1 for p in parts[2:]]
        if k < 1 or len(fruit) != k or len(set(fruit)) != k or not all(0 <= f < n for f in fruit):
            raise Bad("bad list of fruit: %s" % line)
        taking = parts[0] == "take"
        if any(outside[f] == taking for f in fruit):
            raise Bad("a fruit is not on the right side: %s" % line)
        if taking:
            smell = sum(aroma[f] * factor[f] for f in fruit)
            if smell.denominator != 1 or smell.numerator % SAFE:
                raise Bad("the alarm goes off at: %s" % line)
        for f in fruit:
            outside[f] = taking
            factor[f] = Fraction(1)
    if not all(outside):
        raise Bad("some fruit stays on the plantation")
    if exits(actions) != exits(want[1:]):
        raise Bad("%d exits, the fewest is %d" % (exits(actions), exits(want[1:])))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
