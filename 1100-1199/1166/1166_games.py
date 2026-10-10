import sys

SUITS = "SCDH"
# the cards after which the second player loses the turn: 6, 7, ace, king
# of spades
SKIPS = [v + s for v in "67A" for s in SUITS] + ["KS"]


def covers(card, top):
    # top is (value, suit, announced suit or None for a non-queen)
    if top[2]:
        return card[1] == top[2]
    return card[1] == top[1] or card[0] == top[0]


def parse_top(tok):
    tok = tok.lstrip("*")
    return tok[0], tok[1], tok[2] if tok[0] == "Q" else None


def main():
    lines = sys.stdin.read().split("\n")
    hand = lines[0].split()
    top = parse_top(lines[1].strip())
    real = [c for c in hand if c in SKIPS]
    jokers = hand.count("*")
    others = [c for c in hand if c != "*" and c not in SKIPS]
    if len(others) > 1:
        print("NO")
        return
    last = others[0] if others else None
    failed = set()

    def finish(mask, used, top):
        # the cards still to lay after top, or None; every card but the last
        # must make the opponent skip, and the last may be anything
        rest = len(real) - bin(mask).count("1") + jokers - used + (last is not None)
        if rest == 1:
            if last:
                return [last + last[1] if last[0] == "Q" else last] if covers(last, top) else None
            if used < jokers:
                return ["*2" + (top[2] or top[1])]
            card = next(c for k, c in enumerate(real) if not mask >> k & 1)
            return [card] if covers(card, top) else None
        key = (mask, used, top)
        if key in failed:
            return None
        for k, card in enumerate(real):
            if not mask >> k & 1 and covers(card, top):
                tail = finish(mask | 1 << k, used, (card[0], card[1], None))
                if tail:
                    return [card] + tail
        if used < jokers:
            for card in SKIPS:
                if covers(card, top):
                    tail = finish(mask, used + 1, (card[0], card[1], None))
                    if tail:
                        return ["*" + card] + tail
        failed.add(key)
        return None

    order = finish(0, 0, top)
    print("YES\n" + " ".join(order) if order else "NO")


main()
