"""A circuit: a seed and a mode. Mode 1 joins random pairs of up to 20
nodes, mode 2 a long chain with many parallel resistors, mode 3 adds
nodes cut off from both ends. Nodes 1 and N are always connected."""

import random
import sys

NODES = 20
RESISTORS = 999
TOP_R = 1000


def connected(n, edges):
    reach, changed = {1}, True
    while changed:
        changed = False
        for a, b, _ in edges:
            if (a in reach) != (b in reach):
                reach |= {a, b}
                changed = True
    return n in reach


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        n = rng.randint(2, NODES)
        edges = []
        if mode == 2:
            for v in range(1, n):
                edges.append((v, v + 1, rng.randint(1, TOP_R)))
        m = rng.randint(len(edges) + 1, RESISTORS)
        # mode 3 keeps the last few inner nodes apart from the rest
        apart = set(range(max(2, n - 3), n)) if mode == 3 else set()
        while len(edges) < m:
            a, b = sorted(rng.sample(range(1, n + 1), 2)) if n > 2 else (1, 2)
            if (a in apart) != (b in apart):
                continue
            edges.append((a, b, rng.randint(1, TOP_R)))
        if connected(n, edges):
            break
    rng.shuffle(edges)
    lines = ["%d %d" % (n, len(edges))] + ["%d %d %d" % e for e in edges]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
