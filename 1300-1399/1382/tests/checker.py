"""Checker: one true statement per friend such that the true claims give
no person two cards and no card two people, and the cards can still be
dealt one to each friend with every false claim false."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def perfect(n, allowed):
    """Is there a perfect matching of people to cards along allowed pairs?"""
    match = [0] * (n + 1)  # card -> person

    def augment(p, seen):
        for q in allowed[p]:
            if q not in seen:
                seen.add(q)
                if match[q] == 0 or augment(match[q], seen):
                    match[q] = p
                    return True
        return False

    sys.setrecursionlimit(10000)
    return all(augment(p, set()) for p in range(1, n + 1))


def main():
    inp, _, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n = data[0]
    got = open(output).read().split()
    if len(got) != n or any(w not in ("1", "2") for w in got):
        fail("expected %d answers of 1 or 2" % n)
    card, owner, false = {}, {}, set()
    for i in range(1, n + 1):
        a, b, c = data[3 * i - 2 : 3 * i + 1]
        true_claim, false_claim = ((i, a), (b, c)) if got[i - 1] == "1" else ((b, c), (i, a))
        p, q = true_claim
        if card.get(p, q) != q or owner.get(q, p) != p:
            fail("friend %d makes a true claim that clashes with another" % i)
        card[p], owner[q] = q, p
        false.add(false_claim)
    if any(card.get(p) == q for p, q in false):
        fail("a false claim turns out true")
    allowed = [[] for _ in range(n + 1)]
    for p in range(1, n + 1):
        if p in card:
            allowed[p] = [card[p]]
        else:
            allowed[p] = [q for q in range(1, n + 1) if q not in owner and (p, q) not in false]
    if not perfect(n, allowed):
        fail("the cards cannot be dealt to match the answers")


if __name__ == "__main__":
    main()
