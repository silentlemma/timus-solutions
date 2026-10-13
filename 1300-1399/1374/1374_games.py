import sys

PLAYERS = 3
SUITS = 4
RANKS = 8
RANK_NAMES = ("7", "8", "9", "10", "J", "Q", "K", "A")
SUIT_NAMES = "SCDH"
HAND = 10  # cards per player
SUIT_BITS = 14  # an owner string of a suit fits in this many bits
LIMIT = 100000  # remembered positions, to stay inside the memory limit
FULL_SUIT = (1 << RANKS) - 1


def main():
    words = sys.stdin.read().split()
    # hand[p] holds player p's cards, suit s in bits 8 s .. 8 s + 7, rank upwards
    hand = [0] * PLAYERS
    for p in range(PLAYERS):
        for t in words[p * HAND : (p + 1) * HAND]:
            hand[p] |= 1 << (SUIT_NAMES.index(t[-1]) * RANKS + RANK_NAMES.index(t[:-1]))
    leader = int(words[PLAYERS * HAND]) - 1
    memo = {}

    suit_codes = {}  # the owner string of a suit, by the three players' masks

    def suit_code(m0, m1, m2):
        v = 1
        for r in range(RANKS):
            if m0 >> r & 1:
                v = v * PLAYERS
            elif m1 >> r & 1:
                v = v * PLAYERS + 1
            elif m2 >> r & 1:
                v = v * PLAYERS + 2
        return v

    def key(lead):
        # the suits play alike and only the order of the cards inside a suit
        # matters, so a position is the sorted owner strings of the suits
        h0, h1, h2 = hand
        codes = []
        for s in range(0, SUITS * RANKS, RANKS):
            m = (
                (h0 >> s & FULL_SUIT)
                | (h1 >> s & FULL_SUIT) << RANKS
                | (h2 >> s & FULL_SUIT) << 2 * RANKS
            )
            v = suit_codes.get(m)
            if v is None:
                v = suit_codes[m] = suit_code(
                    h0 >> s & FULL_SUIT, h1 >> s & FULL_SUIT, h2 >> s & FULL_SUIT
                )
            codes.append(v)
        codes.sort()
        k = lead + 1
        for v in codes:
            k = (k << SUIT_BITS) | v
        return k

    def choices(p, allowed, everyone):
        # one card from each run of touching cards: no other player's card
        # lies between two cards of a run
        out = []
        mine = hand[p]
        while allowed:
            low = allowed & -allowed
            allowed ^= low
            c = low.bit_length() - 1
            below = everyone & (low - 1) & (FULL_SUIT << (c - c % RANKS))
            if below == 0 or not mine >> (below.bit_length() - 1) & 1:
                out.append(c)
        return out

    def play(lead, step, suit, best, best_player, everyone):
        # the first player looks for any good card, the others for any card
        # that makes the first player take the trick
        p = (lead + step) % PLAYERS
        allowed = hand[p]
        if step > 0 and allowed & (FULL_SUIT << (suit * RANKS)):
            allowed &= FULL_SUIT << (suit * RANKS)
        for c in choices(p, allowed, everyone):
            s, b, bp = (c // RANKS, c, p) if step == 0 else (suit, best, best_player)
            if step > 0 and c // RANKS == suit and c > best:
                b, bp = c, p
            hand[p] &= ~(1 << c)
            if step + 1 < PLAYERS:
                ok = play(lead, step + 1, s, b, bp, everyone)
            else:
                ok = bp != 0 and survive(bp)
            hand[p] |= 1 << c
            if ok == (p == 0):
                return ok
        return p != 0

    def survive(lead):
        # can the first player take no trick from here, whatever the others do
        if hand[0] == 0:
            return True
        k = key(lead)
        if k not in memo:
            if len(memo) > LIMIT:
                memo.clear()
            memo[k] = play(lead, 0, 0, -1, -1, hand[0] | hand[1] | hand[2])
        return memo[k]

    print(";)" if survive(leader) else ";(")


main()
