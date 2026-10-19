"""Planets and tourists from a seed and a mode: mode 1 a few planets
close to the star, 2 the most planets and tourists with many pieces,
3 one piece holding every planet, so that all ranges fall inside it,
4 every planet of its own race, 5 a few races and gaps right at d,
6 tourists whose ranges are mostly empty or cover everything."""

import random
import sys

MOST = 100000
LIMIT = 10 ** 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m, top = rng.randint(1, 10), rng.randint(1, 10), 30
        s, d = rng.randint(1, 4), rng.randint(1, 6)
    else:
        n, m, top = MOST, MOST, LIMIT
        s = MOST if mode == 4 else rng.choice((3, 50, 1000))
        d = {2: 15, 3: LIMIT, 5: 10}.get(mode, rng.randint(1, 30))
    if mode == 5:
        dist, at = [], 0
        while len(dist) < n:
            at += rng.choice((d, d, d + 1))
            dist.append(at)
    else:
        dist = rng.sample(range(1, top + 1), n)
    planets = [(x, rng.randint(1, s)) for x in dist]
    if mode == 4:
        races = rng.sample(range(1, s + 1), n)
        planets = [(x, r) for (x, _), r in zip(planets, races)]
    rng.shuffle(planets)
    span = max(dist)
    tourists = []
    for _ in range(m):
        if mode == 6 and rng.random() < 0.5:
            a = rng.choice((1, span, rng.randint(1, LIMIT)))
            b = a if rng.random() < 0.5 else LIMIT
        else:
            a, b = sorted(rng.randint(1, span + 1) for _ in range(2))
        tourists.append((a, b))
    print(n, s, d)
    print("\n".join("%d %d" % p for p in planets))
    print(m)
    print("\n".join("%d %d" % t for t in tourists))


main()
