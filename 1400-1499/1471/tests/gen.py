"""One test from a seed and a mode. Mode 1 is a small random tree, mode 2 a
random tree of 50000 vertices, mode 3 a path of 50000 vertices with the
heaviest edges, asked first for its two ends, mode 4 a star, mode 5 a long
path with short branches. Vertex names are shuffled and every mode asks
75000 questions, except the small one."""

import random
import sys

LARGEST = 50000
QUESTIONS = 75000
SMALL = 30
SMALL_QUESTIONS = 200
HEAVIEST = 1000
BRANCH = 3  # in mode 5 every vertex hangs within this many steps back


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else LARGEST
    m = SMALL_QUESTIONS if mode == 1 else QUESTIONS
    parents = []
    for v in range(1, n):
        if mode == 3:
            parents.append(v - 1)
        elif mode == 4:
            parents.append(0)
        elif mode == 5:
            parents.append(max(0, v - rng.randint(1, BRANCH)))
        else:
            parents.append(rng.randrange(v))
    names = list(range(n))
    rng.shuffle(names)
    lines = [str(n)]
    for v, p in zip(range(1, n), parents):
        w = HEAVIEST if mode == 3 else rng.randint(0, HEAVIEST)
        a, b = names[v], names[p]
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d %d" % (a, b, w))
    lines.append(str(m))
    for i in range(m):
        if mode == 3 and i == 0:
            lines.append("%d %d" % (names[0], names[n - 1]))  # the two ends
        else:
            lines.append("%d %d" % (rng.randrange(n), rng.randrange(n)))
    print("\n".join(lines))


main()
