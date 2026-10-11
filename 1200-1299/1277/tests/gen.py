"""A galaxy: a seed and a mode. Mode 1 draws up to 10 stations, mode 2 up
to 100 stations with few channels, mode 3 up to 100 stations with many,
mode 4 a long ladder of stations between the museum and the refuge. The
graph is always connected; K sits near the cheapest cut to test both
answers."""

import random
import sys

STATIONS = 100
POLICE = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(3, 10) if mode == 1 else rng.randint(3, STATIONS)
    edges = set()
    if mode == 4:
        # two rails joined by rungs; each rung pair is a possible cut
        n = 2 * (n // 2) + 2
        for i in range(0, n - 2, 2):
            edges |= {(i, i + 2), (i + 1, i + 3), (i, i + 1)}
    order = list(range(n))
    rng.shuffle(order)
    for i in range(1, n):
        a, b = order[i], order[rng.randrange(i)]
        edges.add((min(a, b), max(a, b)))
    extra = {1: n, 2: n // 2, 3: n * (n - 1) // 4, 4: 0}[mode]
    for _ in range(extra):
        a, b = rng.sample(range(n), 2)
        edges.add((min(a, b), max(a, b)))
    costs = [rng.randint(1, POLICE // n) for _ in range(n)]
    s, f = rng.sample(range(1, n + 1), 2) if rng.random() < 0.95 else [1, 1]
    k = rng.randint(2, POLICE)
    lines = ["%d" % k, "%d %d %d %d" % (n, len(edges), s, f), " ".join(map(str, costs))]
    lines += ["%d %d" % (a + 1, b + 1) for a, b in sorted(edges)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
