"""One test from a seed and a mode: n operators and k priced routes.
Mode 1 a few operators with dense routes, mode 2 up to 100000 random
routes among a few hundred operators, mode 3 10^4 operators where a few
cover half of everybody each, mode 4 random routes that rarely let a
pair cover everybody, mode 5 many repeated routes with different
prices, mode 6 maximum n and k split between three indispensable senders,
mode 7 maximum n and k with a 9998-target sender and a two-target partner.
Modes 6 and 7 use seeded route prices, duplicates, and input shuffling."""

import random
import sys

LIMIT_N = 10 ** 4
LIMIT_K = 10 ** 5
TOP = 10 ** 9
FEW = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = rng.choice([10, 1000, TOP])
    routes = []
    if mode == 1:
        n = rng.randint(2, FEW)
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if rng.random() < 0.6:
                    routes.append((x, y, rng.randint(1, top)))
    elif mode == 2:
        n = rng.randint(2, 400)
        k = rng.randint(1, LIMIT_K)
        routes = [(rng.randint(1, n), rng.randint(1, n), rng.randint(1, top)) for _ in range(k)]
    elif mode == 3:
        n = LIMIT_N
        big = rng.sample(range(1, n + 1), FEW)
        for x in big:
            share = rng.randint(n // 2, n)
            for y in rng.sample(range(1, n + 1), share):
                if len(routes) < LIMIT_K - 1000:
                    routes.append((x, y, rng.randint(1, top)))
        while len(routes) < LIMIT_K:
            routes.append((rng.randint(1, n), rng.randint(1, n), rng.randint(1, top)))
    elif mode == 4:
        n = rng.randint(2, 50)
        k = rng.randint(1, n * n // 2)
        routes = [(rng.randint(1, n), rng.randint(1, n), rng.randint(1, top)) for _ in range(k)]
    elif mode == 6:
        n = LIMIT_N
        senders = rng.sample(range(1, n + 1), 3)
        for y in range(1, n + 1):
            routes.append((senders[(y - 1) % 3], y, rng.randint(1, top)))
        while len(routes) < LIMIT_K:
            x, y, _ = routes[rng.randrange(n)]
            routes.append((x, y, rng.randint(1, top)))
    elif mode == 7:
        n = LIMIT_N
        for y in range(1, n - 1):
            routes.append((n - 1, y, rng.randint(1, 100)))
        routes.extend([(n, n - 1, TOP - 2), (n, n, TOP - 1)])
        # Every other sender is present but reaches only the first target.
        for x in range(1, n - 1):
            routes.append((x, 1, rng.randint(1, TOP)))
        while len(routes) < LIMIT_K:
            routes.append((rng.randint(1, n - 2), 1, rng.randint(1, TOP)))
    else:
        n = rng.randint(2, FEW * 3)
        base = [(x, y) for x in range(1, n + 1) for y in range(1, n + 1) if rng.random() < 0.7]
        for _ in range(rng.randint(1, LIMIT_K // 10)):
            x, y = rng.choice(base)
            routes.append((x, y, rng.randint(1, top)))
    rng.shuffle(routes)
    print(n, len(routes))
    print("\n".join("%d %d %d" % r for r in routes))


main()
