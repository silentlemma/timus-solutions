"""One test from a seed and a mode: up to 1000 numbers from 1 to 10. Mode
1 draws them at random, mode 2 makes long runs, mode 3 makes no two
neighbours equal, mode 4 is short."""

import random
import sys

LONGEST = 1000
TOP = 10
SHORT = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SHORT) if mode == 4 else LONGEST
    numbers = []
    while len(numbers) < n:
        value = rng.randint(1, TOP)
        if mode == 3 and numbers and numbers[-1] == value:
            continue
        numbers += [value] * (rng.randint(1, 100) if mode == 2 else 1)
    numbers = numbers[:n]
    print(n)
    print(*numbers)


main()
