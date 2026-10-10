"""Senators and their files: a seed, N, a mode, a number of groups and an
edge density in percent. Mode 1 is the complete graph, mode 2 groups that
all lead from a single first group, mode 3 the same with a second group
nobody reaches, mode 4 one long cycle and mode 5 a random graph."""

import random
import sys


def main():
    seed, n, mode, k, percent = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    if mode != 2 and mode != 3:
        k = 1
    cuts = sorted(rng.sample(range(1, n), k - 1))
    bounds = [0] + cuts + [n]
    group = [g for g in range(k) for _ in range(bounds[g], bounds[g + 1])]
    # one edge into every later group from somewhere earlier
    extra = {}
    for g in range(1, k):
        extra.setdefault(rng.randrange(bounds[g]), []).append(
            rng.randrange(bounds[g], bounds[g + 1])
        )
    last = bounds[k - 1] if mode == 3 else n
    label = list(range(1, n + 1))
    rng.shuffle(label)
    rows = [""] * n
    for u in range(n):
        g = group[u]
        size = bounds[g + 1] - bounds[g]
        if mode == 1:
            row = [v for v in range(n) if v != u]
        elif mode == 4:
            row = [(u + 1) % n]
        elif mode == 5:
            row = [v for v in range(n) if rng.randrange(100) < percent]
        else:
            row = [v for v in range(bounds[g], n) if rng.randrange(100) < percent]
            if size > 1:
                row.append(bounds[g] + (u - bounds[g] + 1) % size)
            row += extra.get(u, [])
            if u < last:
                row = [v for v in row if v < last]
        row = [label[v] for v in set(row)]
        rng.shuffle(row)
        rows[label[u] - 1] = " ".join(map(str, row + [0]))
    sys.stdout.write(str(n) + "\n" + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
