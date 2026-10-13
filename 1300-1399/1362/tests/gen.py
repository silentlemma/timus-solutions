"""An agency of 100 000 employees: a seed and a mode. Mode 1 gives a
random hierarchy, mode 2 one long chain with Tanya in the middle, mode 3
a director with every other employee directly below, mode 4 a broom: a
long chain ending in many leaves. Tanya is random unless said."""

import random
import sys

COUNT = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = COUNT
    label = list(range(1, n + 1))
    rng.shuffle(label)
    boss = [0] * n
    for v in range(1, n):
        if mode == 1:
            boss[v] = rng.randrange(max(0, v - 50), v)
        elif mode == 2:
            boss[v] = v - 1
        elif mode == 3:
            boss[v] = 0
        else:
            boss[v] = v - 1 if v < n // 2 else n // 2 - 1
    subs = [[] for _ in range(n + 1)]
    for v in range(1, n):
        subs[label[boss[v]]].append(label[v])
    tanya = label[n // 2] if mode == 2 else label[rng.randrange(n)]
    print(n)
    for k in range(1, n + 1):
        print(" ".join(map(str, subs[k] + [0])))
    print(tanya)


main()
