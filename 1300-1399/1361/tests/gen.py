"""A city of 100 000 crossroads: a seed and a mode. Mode 1 gives random
lists of roads, mode 2 two cycles of coprime lengths near 50 000 that
share one crossroad, so the meeting comes after about 2.5 * 10^9
minutes, mode 3 two even cycles that A and B reach out of step, so they
never meet, mode 4 a long chain where A goes one crossroad at a time
and B two. Mode 5 gives two disjoint long tails ending at different
self-loops. Mode 6 gives equal long tails that meet before their common
sink. Mode 7 gives 200 randomly ordered complete road lists. Mode 8
gives two independently shuffled successor permutations on 60 crossroads.
Modes 1 through 6 use the maximum city size or one fewer crossroad."""

import random
import sys

COUNT = 100000


def extra_mode(rng, mode):
    sys.stdout.reconfigure(newline="\n")
    if mode == 5:
        n = COUNT
        half = n // 2
        lists = [[v + 1 if v not in (half, n) else v] for v in range(1, n + 1)]
        a, b = 1, half + 1
    elif mode == 6:
        n = COUNT
        half = n // 2
        lists = [[v + 1] for v in range(1, n)] + [[n]]
        lists[half - 2] = [n - 1]
        lists[n - 3] = [n - 1]
        a, b = 1, half
    elif mode == 7:
        n = 200
        lists = []
        for _ in range(n):
            roads = list(range(1, n + 1))
            rng.shuffle(roads)
            lists.append(roads)
        a, b = rng.sample(range(1, n + 1), 2)
    elif mode == 8:
        n = 60
        left = list(range(1, n + 1))
        right = left[:]
        rng.shuffle(left)
        rng.shuffle(right)
        lists = [[l, r] if l != r else [l] for l, r in zip(left, right)]
        a, b = rng.sample(range(1, n + 1), 2)
    else:
        raise ValueError("unknown mode")
    print(n)
    for roads in lists:
        print(*roads, 0)
    print(a, b)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode >= 5:
        extra_mode(rng, mode)
        return
    n = COUNT if mode in (1, 4) else COUNT - 1
    lists = []
    if mode == 1:
        for _ in range(n):
            lists.append([rng.randint(1, n) for _ in range(rng.randint(1, 3))])
        a, b = rng.randint(1, n), rng.randint(1, n)
    elif mode in (2, 3):
        # crossroad 1 is shared; A loops 1, 2, ..., p and B loops 1, p + 1, ..., n:
        # lengths 49 999 and 50 001 in mode 2, both 50 000 in mode 3
        p = n // 2 if mode == 2 else n // 2 + 1
        lists.append([2, p + 1])
        for v in range(2, p + 1):
            lists.append([v + 1 if v < p else 1, rng.randint(1, n)])
        for v in range(p + 1, n + 1):
            lists.append([rng.randint(1, n), v + 1 if v < n else 1])
        a, b = 2, p + 1 if mode == 2 else p + 2
    else:
        for v in range(1, n + 1):
            lists.append([min(v + 1, n), min(v + 2, n)])
        a, b = 1, 2
    print(n)
    for roads in lists:
        print(" ".join(map(str, roads)), 0)
    print(a, b)


main()
