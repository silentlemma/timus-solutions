"""Maps of a forest: a seed, N and a mode. Cities are shuffled.

1: random tree; 2: long chain; 3: star; 4: forest; 5: no links.
6: chain with maximum city and flight joys.
7: balanced binary tree with zero city joys and unit flight joys.
8: random forest with zero-heavy boundary joys and reversed flights.
"""

import random
import sys

TOP = 10000
PIECES = 1000


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    links = []
    for v in range(2, n + 1):
        if mode == 1:
            links.append((v, rng.randint(1, v - 1)))
        elif mode == 2:
            links.append((v, v - 1))
        elif mode == 3:
            links.append((v, 1))
        elif mode == 4 and rng.randrange(PIECES):
            links.append((v, rng.randint(max(1, v - PIECES), v - 1)))
        elif mode == 6:
            links.append((v, v - 1))
        elif mode == 7:
            links.append((v, v // 2))
        elif mode == 8 and rng.randrange(4):
            links.append((v, rng.randint(1, v - 1)))
    names = list(range(1, n + 1))
    rng.shuffle(names)
    rng.shuffle(links)
    if mode in (6, 7, 8):
        if mode == 6:
            joys = [TOP] * n
        elif mode == 7:
            joys = [0] * n
        else:
            joys = [rng.choice((0, 0, 1, TOP)) for _ in range(n)]
        lines = ["%d %d" % (n, len(links)), " ".join(map(str, joys))]
        for a, b in links:
            c = TOP if mode == 6 else 1 if mode == 7 else rng.choice((0, 0, 1, TOP))
            if mode == 8 and rng.randrange(2):
                a, b = b, a
            lines.append("%d %d %d" % (names[a - 1], names[b - 1], c))
        print("\n".join(lines))
        return
    lines = ["%d %d" % (n, len(links)), " ".join(str(rng.randint(0, TOP)) for _ in range(n))]
    lines += ["%d %d %d" % (names[a - 1], names[b - 1], rng.randint(0, TOP)) for a, b in links]
    print("\n".join(lines))


main()
