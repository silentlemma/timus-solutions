"""Pairs of teams from a seed; every team plays one to three pairs.

Mode 1: a few teams. Mode 2: 10^5 teams in trees and cycles, so Yes. Mode 3:
like mode 2, but the first group gets two extra pairs, so No. Mode 4: one
cycle through all 10^5 teams. Mode 5: one path through all teams.
Mode 6: disjoint pairs covering 10^5 teams (minimum games for that many teams).
Mode 7: a cycle with a matching of chords, 10^5 games on 66667 teams, so No.
Arguments: mode seed [teams]; optional teams applies only to modes 6 and 7.
"""

import random
import sys

SMALL = 7
GROUP = 50
MAX = 10 ** 5
MOST = 3


def group(rng, part, extra, pairs):
    # a random tree with degrees below 3, then up to `extra` more pairs
    degree = {v: 0 for v in part}
    for i in range(1, len(part)):
        while True:
            j = rng.randrange(i)
            if degree[part[j]] < MOST - 1:
                break
        pairs.append((part[i], part[j]))
        degree[part[i]] += 1
        degree[part[j]] += 1
    added = 0
    while added < extra:
        free = [v for v in part if degree[v] < MOST]
        if len(free) < 2:
            break
        x, y = rng.sample(free, 2)
        pairs.append((x, y))
        degree[x] += 1
        degree[y] += 1
        added += 1
    return added


def groups(rng, k, first_extra):
    order = list(range(1, k + 1))
    rng.shuffle(order)
    pairs = []
    pos, first = 0, True
    while pos < k:
        size = min(k - pos, rng.randint(2, GROUP))
        if k - pos - size == 1:
            size += 1
        extra = first_extra if first else rng.randint(0, 1)
        group(rng, order[pos:pos + size], extra, pairs)
        pos, first = pos + size, False
    return pairs


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        k = rng.randint(2, SMALL)
        pairs = groups(rng, k, rng.randint(0, 2))
    elif mode in (2, 3):
        k = MAX
        pairs = groups(rng, k, 2 if mode == 3 else 1)
    elif mode == 6:
        k = int(sys.argv[3]) if len(sys.argv) > 3 else MAX
        if not 2 <= k <= MAX or k % 2:
            raise ValueError("mode 6 needs an even team count in [2, 100000]")
        order = list(range(1, k + 1))
        rng.shuffle(order)
        pairs = list(zip(order[::2], order[1::2]))
    elif mode == 7:
        k = int(sys.argv[3]) if len(sys.argv) > 3 else 66667
        if not 4 <= k or k + k // 2 > MAX:
            raise ValueError("mode 7 needs 4 <= teams and teams + teams // 2 <= 100000")
        order = list(range(1, k + 1))
        rng.shuffle(order)
        pairs = [(order[i], order[(i + 1) % k]) for i in range(k)]
        pairs += [(order[i], order[i + k // 2]) for i in range(k // 2)]
    else:
        k = MAX
        order = list(range(1, k + 1))
        rng.shuffle(order)
        pairs = [(order[i], order[i + 1]) for i in range(k - 1)]
        if mode == 4:
            pairs.append((order[-1], order[0]))
    rng.shuffle(pairs)
    pairs = [p if rng.random() < 0.5 else (p[1], p[0]) for p in pairs]
    print(len(pairs), k)
    for x, y in pairs:
        print(x, y)


main()
