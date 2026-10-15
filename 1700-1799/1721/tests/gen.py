"""One test from a seed and a mode: mode 1 a few people with ranks from 3
to 12, mode 2 1000 people with any ranks, mode 3 1000 people with ranks 3
and 5 only, so that every possible pair is an edge, mode 4 1000 people
with ranks from 3 to 20, so that long chains of ranks appear; mode 5 a
descending 498-person path and 502 isolated testers, forcing a long
augmenting path; mode 6 500 universal people at each of ranks 3 and 5,
giving all 250000 edges. Modes 5 and 6 use 20-letter names."""

import random
import string
import sys

KINDS = ("statements", "testdata", "anything")
LOW = 3
HIGH = 1000
MOST = 1000
FEW = 8
SMALL_TOP = 12
CHAIN_TOP = 20
NAME = 20


def name(rng, taken):
    while True:
        size = rng.randint(1, NAME)
        word = "".join(rng.choice(string.ascii_letters) for _ in range(size))
        if word not in taken:
            taken.add(word)
            return word


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6):
        taken = set()
        print(MOST)
        if mode == 5:
            rows = [("anything", rank) for rank in range(HIGH - 2, LOW, -2)]
            rows += [("testdata", HIGH - 1)] * (MOST - len(rows))
        else:
            rows = [("anything", LOW)] * (MOST // 2)
            rows += [("anything", LOW + 2)] * (MOST // 2)
            rng.shuffle(rows)
        for kind, rank in rows:
            while True:
                word = "".join(rng.choice(string.ascii_letters) for _ in range(NAME))
                if word not in taken:
                    taken.add(word)
                    break
            print(word, kind, rank)
        return
    if mode == 1:
        n, top = rng.randint(2, FEW), SMALL_TOP
    else:
        n, top = MOST, CHAIN_TOP if mode == 4 else HIGH
    taken = set()
    print(n)
    for _ in range(n):
        rank = rng.randint(LOW, top)
        if mode == 3:
            rank = rng.choice((LOW, LOW + 2))
        print(name(rng, taken), rng.choice(KINDS), rank)


main()
