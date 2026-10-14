"""One test from a seed and a mode. Mode 1 takes 5000 points (x, x^2 mod p)
for a prime p near 10^8, which have no three on a line, mode 2 the same
on a smaller prime, mode 3 5 to 8 random points in a small box, mode 4
nine of them, mode 5 5000 points on a parabola."""

import random
import sys

LARGEST = 5000
TOP = 10**8
SMALL_PRIME_TOP = 10**4
BOX = 20
FEW = 8
NINE = 9


def is_prime(v):
    return v > 1 and all(v % d for d in range(2, int(v**0.5) + 1))


def no_three_on_a_line(points):
    for i, a in enumerate(points):
        for j in range(i):
            b = points[j]
            for c in points[:j]:
                if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]):
                    return False
    return True


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (1, 2):
        p = (
            rng.randint(TOP // 2, TOP // 2 + TOP // 4)
            if mode == 1
            else rng.randint(LARGEST, SMALL_PRIME_TOP)
        )
        while not is_prime(p):
            p += 1
        xs = rng.sample(range(p), LARGEST)
        points = [(x - p // 2, x * x % p - p // 2) for x in xs]
    elif mode in (3, 4):
        n = NINE if mode == 4 else rng.randint(5, FEW)
        while True:
            points = [(rng.randint(-BOX, BOX), rng.randint(-BOX, BOX)) for _ in range(n)]
            if len(set(points)) == n and no_three_on_a_line(points):
                break
    else:
        xs = rng.sample(range(-LARGEST, LARGEST), LARGEST)
        points = [(x, x * x) for x in xs]
    if rng.randint(0, 1):
        points = [(y, x) for x, y in points]
    print(len(points))
    for x, y in points:
        print(x, y)


main()
