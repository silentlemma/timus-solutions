"""A hand: a seed and a mode. Mode 1 draws up to 8 cards in four suits,
mode 2 twenty cards in all ten suits, mode 3 twenty cards with one more
blue suit than yellow. Hands always keep the blue and yellow suit counts
within one of each other."""

import random
import sys

CARDS = 20
TOP = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        blue, yellow = rng.sample([1, 3], rng.randint(1, 2)), rng.sample([2, 4], rng.randint(0, 2))
        n = rng.randint(1, 8)
    elif mode == 2:
        blue, yellow, n = [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], CARDS
    else:
        blue, yellow, n = rng.sample([1, 3, 5, 7, 9], 4), rng.sample([2, 4, 6, 8, 10], 3), CARDS
    while abs(len(blue) - len(yellow)) > 1:
        yellow.append(rng.choice([s for s in range(2, 11, 2) if s not in yellow]))
    suits = blue + yellow
    n = max(n, len(suits))
    cards = {(rng.randint(1, TOP), s) for s in suits}
    while len(cards) < n:
        cards.add((rng.randint(1, TOP), rng.choice(suits)))
    cards = list(cards)
    rng.shuffle(cards)
    sys.stdout.write("%d\n%s\n" % (len(cards), "\n".join("%d %d" % c for c in cards)))


if __name__ == "__main__":
    main()
