"""One test from a seed and a mode: mode 1 a few universities with many
teams each, mode 2 many universities with one team each, mode 3 names
written in mixed letter case, mode 4 the largest protocol with names
that are prefixes of one another."""

import random
import string
import sys

MOST_N = 201
MOST_TEAMS = 8
MOST_NAME = 36
WORDS = ["Ural", "SU", "State", "University", "St", "Petersburg", "IFMO", "Moscow",
         "Saratov", "Tech.", "Inst-of", "Arts&Sciences", "Novosibirsk", "Belarusian", "U"]


def university(rng):
    while True:
        name = " ".join(rng.choice(WORDS) for _ in range(rng.randint(1, 4)))
        if len(name) <= MOST_NAME:
            return name


def recase(name, rng):
    return "".join(c.swapcase() if c in string.ascii_letters and rng.random() < 0.3 else c
                   for c in name)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    q = rng.randint(3, 12)
    count = {1: q + 2, 2: MOST_N, 3: q + rng.randint(1, 10), 4: q + 10}[mode]
    names = []
    while len(names) < count:
        name = university(rng)
        if mode == 4 and names and rng.random() < 0.5:
            name = (rng.choice(names) + " " + rng.choice(WORDS))[:MOST_NAME].rstrip()
        if name.lower() not in {x.lower() for x in names}:
            names.append(name)
    teams = []
    for name in names:
        k = 1 if mode == 2 else rng.randint(1, MOST_TEAMS)
        teams += [(name, j) for j in rng.sample(range(1, MOST_TEAMS + 1), k)]
    rng.shuffle(teams)
    teams = teams[:MOST_N] if mode != 1 else teams
    # keep the answer: q + 1 different universities must stay
    while len({t[0] for t in teams}) <= q:
        teams.append((names[len(teams) % len(names)], 1))
    sizes = {}
    for name, _ in teams:
        sizes[name] = sizes.get(name, 0) + 1
    print(rng.randint(1996, 2008), len(teams), q)
    for name, j in teams:
        shown = recase(name, rng) if mode == 3 else name
        alone = sizes[name] == 1 and rng.random() < 0.5
        print(shown if alone else "%s #%d" % (shown, j))


main()
