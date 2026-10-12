"""Factories and an order: a seed and a mode. Mode 1 gives 1000 factories
of up to 100 brooms with random prices and an order of 1000, mode 2
factories whose last broom is cheaper than the first, mode 3 factories
that cannot make the whole order, mode 4 prices that tie a lot."""

import random
import sys

N = 1000
TOP = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = 30 if mode == 3 else N
    factories = []
    for _ in range(n):
        k = rng.randint(1, 100 if mode != 3 else 20)
        p, q = rng.randint(0, TOP), rng.randint(0, TOP)
        if mode == 2:
            p, q = max(p, q), min(p, q)
        if mode == 4:
            p, q = rng.choice([0, 500, TOP]), rng.choice([0, 500, TOP])
        factories.append((k, p, q))
    print(n, TOP)
    for f in factories:
        print(*f)


main()
