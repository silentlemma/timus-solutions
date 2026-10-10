"""A position of the card game: a seed, the number of turn-skipping cards
(6, 7, ace, king of spades) in the hand, the number of jokers in it and the
number of other cards in it. The face-up card is drawn from what is left
of the 54-card deck; a queen gets an announced suit and a joker gets the
card it stands for."""

import random
import sys

SUITS = "SCDH"
VALUES = "23456789TJQKA"
SKIPS = [v + s for v in "67A" for s in SUITS] + ["KS"]
JOKERS = 2


def spec(rng, card):
    return card + rng.choice(SUITS) if card[0] == "Q" else card


def main():
    seed, skips, jokers, others = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    plain = [v + s for v in VALUES for s in SUITS if v + s not in SKIPS]
    rng.shuffle(plain)
    skip_pool = SKIPS[:]
    rng.shuffle(skip_pool)
    hand = skip_pool[:skips] + plain[:others] + ["*"] * jokers
    rng.shuffle(hand)
    rest = skip_pool[skips:] + plain[others:] + ["*"] * (JOKERS - jokers)
    top = rng.choice(rest)
    if top == "*":
        top = "*" + spec(rng, rng.choice([v + s for v in VALUES for s in SUITS]))
    else:
        top = spec(rng, top)
    sys.stdout.write(" ".join(hand) + "\n" + top + "\n")


if __name__ == "__main__":
    main()
