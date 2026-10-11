import sys
from math import comb


def spread(items, runs):
    """Ways to put identical items into runs in order, runs may stay empty."""
    if runs == 0:
        return 1 if items == 0 else 0
    return comb(items + runs - 1, runs - 1)


def main():
    words = iter(sys.stdin.read().split())
    n, k, loco = int(next(words)), int(next(words)), next(words)
    have = {t: 0 for t in ("AA", "AB", "BA", "BB")}
    for _ in range(n):
        have[next(words)] += 1
    # the train starts with the coupling that fits the locomotive's right
    # end and finishes with the one that fits its left end
    start, end = loco[1], loco[0]
    other = {"A": "B", "B": "A"}
    total = 0
    for switches in range(k + 1):
        # AB and BA carriages must alternate, beginning with the one that
        # leaves the starting coupling
        first, second = start + other[start], other[start] + start
        uses = {first: (switches + 1) // 2, second: switches // 2}
        if uses[first] > have[first] or uses[second] > have[second]:
            continue
        if (start if switches % 2 == 0 else other[start]) != end:
            continue
        # the runs between switches hold the AA and BB carriages
        runs = {start: switches // 2 + 1, other[start]: (switches + 1) // 2}
        for aa in range(k - switches + 1):
            bb = k - switches - aa
            if aa <= have["AA"] and bb <= have["BB"]:
                total += spread(aa, runs["A"]) * spread(bb, runs["B"])
    print("YES\n%d" % total if total else "NO")


main()
