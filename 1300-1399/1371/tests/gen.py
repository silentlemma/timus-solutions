"""Weighted trees: seed mode [N], with N defaulting to 50 000.

Modes 1-4 retain their original fixed size and output:
1: random recursive tree; 2: maximum-weight path; 3: random-weight star;
4: random recursive tree with shuffled, randomly directed edges.
New modes accept optional N (2 through 50 000):
5: two equal hubs of maximum-weight roads, joined by a maximum-weight road;
6: balanced binary tree with alternating free and maximum-weight levels;
7: comb with alternating free and maximum-weight spine roads and unit teeth;
8: uniformly random labelled tree from a seeded Prufer sequence, random weights.
All new modes shuffle vertex labels, edge order, and edge directions.
"""

import heapq
import random
import sys

COUNT = 50000
DEAREST = 1000


def new_tree(rng, mode, n):
    edges = []
    if mode == 5:
        edges.append((0, 1, DEAREST))
        edges.extend((v % 2, v, DEAREST) for v in range(2, n))
    elif mode == 6:
        for v in range(1, n):
            depth = (v + 1).bit_length() - 1
            edges.append(((v - 1) // 2, v, DEAREST if depth % 2 else 0))
    elif mode == 7:
        spine = (n + 1) // 2
        edges.extend((v - 1, v, DEAREST if v % 2 else 0) for v in range(1, spine))
        edges.extend((v - spine, v, 1) for v in range(spine, n))
    else:
        sequence = [rng.randrange(n) for _ in range(n - 2)]
        degree = [1] * n
        for v in sequence:
            degree[v] += 1
        leaves = [v for v in range(n) if degree[v] == 1]
        heapq.heapify(leaves)
        for v in sequence:
            leaf = heapq.heappop(leaves)
            edges.append((leaf, v, rng.randint(0, DEAREST)))
            degree[v] -= 1
            if degree[v] == 1:
                heapq.heappush(leaves, v)
        edges.append((*leaves, rng.randint(0, DEAREST)))
    label = list(range(1, n + 1))
    rng.shuffle(label)
    edges = [(label[a], label[b], c) for a, b, c in edges]
    rng.shuffle(edges)
    return [(b, a, c) if rng.random() < 0.5 else (a, b, c) for a, b, c in edges]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7, 8):
        n = int(sys.argv[3]) if len(sys.argv) > 3 else COUNT
        if not 2 <= n <= COUNT:
            raise ValueError('N must be between 2 and 50 000')
        print(n)
        for e in new_tree(rng, mode, n):
            print(*e)
        return
    n = COUNT
    label = list(range(1, n + 1))
    rng.shuffle(label)
    edges = []
    for v in range(1, n):
        if mode == 2:
            edges.append((label[v - 1], label[v], DEAREST))
        elif mode == 3:
            edges.append((label[0], label[v], rng.randint(0, DEAREST)))
        else:
            edges.append((label[rng.randrange(v)], label[v], rng.randint(0, DEAREST)))
    if mode == 4:
        rng.shuffle(edges)
        edges = [(b, a, c) if rng.random() < 0.5 else (a, b, c) for a, b, c in edges]
    print(n)
    for e in edges:
        print(*e)


main()
