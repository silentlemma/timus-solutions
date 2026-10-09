"""A random road map: a seed, N, M and the shape (0 any roads, 1 every
pair of cities, 2 up to three separate groups, 3 one long ring with M - N
chords). A ring on fewer than three cities is a path. M is capped at the
shape's capacity; complete graphs and rings include their required roads.
Cities and roads come in random order."""

import random
import sys

ANY, COMPLETE, GROUPS, RING = 0, 1, 2, 3
GROUP_COUNT = 3


def main():
    seed, n, m, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    roads = set()
    if shape == COMPLETE:
        roads = {(a, b) for a in range(n) for b in range(a + 1, n)}
    elif shape == RING and n > 1:
        roads = {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}
    groups = [list(range(n))]
    if shape == GROUPS:
        cut = sorted(rng.sample(range(1, n), min(GROUP_COUNT, n) - 1))
        groups = [list(range(lo, hi)) for lo, hi in zip([0] + cut, cut + [n])]
    available = [
        (a, b)
        for group in groups
        for i, a in enumerate(group)
        for b in group[i + 1:]
        if (a, b) not in roads
    ]
    roads.update(rng.sample(available, min(max(m - len(roads), 0), len(available))))
    label = list(range(1, n + 1))
    rng.shuffle(label)
    roads = list(roads)
    rng.shuffle(roads)
    lines = ["%d %d" % (n, len(roads))]
    for a, b in roads:
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d" % (label[a], label[b]))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
