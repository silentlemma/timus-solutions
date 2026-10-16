"""One test from a seed and a mode: four piles holding ranks 2 to A from
top to bottom, the suits of each rank dealt among the piles; mode 1
any deal, mode 2 suits that stay in place with a small chance to be
shuffled at each rank, mode 3 suits that rotate among the piles at
some ranks."""

import random
import sys

RANKS = "23456789TJQKA"
SUITS = "SCDH"
RARE = 0.2


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    order = list(SUITS)
    rng.shuffle(order)
    columns = []
    for _ in RANKS:
        if mode == 1 or rng.random() < RARE:
            if mode == 3:
                shift = rng.randint(1, len(order) - 1)
                order = order[shift:] + order[:shift]
            else:
                rng.shuffle(order)
        columns.append(order[:])
    for pile in range(len(SUITS)):
        print(" ".join(rank + columns[r][pile] for r, rank in enumerate(RANKS)))


main()
