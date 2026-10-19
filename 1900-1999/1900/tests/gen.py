"""Generate from seed and mode: 1 small, 2 maximal dense, 3 maximal zero,
4 one cut, 5 quarter cuts, 6 half cuts, 7 all cuts, 8 neighboring trips."""

import random
import sys


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    maximum_n = 500
    n = 10 if mode == 1 else maximum_n
    cuts = {1: 4, 2: 250, 3: 250, 4: 1, 5: 125, 6: 250, 7: 499, 8: 249}
    print(n, cuts[mode])
    for left in range(1, n):
        row = []
        for right in range(left + 1, n + 1):
            if mode == 2:
                value = 100
            elif mode == 3:
                value = 0
            elif mode == 8:
                value = rng.randrange(101) if right == left + 1 else 0
            else:
                value = rng.randrange(101)
            row.append(str(value))
        print(" ".join(row))


if __name__ == "__main__":
    main()
