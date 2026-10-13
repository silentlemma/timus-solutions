"""One test from a seed and a mode. Mode 1 is a few small animals, mode 2
is 10000 animals on different random rays whose kinds change often, mode 3
puts many animals on few rays (multiples of the same direction), mode 4
alternates the kinds on the 10000 rays (10000, b), mode 5 is a random herd
with one animal of the wrong kind on a used ray."""

import random
import sys
from math import gcd

LARGEST = 10000
SMALL = 8
SMALL_SIDE = 6
FEW_RAYS = 7


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    animals = []
    if mode == 1:
        for _ in range(rng.randint(1, SMALL)):
            a, b = rng.randint(0, SMALL_SIDE), rng.randint(0, SMALL_SIDE)
            if a == b == 0:
                a = 1
            animals.append((a, b, rng.randint(1, 2)))
    elif mode == 2:
        seen = set()
        while len(animals) < LARGEST:
            a, b = rng.randint(0, LARGEST), rng.randint(1, LARGEST)
            g = gcd(a, b)
            if (a // g, b // g) not in seen:
                seen.add((a // g, b // g))
                animals.append((a, b, rng.randint(1, 2)))
    elif mode == 3:
        rays = []
        while len(rays) < FEW_RAYS:
            a, b = rng.randint(0, SMALL_SIDE), rng.randint(0, SMALL_SIDE)
            if (a, b) != (0, 0) and all(a * q - b * p for p, q, _ in rays):
                rays.append((a, b, rng.randint(1, 2)))
        for _ in range(LARGEST):
            a, b, c = rng.choice(rays)
            k = rng.randint(1, LARGEST // max(a, b))
            animals.append((a * k, b * k, c))
    elif mode == 4:
        for b in range(LARGEST):
            animals.append((LARGEST, b, 1 + b % 2))
    else:
        for _ in range(LARGEST - 1):
            animals.append((rng.randint(1, LARGEST), rng.randint(1, LARGEST), rng.randint(1, 2)))
        a, b, c = rng.choice(animals)
        animals.append((a, b, 3 - c))
    rng.shuffle(animals)
    lines = [str(len(animals))] + ["%d %d %d" % x for x in animals]
    print("\n".join(lines))


main()
