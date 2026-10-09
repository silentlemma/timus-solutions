"""A random road map: a seed, N, M and the shape (0 any roads, 1 every
pair of cities, 2 three separate groups, 3 one long ring with M - N
chords). Cities and roads come in random order."""

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
    elif shape == RING:
        roads = {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}
    groups = [list(range(n))]
    if shape == GROUPS:
        cut = sorted(rng.sample(range(1, n), GROUP_COUNT - 1))
        groups = [list(range(lo, hi)) for lo, hi in zip([0] + cut, cut + [n])]
    while len(roads) < m:
        group = rng.choice(groups)
        if len(group) < 2:
            continue
        a, b = rng.sample(group, 2)
        roads.add((min(a, b), max(a, b)))
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
