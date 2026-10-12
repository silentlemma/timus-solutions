"""100 cities: a seed and a mode. Mode 1 gives cities all over the field,
mode 2 all of them close together so that every pair gives places to
try, mode 3 cities on a circle of integer points of radius 5 times k
with the bomb reach exactly that radius, mode 4 cities on a line."""

import random
import sys

N = 100
TOP = 10000
TRIPLES = [(0, 5), (3, 4), (4, 3), (5, 0)]  # integer points at distance 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    cities = set()
    if mode == 3:
        k = rng.randint(1, 1000)
        cx, cy = rng.randint(-TOP // 2, TOP // 2), rng.randint(-TOP // 2, TOP // 2)
        for a, b in TRIPLES:
            for sa in (1, -1):
                for sb in (1, -1):
                    cities.add((cx + sa * a * k, cy + sb * b * k))
        r = rng.randint(1, 100)
        big = 5 * k + r
    else:
        r = rng.randint(1, 100)
        big = rng.randint(r, TOP)
    while len(cities) < N:
        if mode == 2:
            spread = max(1, big - r)
            cities.add((rng.randint(-spread, spread), rng.randint(-spread, spread)))
        elif mode == 4:
            cities.add((rng.randint(-TOP, TOP), 7))
        else:
            cities.add((rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)))
    cities = list(cities)
    rng.shuffle(cities)
    print(len(cities))
    for x, y in cities:
        print(x, y)
    print(big, r)


main()
