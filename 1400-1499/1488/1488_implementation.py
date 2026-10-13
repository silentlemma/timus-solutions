import sys

RANKS = {"J": 11, "Q": 12, "K": 13, "A": 14}
THREE = 3
HAND = 3
SLEEVE = 6  # three of Sasha's cards, three of Dima's, then the sleeve
CARDS = 8
COMBINATIONS = 7
# combinations from the lowest: high card, pair, flush, straight,
# three of a kind, straight flush, three threes
HIGH, PAIR, FLUSH, STRAIGHT, TRIPLE, STRAIGHT_FLUSH, THREE_THREES = range(COMBINATIONS)


def rank(card):
    return RANKS.get(card[:-1]) or int(card[:-1])


def value(hand):
    """A key that orders hands from the weakest to the strongest."""
    ranks = sorted((rank(c) for c in hand), reverse=True)
    flush = len({c[-1] for c in hand}) == 1
    straight = ranks[0] == ranks[1] + 1 == ranks[2] + 2
    if ranks.count(THREE) == HAND:
        return (THREE_THREES,)
    if straight and flush:
        return (STRAIGHT_FLUSH, *ranks)
    if ranks[0] == ranks[2]:
        return (TRIPLE, *ranks)
    if straight:
        return (STRAIGHT, *ranks)
    if flush:
        return (FLUSH, *ranks)
    if ranks[0] == ranks[1] or ranks[1] == ranks[2]:
        pair = ranks[1]
        other = ranks[2] if ranks[0] == ranks[1] else ranks[0]
        return (PAIR, pair, other)
    return (HIGH, *ranks)


def best(sasha, dima, sleeve):
    """Dima's hands: as dealt, one card swapped, or two swapped for both."""
    usable = [c for c in sleeve if c not in sasha]
    hands = [dima]
    for c in usable:
        for i in range(HAND):
            hands.append(dima[:i] + [c] + dima[i + 1 :])
    if len(usable) == 2:
        for keep in range(HAND):
            hands.append([dima[keep]] + usable)
    target = value(sasha)
    results = [value(h) for h in hands if len(set(h)) == HAND]
    if any(v > target for v in results):
        return "Dima"
    if any(v == target for v in results):
        return "Artyom"
    return "Sasha"


def main():
    cards = sys.stdin.read().split()
    out = []
    for t in range(0, len(cards) - CARDS + 1, CARDS):
        game = cards[t : t + CARDS]
        out.append(best(game[:HAND], game[HAND:SLEEVE], game[SLEEVE:]))
    print("\n".join(out))


main()
