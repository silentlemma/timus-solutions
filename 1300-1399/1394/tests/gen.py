"""Hard fleets: a seed and a mode. The ships are dealt into the rows at
random, so a placement exists. Mode 1 draws 99 ships of any length into 9
rows, mode 2 99 ships of 88 to 100, mode 3 mostly equal ships, mode 4 long
ships from 86 to 100 with a few short ones that must fix the remainders,
mode 5 a few distinct lengths repeated with one very long row, mode 6 any
fleet in two rows, mode 7 multiples of some k with one special ship per row
whose residue pins its row, mode 8 even ships with one odd ship per row,
mode 9 complementary pairs totaling 101 in nine equal rows, mode 10 five
rows of three random ships from 76 to 100 (every row needs exactly three)."""

import random
import sys

SHIPS = 99
ROWS = 9
TOP = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (9, 10):
        groups = []
        if mode == 9:
            for _ in range(ROWS):
                length = rng.randint(34, 50)
                groups.append([length, 101 - length])
        else:
            groups = [[rng.randint(76, TOP) for _ in range(3)] for _ in range(5)]
        ships = [ship for group in groups for ship in group]
        rows = [sum(group) for group in groups]
        rng.shuffle(ships)
        rng.shuffle(rows)
        print(len(ships), len(rows))
        print("\n".join(map(str, ships)))
        print("\n".join(map(str, rows)))
        return
    n, m = SHIPS, ROWS
    if mode == 1:
        ships = [rng.randint(1, TOP) for _ in range(n)]
    elif mode == 2:
        ships = [rng.randint(88, TOP) for _ in range(n)]
    elif mode == 3:
        common = rng.randint(30, 70)
        ships = [common if rng.random() < 0.8 else rng.randint(1, TOP) for _ in range(n)]
    elif mode == 4:
        n, m = rng.randint(40, 60), rng.randint(6, ROWS)
        short = rng.randint(4, 12)
        ships = [rng.randint(86, TOP) for _ in range(n - short)]
        ships += [rng.randint(1, 60) for _ in range(short)]
    elif mode == 5:
        ships = []
        for length in rng.sample(range(5, TOP + 1), rng.randint(8, 14)):
            ships += [length] * rng.randint(1, 10)
        ships = ships[:SHIPS]
        n = len(ships)
    elif mode == 6:
        m = 2
        ships = [rng.randint(1, TOP) for _ in range(n)]
    else:
        # one special ship per row, the rest multiples of k (mode 7) or even (mode 8)
        k = rng.randint(5, 12) if mode == 7 else 2
        special = [rng.choice([x for x in range(1, TOP + 1) if x % k]) for _ in range(m)]
        common = [k * rng.randint(1, TOP // k) for _ in range(n - m)]
        owner = list(range(m)) + [rng.randrange(m) for _ in range(n - m)]
        ships = special + common
    if mode < 7:
        # every row gets one ship, then most ships go to random rows and the rest to row 0
        owner = list(range(m)) + [
            rng.randrange(m) if rng.random() < 0.7 else 0 for _ in range(n - m)
        ]
        rng.shuffle(owner)
    rows = [0] * m
    for s, r in zip(ships, owner):
        rows[r] += s
    rng.shuffle(rows)
    if mode >= 7:
        rng.shuffle(ships)
    print(n, m)
    print("\n".join(map(str, ships)))
    print("\n".join(map(str, rows)))


main()
