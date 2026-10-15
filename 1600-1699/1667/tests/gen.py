"""One test from a seed and a mode, always twenty tables.

1: random sizes; 2: sizes from 17 to 20; 3: random square tables;
4: one side of 1 or 2 and the other up to 20; 5: twenty 20 x 20 tables;
6: every row count with 20 columns, shuffled; 7: every column count with
20 rows, shuffled; 8: every square size, shuffled; 9: every pair whose
dimensions sum to 21, shuffled. Usage: python gen.py SEED MODE.
"""

import random
import sys

MOST = 20
TESTS = 20


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if 5 <= mode <= 9:
        if mode == 5:
            sizes = [(MOST, MOST)] * TESTS
        elif mode == 6:
            sizes = [(n, MOST) for n in range(1, MOST + 1)]
        elif mode == 7:
            sizes = [(MOST, m) for m in range(1, MOST + 1)]
        elif mode == 8:
            sizes = [(n, n) for n in range(1, MOST + 1)]
        else:
            sizes = [(n, MOST + 1 - n) for n in range(1, MOST + 1)]
        rng.shuffle(sizes)
        print(len(sizes))
        for n, m in sizes:
            print(n, m)
        return
    sizes = []
    for _ in range(TESTS):
        if mode == 1:
            sizes.append((rng.randint(1, MOST), rng.randint(1, MOST)))
        elif mode == 2:
            sizes.append((rng.randint(MOST - 3, MOST), rng.randint(MOST - 3, MOST)))
        elif mode == 3:
            n = rng.randint(1, MOST)
            sizes.append((n, n))
        else:
            pair = [rng.randint(1, 2), rng.randint(1, MOST)]
            rng.shuffle(pair)
            sizes.append(tuple(pair))
    print(len(sizes))
    for n, m in sizes:
        print(n, m)


main()
