import sys

LYOSHA = "Efremov"
VADIK = "Kantorov"


def main():
    words = iter(sys.stdin.read().split())
    played = set()
    for _ in range(int(next(words))):
        size = int(next(words))
        played.add(frozenset(next(words) for _ in range(size)))
    lyosha, vadik = int(next(words)), int(next(words))
    best, chosen = -1, None
    for _ in range(int(next(words))):
        name, rating = next(words), int(next(words))
        # Lyosha stays away from a team that has played before, and the
        # pair left over must then be new, or the team is out
        if frozenset((LYOSHA, VADIK, name)) not in played:
            strength = lyosha + vadik + rating
        elif frozenset((VADIK, name)) not in played:
            strength = vadik + rating
        else:
            continue
        if strength > best:
            best, chosen = strength, name
    print("Fail" if chosen is None else "Win\n" + chosen)


main()
