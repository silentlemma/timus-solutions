"""One test from a seed and a mode. Mode 1 is a few small animals, mode 2
is 10000 animals on different random rays whose kinds change often, mode 3
puts many animals on few rays (multiples of the same direction), mode 4
alternates the kinds on the 10000 rays (10000, b), mode 5 is a random herd
with one animal of the wrong kind on a used ray. Mode 6 puts 10000 camels
on one interior ray, mode 7 alternates on 9999 rays with one repeated
animal, and mode 8 has random animals separated just above the diagonal."""

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
    elif mode == 6:
        animals.append((LARGEST, LARGEST, 1))
        for _ in range(LARGEST - 1):
            k = rng.randint(1, LARGEST)
            animals.append((k, k, 1))
    elif mode == 7:
        for b in range(LARGEST - 1):
            animals.append((LARGEST, b, 1 + b % 2))
        animals.append(animals[(LARGEST - 1) // 2])
    elif mode == 8:
        animals = [(LARGEST, 0, 2), (0, LARGEST, 1), (LARGEST, LARGEST, 2)]
        while len(animals) < LARGEST:
            a, b = rng.randint(0, LARGEST), rng.randint(0, LARGEST)
            if a or b:
                animals.append((a, b, 1 if b > a else 2))
    else:
        for _ in range(LARGEST - 1):
            animals.append((rng.randint(1, LARGEST), rng.randint(1, LARGEST), rng.randint(1, 2)))
        a, b, c = rng.choice(animals)
        animals.append((a, b, 3 - c))
    rng.shuffle(animals)
    lines = [str(len(animals))] + ["%d %d %d" % x for x in animals]
    print("\n".join(lines))


main()
