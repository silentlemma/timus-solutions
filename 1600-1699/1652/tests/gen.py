"""One test from a seed and a mode: mode 1 a few banks in two countries,
mode 2 1000 banks and 10000 contracts in a few countries, mode 3 one
country where every bank is rich and debts are few, mode 4 one country
of poor banks and many expensive debts, mode 5 one country where every
bank lends exactly once, mode 6 nearly all debts owed by a few banks,
mode 7 ten lenders, poor banks and only a few debts cheap enough."""

import random
import sys

MOST_BANKS = 1000
MOST_DEBTS = 10000
TOP = 10**9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m, countries, top = rng.randint(2, 5), rng.randint(0, 5), 2, 10
    elif mode == 2:
        n, m, countries, top = MOST_BANKS, MOST_DEBTS, rng.randint(1, 5), TOP
    elif mode == 3:
        n, m, countries, top = MOST_BANKS, rng.randint(100, 900), 1, TOP
    elif mode == 5:
        n, m, countries, top = MOST_BANKS, MOST_BANKS, 1, TOP
    elif mode == 7:
        n, m, countries, top = MOST_BANKS, MOST_DEBTS, 1, TOP
    else:
        n, m, countries, top = MOST_BANKS, MOST_DEBTS, rng.randint(1, 2), TOP
    banks = []
    for _ in range(n):
        if mode == 3:
            cash = rng.randint(top // 2, top)
        elif mode in (4, 7):
            cash = rng.randint(0, top // 100)
        else:
            cash = rng.randint(0, top)
        banks.append((rng.randint(1, countries), cash))
    contracts = []
    lenders = rng.sample(range(n), n)
    for i in range(m):
        a, b = rng.sample(range(n), 2)
        if mode == 5:
            a = lenders[i]
            b = rng.choice([x for x in (a - 1, a + 1, rng.randrange(n)) if 0 <= x < n and x != a])
        if mode == 6:
            b = rng.randrange(3)
            if a == b:
                a = (a + 3) % n
        if mode == 7:
            a = rng.randrange(10)
            b = rng.randrange(10, n)
        if mode in (4, 7):
            amount = rng.randint(top // 200, top)
        else:
            amount = rng.randint(1, top)
        contracts.append((a + 1, b + 1, amount))
    print(n)
    for c, v in banks:
        print(c, v)
    print(m)
    for a, b, s in contracts:
        print(a, b, s)


main()
