"""1000 test cases from a seed and a mode, ending with 0 0. Mode 1 draws
eggs and floors up to 10^18, mode 2 has two eggs and huge buildings, mode
3 has 2 to 70 eggs and 10^18 floors, mode 4 sits exactly on the edges
where one more floor needs one more drop, mode 5 has small numbers,
mode 6 alternates one, maximum and few eggs on large buildings, and
mode 7 draws small buildings where too few eggs prevent binary search."""

import random
import sys

MOST = 10**18
CASES = 1000
FEW_EGGS = 70
SMALL = 1000


def covered(t, k):
    total, term = 0, 1
    for i in range(1, min(k, t) + 1):
        term = term * (t - i + 1) // i
        total += term
    return total


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    cases = []
    while len(cases) < CASES:
        if mode == 1:
            k, n = rng.randint(1, MOST), rng.randint(1, MOST)
            if rng.random() < 0.5:
                k = rng.randint(1, FEW_EGGS)
        elif mode == 2:
            k, n = 2, rng.randint(MOST // 2, MOST)
        elif mode == 3:
            k, n = rng.randint(2, FEW_EGGS), MOST
        elif mode == 4:
            k = rng.randint(2, FEW_EGGS)
            t = rng.randint(1, 3000)
            n = covered(t, k) + rng.choice([0, 1])
            if n > MOST:
                continue
        elif mode == 6:
            branch = len(cases) % 3
            if branch == 0:
                k = 1
            elif branch == 1:
                k = MOST - rng.randrange(1000)
            else:
                k = rng.randint(2, 8)
            n = rng.randint(MOST // 2, MOST)
        elif mode == 7:
            k, n = rng.randint(2, 5), rng.randint(30, 160)
            if covered(n.bit_length(), k) >= n:
                continue
        else:
            k, n = rng.randint(1, SMALL), rng.randint(1, SMALL)
        cases.append((k, n))
    for k, n in cases:
        print(k, n)
    print(0, 0)


main()
