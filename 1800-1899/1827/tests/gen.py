"""One chronicle from a seed and a mode: mode 1 a short sky with few
star counts, mode 2 the longest sky with few star counts and wars of
every length, mode 3 the longest sky of a single star count, mode 4
the longest sky of random counts with a few thousand wars, mode 5 the
same with the most wars, all made of random counts from the sky. Some
wars are taken from the sky, the rest are random. Mode 6 uses the largest
sky and book, repeated first-day counts and absent last-day counts,
except for one two-day match at the oldest edge."""

import random
import sys

LIMIT = 100000
TOP = 200000000
LONGEST = 50
SMALL = 30


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        stars = [0] * (LIMIT - 1) + [TOP]
        wars = [(0, rng.randint(1, TOP - 1), rng.randint(2, LONGEST))
                for _ in range(LIMIT)]
        wars[rng.randrange(LIMIT)] = (TOP, 0, 2)
        print(LIMIT)
        print(*stars)
        print(LIMIT)
        print("\n".join(f"{x} {y} {d}" for x, y, d in wars))
        return
    n = rng.randint(2, SMALL) if mode == 1 else LIMIT
    m = rng.randint(1, SMALL) if mode == 1 else LIMIT
    if mode == 4:
        m = rng.randint(100, 3000)
    if mode == 3:
        value = rng.randint(0, TOP)
        stars = [value] * n
    elif mode >= 4:
        stars = [rng.randint(0, TOP) for _ in range(n)]
    else:
        palette = [rng.randint(0, TOP) for _ in range(rng.randint(1, 4))]
        stars = [rng.choice(palette) for _ in range(n)]
    wars = []
    for _ in range(m):
        d = rng.randint(2, LONGEST)
        if d <= n and mode != 5 and rng.random() < 0.5:
            k = rng.randint(0, n - d)
            wars.append((stars[k + d - 1], stars[k], d))
        else:
            wars.append((rng.choice(stars), rng.choice(stars), d))
    print(n)
    print(*stars)
    print(m)
    print("\n".join(f"{x} {y} {d}" for x, y, d in wars))


main()
