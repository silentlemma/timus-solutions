"""One test from a seed and a mode: a connected network and protocols.
Mode 1 takes 50 computers with a random tree and extra links, mode 2 a
path with alternating protocols, mode 3 up to 10 computers, mode 4 a
dense network, mode 5 a cycle with alternating protocols."""

import random
import sys

LARGEST = 50
SMALL = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 3 else LARGEST
    edges = set()
    if mode in (2, 5):
        order = list(range(n))
        rng.shuffle(order)
        protocol = [""] * n
        for i, v in enumerate(order):
            protocol[v] = "EJ"[i % 2]
            if i:
                edges.add((order[i - 1], v))
        if mode == 5:
            edges.add((order[-1], order[0]))
    else:
        protocol = [rng.choice("EJ") for _ in range(n)]
        for v in range(1, n):
            edges.add((rng.randrange(v), v))
        extra = n * n // 4 if mode == 4 else rng.randint(0, n)
        for _ in range(extra):
            a, b = rng.sample(range(n), 2) if n > 1 else (0, 0)
            if a != b and (b, a) not in edges:
                edges.add((a, b))
    edges = list(edges)
    rng.shuffle(edges)
    print(n, len(edges))
    print(" ".join(protocol))
    for a, b in edges:
        print(a + 1, b + 1)


main()
