"""One test from a seed and a mode: mode 1 the most pairs over all
diameters, mode 2 the most pairs over a few diameters, mode 3 a random
small test."""

import random
import sys

MOST = 150
SMALLEST, LARGEST = 600, 700


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        sizes = [rng.randint(SMALLEST, LARGEST) for _ in range(MOST)]
    elif mode == 2:
        few = [rng.randint(SMALLEST, LARGEST) for _ in range(rng.randint(1, 5))]
        sizes = [rng.choice(few) for _ in range(MOST)]
    else:
        sizes = [rng.randint(SMALLEST, SMALLEST + 3) for _ in range(rng.randint(1, 20))]
    print(len(sizes))
    print("\n".join(map(str, sizes)))


main()
