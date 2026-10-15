"""One test from a seed and a mode: mode 1 a few tournaments and
candidates with small ratings, so that ties are common, mode 2 100
tournaments and 100 candidates, mode 3 50 candidates who have all
played both with and without Lyosha, so the answer is Fail, mode 4
equal ratings."""

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


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
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
