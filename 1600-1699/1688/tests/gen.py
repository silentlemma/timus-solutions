"""One test from a seed and a mode: mode 1 a few small bills, mode 2 the
most and largest bills against the largest fee, mode 3 a fee met
exactly (the share equals n but does not exceed it), mode 4 a fee
passed on the last visit, mode 5 a threshold just above the signed
32-bit limit met exactly and then exceeded by one before later bills."""

import random
import sys

MOST_N = 2 * 10 ** 9
MOST_M = 3000
MOST_BILL = 2 * 10 ** 6
SHARES = 3


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        m = rng.randint(0, 10)
        bills = [rng.randint(1, 100) for _ in range(m)]
        n = rng.randint(1, 200)
    elif mode == 5:
        n = ((1 << 31) + 1) // SHARES
        remaining = SHARES * n
        bills = []
        while remaining > MOST_BILL:
            bill = rng.randint(MOST_BILL // 2, MOST_BILL)
            bills.append(bill)
            remaining -= bill
        bills.extend([remaining, 1])
        bills.extend(rng.randint(1, MOST_BILL) for _ in range(MOST_M - len(bills)))
    else:
        m = MOST_M
        bills = [rng.randint(MOST_BILL // 2, MOST_BILL) for _ in range(m)]
        if mode == 2:
            n = MOST_N
        else:
            k = rng.randint(1, m)
            reach = sum(bills[:k])
            reach -= reach % SHARES
            n = reach // SHARES if mode == 3 else (sum(bills) - 1) // SHARES
    print(n, len(bills))
    for b in bills:
        print(b)


main()
