"""One test from a seed and a mode: mode 1 a few tournaments and
candidates with small ratings, so that ties are common, mode 2 100
tournaments and 100 candidates, mode 3 50 candidates who have all
played both with and without Lyosha, so the answer is Fail, mode 4
equal ratings, mode 5 100 candidates whose triples all appeared but
whose pairs are new, mode 6 50 blocked candidates and one fresh
candidate after the maximum 100 tournaments."""

import random
import string
import sys

LYOSHA = "Efremov"
VADIK = "Kantorov"
MOST = 100
FEW = 6
TOP = 666
LOW = 5
NAME = 8


def word(rng, taken):
    while True:
        rest = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(0, NAME)))
        w = rng.choice(string.ascii_uppercase) + rest
        if w not in taken:
            taken.add(w)
            return w


def structured(rng, mode):
    taken = {LYOSHA, VADIK}
    m = MOST if mode == 5 else MOST // 2 + 1
    candidates = [word(rng, taken) for _ in range(m)]
    teams = []
    for c in candidates if mode == 5 else candidates[:-1]:
        teams.append(sorted((LYOSHA, VADIK, c)))
        if mode == 6:
            teams.append(sorted((VADIK, c)))
    rng.shuffle(teams)
    print(len(teams))
    for team in teams:
        print(len(team), " ".join(team))
    print(TOP, TOP if mode == 5 else 1)
    print(m)
    if mode == 5:
        ratings = [1, TOP] + [rng.randint(1, TOP - 1) for _ in range(m - 2)]
        rng.shuffle(ratings)
    else:
        ratings = [TOP] * (m - 1) + [1]
    for c, rating in zip(candidates, ratings):
        print(c, rating)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6):
        structured(rng, mode)
        return
    m = rng.randint(1, FEW) if mode == 1 else MOST
    if mode == 3:
        m = MOST // 2
    taken = {LYOSHA, VADIK}
    candidates = [word(rng, taken) for _ in range(m)]
    others = [word(rng, taken) for _ in range(FEW)]
    teams = set()
    if mode == 3:
        for c in candidates:
            teams.add(frozenset((LYOSHA, VADIK, c)))
            teams.add(frozenset((VADIK, c)))
    limit = rng.randint(1, FEW) if mode == 1 else MOST
    tries = 0
    while len(teams) < limit and tries < MOST * MOST:
        tries += 1
        third = rng.choice(candidates + others)
        kind = rng.randint(1, 4)
        if kind == 1:
            teams.add(frozenset((LYOSHA, VADIK, third)))
        elif kind == 2:
            teams.add(frozenset((VADIK, third)))
        elif kind == 3:
            teams.add(frozenset((LYOSHA, VADIK)))
        else:
            teams.add(frozenset((VADIK,)))
    top = LOW if mode == 1 else TOP
    print(len(teams))
    for t in sorted(teams, key=sorted):
        print(len(t), " ".join(sorted(t)))
    print(rng.randint(1, top), rng.randint(1, top))
    print(m)
    same = rng.randint(1, top)
    for c in candidates:
        print(c, same if mode == 4 else rng.randint(1, top))


main()
