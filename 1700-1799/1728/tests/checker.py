"""Checker: Fail exactly when every candidate gets the team disqualified,
and otherwise Win and a candidate who gives the strongest team."""

import sys

LYOSHA = "Efremov"
VADIK = "Kantorov"


class Bad(Exception):
    pass


def strengths(source):
    words = iter(open(source).read().split())
    played = set()
    for _ in range(int(next(words))):
        size = int(next(words))
        played.add(frozenset(next(words) for _ in range(size)))
    lyosha, vadik = int(next(words)), int(next(words))
    result = {}
    for _ in range(int(next(words))):
        name, rating = next(words), int(next(words))
        if frozenset((LYOSHA, VADIK, name)) not in played:
            result[name] = lyosha + vadik + rating
        elif frozenset((VADIK, name)) not in played:
            result[name] = vadik + rating
    return result


def check(source, output):
    result = strengths(source)
    got = open(output).read().split()
    if not result:
        if got != ["Fail"]:
            raise Bad("every choice fails, expected Fail")
        return
    if len(got) != 2 or got[0] != "Win":
        raise Bad("expected Win and a name")
    best = max(result.values())
    if got[1] not in result:
        raise Bad("%s is not a candidate who keeps the team in" % got[1])
    if result[got[1]] != best:
        raise Bad("strength %d, the best is %d" % (result[got[1]], best))


def main():
    try:
        check(sys.argv[1], sys.argv[3])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
