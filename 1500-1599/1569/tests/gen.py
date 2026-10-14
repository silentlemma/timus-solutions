"""One test from a seed and a mode: a connected plan without repeated
channels. Mode 1 joins all 100 nodes to each other, mode 2 is a random
plan on 100 nodes, mode 3 a long path with a few shortcuts, mode 4 two
dense halves joined by one channel, mode 5 is small."""

import random
import sys

NODES = 100
SMALL = 8


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 5 else NODES
    channels = set()
    order = list(range(1, n + 1))
    rng.shuffle(order)
    if mode == 1:
        channels = {(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1)}
    else:
        # a random spanning tree keeps the plan connected
        for i in range(1, n):
            channels.add(tuple(sorted((order[i], order[rng.randrange(i)]))))
        if mode == 3:
            channels = {tuple(sorted((order[i], order[i + 1]))) for i in range(n - 1)}
            for _ in range(rng.randint(1, 5)):
                i = rng.randrange(n - 3)
                channels.add(tuple(sorted((order[i], order[i + rng.randint(2, 3)]))))
        elif mode == 4:
            half = n // 2
            channels = {tuple(sorted((order[0], order[half])))}
            for side in (order[:half], order[half:]):
                for i in range(1, len(side)):
                    channels.add(tuple(sorted((side[i], side[rng.randrange(i)]))))
                for _ in range(len(side) * 3):
                    a, b = rng.sample(side, 2)
                    channels.add(tuple(sorted((a, b))))
        else:
            extra = rng.randint(0, n * (n - 1) // 2 - n + 1)
            for _ in range(extra):
                a, b = rng.sample(range(1, n + 1), 2)
                channels.add(tuple(sorted((a, b))))
    channels = list(channels)
    rng.shuffle(channels)
    print(n, len(channels))
    for a, b in channels:
        print(*((a, b) if rng.random() < 0.5 else (b, a)))


main()
