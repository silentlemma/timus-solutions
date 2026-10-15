"""One test from a seed and a mode: mode 1 small hands and few
combinations, mode 2 the largest sizes with no common card shown, mode 3
the largest sizes with some common cards shown, mode 4 combinations of
single ranks only (pairs, threes, ...)."""

import random
import sys

RANKS = "23456789TJQKA"
MOST_C = 100
SMALL = 8  # combinations use at most this many cards


def combination(rng, cards):
    total = rng.randint(1, min(cards, SMALL))
    parts = []
    while total:
        x = rng.randint(1, total)
        parts.append(x)
        total -= x
    return sorted(parts, reverse=True)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m, k = rng.randint(2, 4), rng.randint(2, 4), rng.randint(1, 3)
        count = rng.randint(1, 6)
    else:
        n, m, k = rng.randint(2, 10), 10, 5
        count = MOST_C
    shown = 0 if mode == 2 else rng.randint(0, k)
    if mode == 4:
        combos = {(rng.randint(1, m + k),) for _ in range(count)}
    else:
        combos = {tuple(combination(rng, m + k)) for _ in range(count)}
    # roughly from easy to hard: fewer cards first, then flatter shapes
    combos = sorted(combos, key=lambda c: (sum(c), c))
    count = len(combos)
    print(n, m, k)
    print("".join(rng.choice(RANKS) for _ in range(m)))
    print("".join(rng.choice(RANKS) for _ in range(shown)))
    print(count)
    for c in combos:
        print(len(c), *c)


main()
