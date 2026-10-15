"""One test from a seed and a mode: mode 1 a small city, mode 2 any
sizes up to 1000, mode 3 the new building touching the city border, mode
4 the buildings almost touching each other, mode 5 radii that differ by
one."""

import random
import sys

LIMIT = 1000
SMALL = 20


def fits(big, small, near, x, y, mode):
    dist2 = x * x + y * y
    apart = dist2 > (small + near) ** 2
    inside = (big - near) ** 2 >= dist2
    if mode == 3:
        inside = inside and (big - near - 1) ** 2 < dist2
    if mode == 4:
        apart = apart and dist2 <= (small + near + 1) ** 2
    return apart and inside


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else LIMIT
    while True:
        big = rng.randint(3, top)
        small = rng.randint(1, big - 2)
        near = rng.randint(small + 1, big - 1)
        if mode == 5:
            near = small + 1
        reach = big - near
        x = rng.randint(-reach, reach)
        y = rng.randint(-reach, reach)
        if near < big and fits(big, small, near, x, y, mode):
            break
    print(big, small, near)
    print(x, y)


main()
