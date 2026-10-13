"""An agency of 100 000 employees: a seed and a mode. Mode 1 gives a
random hierarchy, mode 2 one long chain with Tanya in the middle, mode 3
a director with every other employee directly below, mode 4 a broom: a
long chain ending in many leaves. Mode 5 is a binary tree with Tanya at
the director, mode 6 has 316 hubs below the director and all remaining
employees below those hubs, with Tanya at a leaf. Mode 7 is a random
hierarchy with each boss chosen uniformly among all earlier vertices.
Tanya is random unless said. All modes shuffle employee labels; modes
5-7 also shuffle the order of subordinate lists."""

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
        elif mode == 5:
            boss[v] = (v - 1) // 2
        elif mode == 6:
            boss[v] = 0 if v <= 316 else 1 + (v - 317) % 316
        elif mode == 7:
            boss[v] = rng.randrange(v)
        else:
            boss[v] = v - 1 if v < n // 2 else n // 2 - 1
    subs = [[] for _ in range(n + 1)]
    for v in range(1, n):
        subs[label[boss[v]]].append(label[v])
    tanya = label[n // 2] if mode == 2 else label[rng.randrange(n)]
    if mode in (5, 6, 7):
        sys.stdout.reconfigure(newline="\n")
        for row in subs:
            rng.shuffle(row)
        if mode == 5:
            tanya = label[0]
        elif mode == 6:
            tanya = label[-1]
    print(n)
    for k in range(1, n + 1):
        print(" ".join(map(str, subs[k] + [0])))
    print(tanya)


main()
