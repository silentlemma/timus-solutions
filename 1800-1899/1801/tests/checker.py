"""Checker: "No" exactly when the expected answer is "No"; otherwise
"Yes" and g groups of t team names, every team used once, each group
holding one team of every pot and no two teams of one party."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    groups, pots = int(words[0]), int(words[1])
    pot_of, party_of = {}, {}
    for e in range(groups * pots):
        name, party = words[2 + 2 * e], words[3 + 2 * e]
        pot_of[name] = e // groups
        party_of[name] = party
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[:1] == ["No"]:
        if got != ["No"]:
            raise Bad("no grouping exists, expected No")
        return
    if not got or got[0] != "Yes":
        raise Bad("a grouping exists, expected Yes")
    names = got[1:]
    if len(names) != groups * pots:
        raise Bad("expected %d team names, got %d" % (groups * pots, len(names)))
    if set(names) != set(pot_of) or len(set(names)) != len(names):
        raise Bad("every team must appear exactly once")
    for g in range(groups):
        members = names[g * pots:(g + 1) * pots]
        if len({pot_of[m] for m in members}) != pots:
            raise Bad("group %d does not hold one team of every pot" % (g + 1))
        if len({party_of[m] for m in members}) != pots:
            raise Bad("group %d holds two teams of one party" % (g + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
