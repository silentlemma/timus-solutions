"""Officials and their reception days: a seed and a mode. Mode 1 gives 100
officials, a week of 100 days and random papers needed, mode 2 a chain of
100 documents where each comes a day too late in the week, mode 3 a cycle
among the papers that are needed, mode 4 a cycle that is broken by a
paper already in hand. Mode 5 lets 100 officials share a short week, so
the order of visits matters, and mode 6 does the same with a few."""

import random
import sys

N = 100
WEEK = 100
CHANCE = 0.05  # how often one document needs another in mode 1
SHORT_WEEK = 7
FEW = 6


def shared(rng, mode):
    """Officials sharing reception days in a short week."""
    n = N if mode == 5 else rng.randint(1, FEW)
    week = rng.randint(1, SHORT_WEEK)
    chance = CHANCE if mode == 5 else rng.random()
    days = [rng.randint(1, week) for _ in range(n)]
    order = list(range(1, n + 1))
    rng.shuffle(order)
    needs = {d: [e for e in order[:i] if rng.random() < chance] for i, d in enumerate(order)}
    held = [d for d in order if rng.random() < CHANCE]
    wanted = rng.sample(order, rng.randint(1, n))
    return n, week, days, needs, rng.randint(1, week), held, wanted


def distinct(rng, mode):
    """Every official on a different day of a week of 100 days."""
    days = rng.sample(range(1, WEEK + 1), N)
    order = list(range(1, N + 1))
    rng.shuffle(order)
    needs = {d: [] for d in order}
    if mode == 2:
        days = [0] * N
        for i, d in enumerate(order):
            days[d - 1] = (WEEK - i) % WEEK + 1
            if i > 0:
                needs[d] = [order[i - 1]]
    else:
        for i, d in enumerate(order):
            needs[d] = [e for e in order[:i] if rng.random() < CHANCE]
    held, wanted = [], [order[-1]] + rng.sample(order, 3)
    if mode in (3, 4):
        # the first document of the order needs the last one, closing a loop
        needs[order[0]].append(order[-1])
        wanted = [order[0]]
        if mode == 4:
            held = [order[-1]]
    elif mode == 1:
        held = rng.sample(order, 10)
    today = rng.randint(1, WEEK)
    return N, WEEK, days, needs, today, held, wanted


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    make = shared if mode >= 5 else distinct
    n, week, days, needs, today, held, wanted = make(rng, mode)
    print(n, week)
    print(*days)
    for d in range(1, n + 1):
        print(*needs[d], 0)
    print(today)
    print(*held, 0)
    print(*wanted, 0)


main()
