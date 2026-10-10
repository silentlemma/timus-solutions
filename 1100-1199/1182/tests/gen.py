"""Acquaintances of N persons: a seed, N, the number of groups of the
conflict graph and a mode. Persons are spread over groups, each group is
split into two sides, and some pairs across sides of a group do not know
each other (at least one way); everybody else knows everybody. Mode 0
keeps the conflicts bipartite, mode 1 adds one conflict inside a side,
which may make an odd cycle, mode 2 makes every group a single conflict
pair or a lone person."""

import random
import sys

CHANCE = 0.3


def main():
    seed, n, groups, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    people = list(range(1, n + 1))
    rng.shuffle(people)
    group = {p: rng.randrange(groups) for p in people}
    side = {p: rng.randrange(2) for p in people}
    knows = {p: set(q for q in people if q != p) for p in people}

    def conflict(a, b):
        # one or both of them do not know the other
        if rng.random() < 0.5:
            knows[a].discard(b)
        if rng.random() < 0.5 or b in knows[a]:
            knows[b].discard(a)

    if mode == 2:
        for k in range(0, n - 1, 2):
            if rng.random() < 0.5:
                conflict(people[k], people[k + 1])
    else:
        for a in people:
            for b in people:
                if a < b and group[a] == group[b] and side[a] != side[b] and rng.random() < CHANCE:
                    conflict(a, b)
        if mode == 1:
            a, b = rng.sample(people, 2)
            conflict(a, b)
    lines = [str(n)]
    for p in range(1, n + 1):
        row = list(knows[p])
        rng.shuffle(row)
        lines.append(" ".join(map(str, row + [0])))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
