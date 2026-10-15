"""One test from a seed and a mode: mode 1 a small random graph, mode 2
fifty robots where most pairs are friends (few enemies each), mode 3
fifty robots with random friendships, mode 4 everyone friends with
everyone (2^50 days), mode 5 the enemies forming paths and cycles,
mode 6 a connected cubic enemy graph (a cycle plus a random matching),
mode 7 a random recursive enemy tree. Modes 6 and 7 shuffle vertex labels."""

import random
import sys

MOST = 50


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 10) if mode == 1 else MOST
    enemy = [[False] * n for _ in range(n)]
    if mode == 6:
        order = list(range(n))
        rng.shuffle(order)
        for a in range(n):
            b = (a + 1) % n
            enemy[order[a]][order[b]] = enemy[order[b]][order[a]] = True
        matching = list(range(n))
        while True:
            rng.shuffle(matching)
            pairs = list(zip(matching[::2], matching[1::2]))
            if all(not enemy[a][b] for a, b in pairs):
                break
        for a, b in pairs:
            enemy[a][b] = enemy[b][a] = True
    elif mode == 7:
        order = list(range(n))
        rng.shuffle(order)
        for v in range(1, n):
            a, b = order[v], order[rng.randrange(v)]
            enemy[a][b] = enemy[b][a] = True
    elif mode == 5:
        order = list(range(n))
        rng.shuffle(order)
        i = 0
        while i < n:
            size = rng.randint(1, 12)
            group = order[i:i + size]
            for a, b in zip(group, group[1:]):
                enemy[a][b] = enemy[b][a] = True
            if len(group) > 2 and rng.random() < 0.5:
                enemy[group[0]][group[-1]] = enemy[group[-1]][group[0]] = True
            i += size
    elif mode != 4:
        p = {1: rng.random(), 2: rng.uniform(0.04, 0.12), 3: rng.random()}[mode]
        for a in range(n):
            for b in range(a + 1, n):
                if rng.random() < p:
                    enemy[a][b] = enemy[b][a] = True
    print(n)
    for a in range(n):
        print("".join("0" if a == b or enemy[a][b] else "1" for b in range(n)))


main()
