"""Checker: YES or NO as in the stored answer; after YES, the hand laid
out in full, each card covering the one before, every card but the last
making the opponent skip, queens with an announced suit and jokers with a
proper card."""

import sys

SUITS = "SCDH"
VALUES = "23456789TJQKA"
SKIPS = [v + s for v in "67A" for s in SUITS] + ["KS"]


def fail(reason):
    print(reason)
    sys.exit(1)


def parse(tok):
    # (card as in the hand, value, suit, announced suit or None)
    joker = tok.startswith("*")
    body = tok[1:] if joker else tok
    if len(body) < 2 or body[0] not in VALUES or body[1] not in SUITS:
        fail("bad card %r" % tok)
    if body[0] == "Q":
        if len(body) != 3 or body[2] not in SUITS:
            fail("queen %r without an announced suit" % tok)
    elif len(body) != 2:
        fail("bad card %r" % tok)
    return ("*" if joker else body[:2]), body[0], body[1], body[2:] or None


def covers(card, top):
    if top[3]:
        return card[2] == top[3]
    return card[2] == top[2] or card[1] == top[1]


def main():
    inp, ans, output = sys.argv[1:4]
    lines = open(inp).read().split("\n")
    hand = sorted(lines[0].split())
    top = parse(lines[1].strip())
    want = open(ans).read().split()[0]
    got = open(output).read().split()
    if not got or got[0] != want:
        fail("expected %s" % want)
    if want == "NO":
        if len(got) != 1:
            fail("extra output after NO")
        return
    cards = [parse(t) for t in got[1:]]
    if sorted(c[0] for c in cards) != hand:
        fail("the cards laid are not the hand")
    for k, card in enumerate(cards):
        if not covers(card, top):
            fail("card %d does not cover the one before" % (k + 1))
        if k + 1 < len(cards) and card[1] + card[2] not in SKIPS:
            fail("card %d gives the opponent a move" % (k + 1))
        top = card


if __name__ == "__main__":
    main()
