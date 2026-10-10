"""A city: a seed, N, the number of links, a coordinate range and a mode.
Mode 1 has random speeds, mode 2 a subway barely faster than walking,
mode 3 equal speeds, and mode 4 stations on a grid so that many routes
tie."""

import random
import sys


def main():
    seed, n, m, size, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    if mode == 1:
        walk = round(rng.uniform(0.5, 50), 2)
        metro = round(rng.uniform(walk, 10000), 2)
    elif mode == 2:
        walk = round(rng.uniform(0.5, 10), 2)
        metro = round(walk * 1.01, 2)
    elif mode == 3:
        walk = metro = round(rng.uniform(0.5, 10000), 2)
    else:
        walk, metro = 1, 2
    if mode == 4:
        side = max(2, int(n**0.5))
        pts = [(i % side, i // side) for i in range(n)]
    else:
        pts = [
            (round(rng.uniform(-size, size), 3), round(rng.uniform(-size, size), 3))
            for _ in range(n)
        ]
    pairs = set()
    while len(pairs) < min(m, n * (n - 1) // 2):
        u, v = rng.sample(range(1, n + 1), 2)
        pairs.add((min(u, v), max(u, v)))
    pairs = list(pairs)
    rng.shuffle(pairs)
    lines = ["%s %s" % (walk, metro), str(n)]
    lines += ["%s %s" % p for p in pts]
    lines += ["%d %d" % p for p in pairs] + ["0 0"]
    for _ in range(2):
        lines.append(
            "%s %s" % (round(rng.uniform(-size, size), 3), round(rng.uniform(-size, size), 3))
        )
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
