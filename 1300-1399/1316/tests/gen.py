"""An exchange log: a seed and a mode. Mode 1 gives a short log with few
prices, mode 2 100000 operations over all prices, mode 3 100000
operations over a handful of prices with large sales, mode 4 prices
written with one decimal or none, mode 5 50000 bids and then 49999
sales that each sell every bid: more than 2^31 pieces in all."""

import random
import sys

TOP = 10**6  # 10000.00 in cents
OPS = 99999
SALE_MAX = 100000


def show(cents, rng, mode):
    if mode == 4 and cents % 100 == 0 and rng.random() < 0.5:
        return str(cents // 100)
    if mode == 4 and cents % 10 == 0 and rng.random() < 0.5:
        return "%d.%d" % (cents // 100, cents % 100 // 10)
    return "%d.%02d" % divmod(cents, 100)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        prices, ops = [rng.randint(1, 500) for _ in range(5)], rng.randint(1, 30)
    elif mode == 3:
        prices, ops = [rng.randint(1, TOP) for _ in range(5)], OPS
    elif mode == 4:
        prices, ops = [100 * rng.randint(1, 100) + rng.choice((0, 50)) for _ in range(50)], 2000
    else:
        prices, ops = None, OPS
    if mode == 5:
        bids = ["BID " + show(rng.randint(1, TOP), rng, mode) for _ in range(OPS // 2 + 1)]
        print("\n".join(bids + ["SALE 0.01 %d" % SALE_MAX] * (OPS // 2) + ["QUIT"]))
        return
    active, lines = [], []
    for _ in range(ops):
        r = rng.random()
        price = rng.choice(prices) if prices else rng.randint(1, TOP)
        if r < 0.5 or not active:
            active.append(price)
            lines.append("BID " + show(price, rng, mode))
        elif r < 0.7:
            gone = active.pop(rng.randrange(len(active)))
            lines.append("DEL " + show(gone, rng, mode))
        else:
            k = rng.randint(1, SALE_MAX if mode == 3 else 10)
            lines.append("SALE %s %d" % (show(price, rng, mode), k))
    print("\n".join(lines + ["QUIT"]))


main()
