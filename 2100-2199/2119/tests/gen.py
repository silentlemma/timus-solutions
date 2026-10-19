"""Tree and queries from "MODE SEED": mode 1 a random tree, mode 2 a path with
shuffled labels, mode 3 a star, mode 4 a caterpillar, mode 5 a random tree
with zero and maximum weights; modes 6 to 10 are the same shapes at the
maximum size, the first five are small. Queries toggle random vertices, so
the set grows and shrinks."""

import random
import sys

MAX_W = 10 ** 9
MAX_N = 3 * 10 ** 5
SHAPES = 5
SMALL_N = 8
SMALL_Q = 30


def tree(mode, n, rng):
    edges = []
    if mode == 2:
        for i in range(2, n + 1):
            edges.append((i - 1, i))
    elif mode == 3:
        for i in range(2, n + 1):
            edges.append((1, i))
    elif mode == 4:
        spine = max(1, n // 2)
        for i in range(2, spine + 1):
            edges.append((i - 1, i))
        for i in range(spine + 1, n + 1):
            edges.append((rng.randint(1, spine), i))
    else:
        for i in range(2, n + 1):
            edges.append((rng.randint(max(1, i - rng.choice([2, 10, n])), i - 1), i))
    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    result = []
    for u, v in edges:
        if mode == 5:
            w = rng.choice([0, MAX_W])
        else:
            w = rng.randint(0, MAX_W)
        result.append((labels[u - 1], labels[v - 1], w))
    rng.shuffle(result)
    return result


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode > SHAPES:
        mode -= SHAPES
        n = q = MAX_N
    else:
        n, q = rng.randint(1, SMALL_N), rng.randint(1, SMALL_Q)
    lines = [str(n)]
    lines += ["%d %d %d" % e for e in tree(mode, n, rng)]
    lines.append(str(q))
    inside = set()
    pool = rng.sample(range(1, n + 1), min(n, rng.choice([2, 10, n])))
    for _ in range(q):
        v = rng.choice(pool)
        if v in inside:
            inside.remove(v)
            lines.append("- %d" % v)
        else:
            inside.add(v)
            lines.append("+ %d" % v)
    print("\n".join(lines))


main()
