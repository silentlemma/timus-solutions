"""A tree of 1000 computers: a seed and a mode. Mode 1 gives a random tree,
mode 2 a path, mode 3 a star around a random computer, mode 4 a
caterpillar, mode 5 a nearly complete binary tree, mode 6 a 900-edge
handle ending in 99 leaves, mode 7 nine arms of 111 edges each, mode 8 a
path with computer 1 at an endpoint (depth 999). Modes 6 and 7 put computer
1 at the handle tip and the hub, respectively. The wires come in a random
order and direction."""

import random
import sys

COUNT = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    label = list(range(1, COUNT + 1))
    rng.shuffle(label)
    if mode in (6, 7, 8):
        root = label.index(1)
        label[0], label[root] = label[root], label[0]
    edges = []
    for v in range(1, COUNT):
        if mode == 1:
            parent = rng.randrange(v)
        elif mode in (2, 8):
            parent = v - 1
        elif mode == 3:
            parent = 0
        elif mode == 4:
            parent = v - 1 if v < COUNT // 2 else rng.randrange(COUNT // 2)
        elif mode == 6:
            parent = v - 1 if v <= 900 else 900
        elif mode == 7:
            parent = 0 if (v - 1) % 111 == 0 else v - 1
        else:
            parent = (v - 1) // 2
        edges.append((label[parent], label[v]))
    rng.shuffle(edges)
    print(COUNT)
    for a, b in edges:
        print(*((a, b) if rng.random() < 0.5 else (b, a)))


main()
