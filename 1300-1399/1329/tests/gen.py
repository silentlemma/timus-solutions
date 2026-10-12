"""A tree of 40000 milestones and 40000 questions: a seed and a mode.
Mode 1 gives a random tree, mode 2 a single chain, mode 3 a star, mode 4
a random tree whose nodes have parents close above them. The numbers are
shuffled over 0 to 40000, and half of the questions ask about a node and
one of its ancestors."""

import random
import sys

N = 40000
TOP = 40000
CLOSE = 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    names = rng.sample(range(TOP + 1), N)
    parent = [-1] * N
    for i in range(1, N):
        if mode == 1:
            parent[i] = rng.randrange(i)
        elif mode == 2:
            parent[i] = i - 1
        elif mode == 3:
            parent[i] = 0
        else:
            parent[i] = rng.randrange(max(0, i - CLOSE), i)
    order = list(range(N))
    rng.shuffle(order)
    print(N)
    for i in order:
        print(names[i], names[parent[i]] if parent[i] >= 0 else -1)
    print(N)
    for _ in range(N):
        a = rng.randrange(N)
        b = rng.randrange(N)
        if rng.random() < 0.5:
            b = a
            for _ in range(rng.randint(1, 30)):
                if parent[b] >= 0:
                    b = parent[b]
        if a == b:
            b = (a + 1) % N
        if rng.random() < 0.5:
            a, b = b, a
        print(names[a], names[b])


main()
