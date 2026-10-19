"""Two maps of the garrisons from a seed and a mode: mode 1 a few
garrisons at random, 2 the most garrisons at random, 3 the most
garrisons with one spell gathering everything, 4 two permutations, so
nothing ever merges, 5 a rotation and a spell that merges two
neighbours, 6 the same random map twice, 7 maps into a few garrisons,
8 a shift down that stops at the end and a spell that changes
nothing, which takes the most days to win."""

import random
import sys

MOST = 1000
SMALL = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 1 else MOST
    a = [rng.randrange(n) for _ in range(n)]
    b = [rng.randrange(n) for _ in range(n)]
    if mode == 3:
        target = rng.randrange(n)
        a = [target] * n
    elif mode == 4:
        a, b = list(range(n)), list(range(n))
        rng.shuffle(a)
        rng.shuffle(b)
    elif mode == 5:
        a = [(i + 1) % n for i in range(n)]
        b = list(range(n))
        b[0] = 1
        if rng.random() < 0.5:
            a, b = b, a
    elif mode == 6:
        b = a[:]
    elif mode == 8:
        a = [max(i - 1, 0) for i in range(n)]
        b = list(range(n))
    elif mode == 7:
        few = rng.sample(range(n), 3)
        a = [rng.choice(few) for _ in range(n)]
        b = [rng.choice(few) if rng.random() < 0.5 else rng.randrange(n) for _ in range(n)]
    print(n)
    print("\n".join("%d %d" % (x + 1, y + 1) for x, y in zip(a, b)))


main()
