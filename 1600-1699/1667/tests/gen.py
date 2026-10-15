"""One test from a seed and a mode: twenty tables of mode 1 random sizes,
mode 2 sizes from 17 to 20, mode 3 square tables, mode 4 one side of 1 or
2 and the other up to 20."""

import random
import sys

MOST = 20
TESTS = 20


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
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
