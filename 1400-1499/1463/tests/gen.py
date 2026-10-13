"""Maps of a forest: a seed, N and a mode. Mode 1 is a random tree, mode 2
a single long chain, mode 3 a star, mode 4 a forest of many small trees,
mode 5 cities without any link. Cities are shuffled."""

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
    names = list(range(1, n + 1))
    rng.shuffle(names)
    rng.shuffle(links)
    lines = ["%d %d" % (n, len(links)), " ".join(str(rng.randint(0, TOP)) for _ in range(n))]
    lines += ["%d %d %d" % (names[a - 1], names[b - 1], rng.randint(0, TOP)) for a, b in links]
    print("\n".join(lines))


main()
