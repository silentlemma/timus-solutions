"""One test from a seed and a mode, with no three consecutive vertices on
a line. Mode 1 is 30000 random vertices, mode 2 uses breakpoints that
are mirror images of each other, mode 3 is an even function, mode 4 an
odd one, mode 5 has steep zigzags, mode 6 is small. Mode 7 is a maximal
tilted zigzag whose odd part is a nonzero straight line; mode 8 clusters
all interior bends on the negative half, nearly doubling the output."""

import random
import sys

REACH = 15000
LARGEST = 30000
SMALL = 8


def straight(xs, ys, i):
    return (ys[i] - ys[i - 1]) * (xs[i + 1] - xs[i]) == (ys[i + 1] - ys[i]) * (xs[i] - xs[i - 1])


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 7:
        offset = rng.randint(-20, 20)
        xs = [x for x in range(-REACH, REACH + 1) if x != 0]
        ys = [x // 2 + offset + (2 if x % 2 else -2) for x in xs]
        print(len(xs))
        print("\n".join("%d %d" % p for p in zip(xs, ys)))
        return
    if mode == 8:
        xs = list(range(-REACH, 1)) + [REACH]
        ys = [(1 if i % 2 else -1) * rng.randint(10000, REACH)
              for i in range(len(xs))]
        print(len(xs))
        print("\n".join("%d %d" % p for p in zip(xs, ys)))
        return
    count = rng.randint(2, SMALL) if mode == 6 else LARGEST
    reach = rng.randint(min(count // 2 + 1, REACH), REACH) if mode != 6 else rng.randint(1, 10)
    if mode in (2, 3, 4):
        size = min(max(1, count // 2) - 1, reach - 1)
        half = sorted(rng.sample(range(1, reach), size) + [reach])
        xs = [-x for x in reversed(half)] + half
    else:
        inner = sorted(rng.sample(range(-reach + 1, reach), min(count - 2, 2 * reach - 1)))
        xs = [-reach] + inner + [reach]
    mirror = {x: i for i, x in enumerate(xs)}
    if mode == 3:
        tail = {x: rng.randint(-REACH, REACH) for x in xs if x > 0}
        ys = [tail[abs(x)] for x in xs]
    elif mode == 4:
        tail = {x: rng.randint(-REACH, REACH) for x in xs if x > 0}
        ys = [tail[x] if x > 0 else -tail[-x] for x in xs]
    elif mode == 5:
        ys = [REACH if i % 2 else -REACH for i in range(len(xs))]
    else:
        ys = [rng.randint(-REACH, REACH) for _ in xs]
    # nudge a vertex off the line through its neighbours, keeping the
    # symmetry of modes 3 and 4
    changed = True
    while changed:
        changed = False
        for i in range(1, len(xs) - 1):
            if straight(xs, ys, i):
                step = 1 if ys[i] < REACH else -1
                ys[i] += step
                j = mirror[-xs[i]]
                if mode == 3:
                    ys[j] = ys[i]
                elif mode == 4:
                    ys[j] = -ys[i]
                changed = True
    print(len(xs))
    print("\n".join("%d %d" % p for p in zip(xs, ys)))


main()
