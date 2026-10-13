"""Planets: a seed and a mode, 1000 balls each. Mode 1 scatters small
balls, mode 2 is a chain along a line given in shuffled order, mode 3
makes clusters, mode 4 has every ball overlap every other, mode 5 is a
lattice of balls that only touch, with a few pairs pushed together.
Mode 6 makes 1000 isolated unit balls; mode 7 makes 500 separate overlapping
pairs of unit balls. Both use shuffled labels and reach coordinate borders."""

import random
import sys

K = 1000
TOP = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    balls = {}
    if mode == 1:
        while len(balls) < K:
            balls[tuple(rng.randint(-TOP, TOP) for _ in range(3))] = rng.randint(1, 100)
    elif mode == 2:
        for i in range(K):
            balls[(-TOP + 2 * i, 0, 0)] = rng.choice((2, 3))
    elif mode == 3:
        centres = [tuple(rng.randint(-900, 900) for _ in range(3)) for _ in range(50)]
        while len(balls) < K:
            cx, cy, cz = rng.choice(centres)
            p = (cx + rng.randint(-60, 60), cy + rng.randint(-60, 60), cz + rng.randint(-60, 60))
            balls[p] = rng.randint(1, 20)
    elif mode == 4:
        while len(balls) < K:
            balls[tuple(rng.randint(-500, 500) for _ in range(3))] = TOP
    elif mode == 6:
        for i in range(K):
            a, b, c = i % 10, i // 10 % 10, i // 100
            balls[(-TOP + 222 * a, -TOP + 222 * b, -TOP + 222 * c)] = 1
        # Include both opposite corners without introducing an overlap.
        del balls[(998, 998, 998)]
        balls[(TOP, TOP, TOP)] = 1
    elif mode == 7:
        for i in range(K // 2):
            a, b, c = i % 10, i // 10 % 10, i // 100
            x, y, z = -TOP + 222 * a, -TOP + 222 * b, -TOP + 500 * c
            balls[(x, y, z)] = 1
            balls[(x + 1, y, z)] = 1
    else:
        side, step = 10, 200
        for i in range(K):
            a, b, c = i % side, i // side % side, i // side // side
            balls[(-TOP + a * step, -TOP + b * step, -TOP + c * step)] = step // 2
        for p in rng.sample(sorted(balls), 20):
            balls[p] += 1
    items = list(balls.items())
    rng.shuffle(items)
    print(len(items))
    for (x, y, z), r in items:
        print(x, y, z, r)


main()
