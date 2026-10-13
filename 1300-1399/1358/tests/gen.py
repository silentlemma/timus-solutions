"""A tree of 1000 computers: a seed and a mode. Mode 1 gives a random tree,
mode 2 a path, mode 3 a star around a random computer, mode 4 a
caterpillar, mode 5 a nearly complete binary tree. The wires come in a
random order and direction."""

import random
import sys

COUNT = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    label = list(range(1, COUNT + 1))
    rng.shuffle(label)
    edges = []
    for v in range(1, COUNT):
        if mode == 1:
            parent = rng.randrange(v)
        elif mode == 2:
            parent = v - 1
        elif mode == 3:
            parent = 0
        elif mode == 4:
            parent = v - 1 if v < COUNT // 2 else rng.randrange(COUNT // 2)
        else:
            parent = (v - 1) // 2
        edges.append((label[parent], label[v]))
    rng.shuffle(edges)
    print(COUNT)
    for a, b in edges:
        print(*((a, b) if rng.random() < 0.5 else (b, a)))


main()
