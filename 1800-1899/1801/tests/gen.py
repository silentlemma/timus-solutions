"""One test from a seed and a mode: mode 1 a few small pots with few
parties, so either answer is possible, mode 2 100 pots of 100 teams
with parties of at most 100 teams each, mode 3 the same with every
party holding exactly as many teams as there are groups, mode 4 a large
draw where one party has one team too many, mode 5 a large draw with
many small parties, mode 6 a full draw with 10000 distinct parties,
mode 7 a cycle of 100 two-team pots, mode 8 two 100-team pots with one
shared saturated party, mode 9 a shuffled 17-by-43 draw with mixed
saturated and unsaturated parties."""

import random
import string
import sys
from collections import Counter

LIMIT = 100
FEW = 5
NAME = 10


def word(rng, used):
    while True:
        w = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, NAME)))
        if w not in used:
            used.add(w)
            return w


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        groups, pots = rng.randint(1, FEW), rng.randint(1, FEW)
        parties = [word(rng, set()) for _ in range(rng.randint(1, FEW))]
        labels = [rng.choice(parties) for _ in range(groups * pots)]
    elif mode in (6, 7, 8, 9):
        names = set()
        if mode == 6:
            groups, pots = LIMIT, LIMIT
            labels = [word(rng, names) for _ in range(groups * pots)]
            rng.shuffle(labels)
        elif mode == 7:
            groups, pots = 2, LIMIT
            parties = [word(rng, names) for _ in range(pots)]
            labels = [parties[v] for p in range(pots) for v in (p, (p + 1) % pots)]
        elif mode == 8:
            groups, pots = LIMIT, 2
            shared, left, right = [word(rng, names) for _ in range(3)]
            first = [shared] * (groups - 1) + [left]
            second = [shared] + [right] * (groups - 1)
            rng.shuffle(first)
            rng.shuffle(second)
            labels = first + second
        else:
            groups, pots = 17, 43
            core = 32
            parties = [word(rng, names) for _ in range(80)]
            labels = []
            for _ in range(groups):
                labels.extend(parties[:core])
                labels.extend(rng.sample(parties[core:], pots - core))
            rng.shuffle(labels)
    else:
        groups, pots = LIMIT, LIMIT
        if mode == 2 or mode == 3:
            # parties of at most `groups` teams, shuffled over the pots
            cap = groups if mode == 3 else rng.randint(1, groups)
            labels = []
            names = set()
            while len(labels) < groups * pots:
                party = word(rng, names)
                labels += [party] * min(cap, groups * pots - len(labels))
            rng.shuffle(labels)
        elif mode == 4:
            names = set()
            labels = [word(rng, names) for _ in range(groups * pots - groups - 1)]
            labels += [word(rng, names)] * (groups + 1)
            rng.shuffle(labels)
        else:
            names = set()
            parties = [word(rng, names) for _ in range(groups * pots // FEW)]
            labels = [rng.choice(parties) for _ in range(groups * pots)]
            while max(Counter(labels).values()) > groups:
                labels = [rng.choice(parties) for _ in range(groups * pots)]
    teams = set()
    lines = ["%d %d" % (groups, pots)]
    for p in range(pots):
        if p > 0:
            lines.append("")
        for g in range(groups):
            lines.append("%s %s" % (word(rng, teams), labels[p * groups + g]))
    print("\n".join(lines))


main()
