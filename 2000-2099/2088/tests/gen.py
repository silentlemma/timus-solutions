"""Deterministic valid decks: python gen.py MODE SEED.

Modes: 1 small, 2 random full deck, 3 dense full deck, 4 all colors,
5 polynomial stress, 6 one ordinary color, 7 empty draws or reveals,
8 all cards drawn, 9 all remaining cards revealed, 10 near-equal probabilities.
"""

import random
import sys

MAX_CARDS = 100
MAX_COLORS = 100
SMALL_CARDS = 10
SMALL_COLORS = 6
DENSE_COLORS = 5
INITIAL_DIVISOR = 5
STRESS_ZEROS = 17
STRESS_FIRST = 41
STRESS_SECOND = 42
STRESS_DRAW = 83
STRESS_REVEAL = 8
STRESS_MARGIN = 30
NEAR_ZERO = 32
NEAR_FIRST = 35
NEAR_SECOND = 33
NEAR_DRAW = 0
NEAR_REVEAL = 33
SMALL = 1
RANDOM_FULL = 2
DENSE = 3
ALL_COLORS = 4
STRESS = 5
ONE_COLOR = 6
EMPTY_STAGE = 7
DRAW_ALL = 8
REVEAL_ALL = 9
NEAR_EQUAL = 10


def generate(mode, seed):
    rng = random.Random(seed)
    k = rng.randint(1, SMALL_COLORS)
    size = rng.randint(0, SMALL_CARDS)
    if mode != SMALL:
        size = MAX_CARDS
    if mode == RANDOM_FULL:
        k = rng.randint(1, MAX_COLORS)
    elif mode == DENSE:
        k = rng.randint(2, DENSE_COLORS)
    elif mode == ALL_COLORS:
        k = MAX_COLORS
    elif mode == ONE_COLOR:
        k = 1
    elif mode in (STRESS, NEAR_EQUAL):
        k = 2

    cards = [0] * (k + 1)
    for _ in range(size):
        cards[rng.randrange(k + 1)] += 1
    initial = [rng.randint(0, count) for count in cards]
    if mode == DENSE:
        initial = [rng.randint(0, count // INITIAL_DIVISOR) for count in cards]
    elif mode == ALL_COLORS:
        cards = [1] * MAX_COLORS + [0]
        rng.shuffle(cards)
        initial = [0] * (k + 1)
    elif mode == STRESS:
        cards = [STRESS_ZEROS, STRESS_FIRST, STRESS_SECOND]
        initial = [0, 0, 0]
    elif mode == NEAR_EQUAL:
        cards = [NEAR_ZERO, NEAR_FIRST, NEAR_SECOND]
        initial = [NEAR_ZERO, 0, 0]

    remaining = sum(cards) - sum(initial)
    t = rng.randint(0, remaining)
    y = rng.randint(0, remaining - t)
    possible = min(MAX_CARDS, initial[0] + t + max(initial[1:]))
    x = rng.randint(0, possible)
    if mode == STRESS:
        t, y, x = STRESS_DRAW, STRESS_REVEAL, STRESS_MARGIN
    elif mode == EMPTY_STAGE:
        if seed % 2:
            t = 0
            y = rng.randint(0, remaining)
        else:
            y = 0
    elif mode == DRAW_ALL:
        t, y = remaining, 0
    elif mode == REVEAL_ALL:
        y = remaining - t
    elif mode == NEAR_EQUAL:
        t, y = NEAR_DRAW, NEAR_REVEAL
        x = seed % 2
    elif mode not in (SMALL, RANDOM_FULL, DENSE, ALL_COLORS, ONE_COLOR):
        raise ValueError("unknown mode")
    return k, t, cards, initial, x, y


def main():
    mode, seed = map(int, sys.argv[1:])
    k, t, cards, initial, x, y = generate(mode, seed)
    print(k, t)
    print(*cards)
    print(*initial)
    print(x, y)


if __name__ == "__main__":
    main()
