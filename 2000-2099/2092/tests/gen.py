"""Generate one valid instance from MODE and SEED.

Modes: 1 small, 2 medium, 3 maximum random, 4 fillers at every discount,
5 tied deltas, 6 free student tickets, 7 a free subscription,
8 maximum prices and a large total, 9 dominated offers, 10 one large subscription,
11 expensive fillers at every discount.
"""

import random
import sys

MIN_COUNT = 2
MAX_COUNT = 100_000
SMALL_COUNT = 12
MEDIUM_MIN = 200
MEDIUM_MAX = 1_000
MIN_PRICE = 100
MAX_PRICE = 50_000
PERCENT = 100
TIE_GROUPS = 4
TIE_STEP = PERCENT // TIE_GROUPS

SMALL = 1
MEDIUM = 2
MAX_RANDOM = 3
FILLERS = 4
TIES = 5
FREE_STUDENTS = 6
FREE_SUBSCRIPTION = 7
MAX_TOTAL = 8
DOMINATED = 9
ONE_OFFER = 10
STRESS = 11


def main():
    mode, seed = map(int, sys.argv[1:])
    if not SMALL <= mode <= STRESS:
        raise ValueError(f"mode must be between {SMALL} and {STRESS}")
    rng = random.Random(seed)
    if mode == SMALL:
        n = rng.randint(MIN_COUNT, SMALL_COUNT)
        m = rng.randint(1, SMALL_COUNT)
    elif mode == MEDIUM:
        n = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        m = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
    else:
        n = m = MAX_COUNT
    if mode == ONE_OFFER:
        m = 1

    tickets = [(rng.randint(MIN_PRICE, MAX_PRICE), rng.randint(0, PERCENT)) for _ in range(n)]
    offers = [(rng.randint(MIN_COUNT, n), rng.randint(1, PERCENT - 1)) for _ in range(m)]

    if mode == SMALL:
        offers = [(k, rng.randint(1, PERCENT)) for k, _ in offers]
    elif mode == FILLERS:
        tickets = [(s, i % PERCENT + 1) for i, (s, _) in enumerate(tickets)]
        offers = []
        for i in range(m):
            p = i % (PERCENT - 1) + 1
            k = (p + 1) * (n // PERCENT)
            offers.append((k, p))
    elif mode == TIES:
        tickets = [(MIN_PRICE, (i % TIE_GROUPS + 1) * TIE_STEP) for i in range(n)]
        offers = []
        for i in range(m):
            p = i % (PERCENT - 1) + 1
            offers.append(((p + 1) * (n // PERCENT), p))
    elif mode == FREE_STUDENTS:
        tickets = [(s, PERCENT) for s, _ in tickets]
    elif mode == FREE_SUBSCRIPTION:
        offers[-1] = (n, PERCENT)
    elif mode == MAX_TOTAL:
        tickets = [(MAX_PRICE, 0)] * n
        offers = [(k, 1) for k, _ in offers]
    elif mode == DOMINATED:
        offers = []
        for i in range(m):
            p = i % (PERCENT - 1) + 1
            k = max(MIN_COUNT, n * p // PERCENT)
            if i >= PERCENT:
                k = rng.randint(k, n)
            offers.append((k, p))
    elif mode == ONE_OFFER:
        tickets = [(s, i % (PERCENT + 1)) for i, (s, _) in enumerate(tickets)]
        offers = [(n, rng.randint(1, PERCENT - 1))]
    elif mode == STRESS:
        tickets = [(MIN_PRICE, 0)] * (n // 10)
        tickets.extend((MIN_PRICE, d) for d in range(1, PERCENT))
        tickets.extend([(MAX_PRICE, PERCENT)] * (n - len(tickets)))
        offers = []
        for i in range(m):
            p = i % (PERCENT - 1) + 1
            offers.append((n - PERCENT + p, p))
        rng.shuffle(tickets)
        rng.shuffle(offers)

    lines = [f"{n} {m}"]
    lines.extend(f"{s} {d}" for s, d in tickets)
    lines.extend(f"{k} {p}" for k, p in offers)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
