"""One test from a seed and a mode: mode 1 a few products and customers
with small amounts, mode 2 up to 1000 of each, mode 3 one large stock
and customers who want one unit, with a few who want everything and
call home again after each of them."""

import random
import string
import sys

LIMIT = 1000
FEW = 6
NAME = 20
RARE = 0.05


def name(rng, short):
    length = rng.randint(1, 2 if short else NAME)
    return "".join(rng.choice(string.ascii_lowercase[:FEW] if short else string.ascii_lowercase)
                   for _ in range(length))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    short = mode != 2
    m = 1 if mode == 3 else rng.randint(1, FEW if short else LIMIT)
    n = rng.randint(1, FEW * 2 if mode == 1 else LIMIT)
    top = FEW if mode == 1 else LIMIT
    products = set()
    while len(products) < m:
        products.add(name(rng, short))
    products = sorted(products)
    rng.shuffle(products)
    print(m)
    for product in products:
        print("%d of %s" % (LIMIT if mode == 3 else rng.randint(1, top), product))
    print(n)
    for _ in range(n):
        known = mode == 3 or rng.random() < 0.9
        product = rng.choice(products) if known else name(rng, short)
        if mode == 3:
            # a rare buyer of everything among buyers of a single unit,
            # each of whom changes the stock and makes the big one call again
            wanted = LIMIT if rng.random() < RARE else 1
        else:
            wanted = rng.randint(1, top)
        print("%d of %s" % (wanted, product))


main()
