"""Deterministic complete deals, always ten cards per player.

random SEED LEADER: shuffle the 32-card deck and deal thirty cards.
low SEED LEADER: bias the declarer's random hand toward low ranks, then
shuffle the remaining deck for the defenders and the two undealt cards.
LEADER is 1, 2, or 3. Both modes also shuffle the order within each hand.
"""

import random
import sys

RANKS = ("7", "8", "9", "10", "J", "Q", "K", "A")
SUITS = "SCDH"


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("random", "low"):
        raise ValueError("usage: gen.py {random|low} SEED LEADER")
    mode = sys.argv[1]
    seed, leader = map(int, sys.argv[2:])
    if leader not in (1, 2, 3):
        raise ValueError("LEADER must be in 1..3")
    rng = random.Random(seed)
    deck = [rank + suit for suit in SUITS for rank in RANKS]
    rng.shuffle(deck)
    if mode == "low":
        # Independent random integer priorities, with a bias toward low cards.
        priorities = {card: rng.randrange(12) + 4 * RANKS.index(card[:-1]) for card in deck}
        first = sorted(deck, key=priorities.__getitem__)[:10]
        rest = [card for card in deck if card not in first]
        rng.shuffle(rest)
        hands = [first, rest[:10], rest[10:20]]
    else:
        hands = [deck[p * 10:(p + 1) * 10] for p in range(3)]
    for hand in hands:
        rng.shuffle(hand)
        print(" ".join(hand))
    print(leader)


if __name__ == "__main__":
    main()
