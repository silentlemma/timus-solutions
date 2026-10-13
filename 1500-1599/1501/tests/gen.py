"""One test from a seed and a mode, with N red and N black cards. Mode 1
shuffles 1000 + 1000 cards at random, mode 2 deals a balanced sequence
(each pair of moves takes one red and one black card) in a random merge
order, so an answer exists, mode 3 alternates the colours in both
piles, mode 4 puts all red cards of the first pile on top, mode 5 is
small."""

import random
import sys

LARGEST = 1000
SMALL = 6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(4, SMALL) if mode == 5 else LARGEST
    if mode == 2:
        colours = []
        for _ in range(n):
            pair = ["1", "0"]
            rng.shuffle(pair)
            colours += pair
        order = ["1"] * n + ["2"] * n
        rng.shuffle(order)
        piles = {"1": [], "2": []}
        for pile, colour in zip(order, colours):
            piles[pile].append(colour)
        first, second = piles["1"], piles["2"]
    elif mode == 3:
        first = ["1" if i % 2 == 0 else "0" for i in range(n)]
        second = ["0" if i % 2 == 0 else "1" for i in range(n)]
    elif mode == 4:
        half = n // 2
        first = ["1"] * half + ["0"] * (n - half)
        second = ["1"] * (n - half) + ["0"] * half
    else:
        cards = ["1"] * n + ["0"] * n
        rng.shuffle(cards)
        first, second = cards[:n], cards[n:]
    print(n)
    print("".join(first))
    print("".join(second))


main()
