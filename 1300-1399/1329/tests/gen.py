"""Print a deterministic tree and queries: a seed and a mode.
Mode 1 gives a random tree, mode 2 a single chain, mode 3 a star, mode 4
a random tree whose nodes have parents close above them. The numbers are
shuffled over 0 to 40000, and half of the questions ask about a node and
one of its ancestors. Modes 1-4 use 40000 nodes and 40000 queries.
Mode 5: a balanced binary tree, with leaf pairs and ancestors.
Mode 6: a broom, with a long handle and a wide fan of leaves.
Mode 7: two long chains, with cross-branch and distant ancestor queries.
Modes 5-7 also use 40000 nodes and 40000 queries.
Mode 8: only three nodes but 40000 queries, repeating all ordered pairs.
"""

import random
import sys

N = 40000
TOP = 40000
CLOSE = 5


def extended(seed, mode):
    sys.stdout.reconfigure(newline="\n")
    rng = random.Random(seed)
    n = 3 if mode == 8 else N
    names = list(range(n - 1)) + [TOP]
    rng.shuffle(names)
    parent = [-1]
    for i in range(1, n):
        if mode == 5:
            par = (i - 1) // 2
        elif mode == 6:
            par = i - 1 if i < N // 2 else N // 2 - 1
        elif mode == 7:
            par = 0 if i in (1, N // 2) else i - 1
        else:
            par = 0
        parent.append(par)
    order = list(range(n))
    rng.shuffle(order)
    print(n)
    for i in order:
        print(names[i], names[parent[i]] if parent[i] >= 0 else -1)
    print(N)
    for q in range(N):
        if mode == 5:
            a, b = rng.sample(range(n // 2, n), 2)
            if q % 3:
                b = a
                for _ in range(rng.randint(1, 15)):
                    if parent[b] >= 0:
                        b = parent[b]
        elif mode == 6:
            a, b = rng.sample(range(n // 2, n), 2)
            if q % 3:
                b = rng.randrange(n // 2)
        elif mode == 7:
            if q % 2 == 0:
                a = rng.randrange(1, n // 2)
                b = rng.randrange(n // 2, n)
            elif q % 4 == 1:
                a, b = rng.sample(range(1, n // 2), 2)
            else:
                a, b = rng.sample(range(n // 2, n), 2)
        else:
            a, b = ((0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1))[q % 6]
        if rng.randrange(2):
            a, b = b, a
        print(names[a], names[b])


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if 5 <= mode <= 8:
        extended(seed, mode)
        return
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
