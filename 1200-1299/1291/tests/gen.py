"""A forest of gears: a seed and a mode. Mode 1 gives a small forest with
every link listed at both ends, mode 2 a tree of 1000 gears, mode 3 a
path of 1000 gears, mode 4 links listed at one end only, mode 5 many
small trees."""

import random
import sys

LARGEST = 1000
SMALL = 12


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else LARGEST
    teeth = [rng.randint(1, LARGEST) for _ in range(n)]
    links = []
    for v in range(1, n):
        if mode == 3:
            links.append((v - 1, v))
        elif mode == 5 and rng.random() < 0.3:
            continue
        elif mode != 1 or rng.random() < 0.7:
            links.append((rng.randrange(v), v))
    order = list(range(n))
    rng.shuffle(order)
    adj = [[] for _ in range(n)]
    for a, b in links:
        a, b = order[a], order[b]
        if mode == 4:
            a, b = rng.choice(((a, b), (b, a)))
            adj[a].append(b)
        else:
            adj[a].append(b)
            adj[b].append(a)
    print(n)
    for i in range(n):
        print(" ".join(map(str, [teeth[i]] + [j + 1 for j in adj[i]] + [0])))
    print(rng.randint(1, n), rng.randint(1, LARGEST))


main()
