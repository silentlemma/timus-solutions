"""One test from a seed and a mode: mode 1 is random, mode 2 changes the
pan at every step, mode 3 never changes it, mode 4 uses close weights."""

import random
import sys

LARGEST = 50
HEAVIEST = 1000
CLOSE = 60


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, LARGEST) if mode == 1 else LARGEST
    weights = rng.sample(range(1, (CLOSE if mode == 4 else HEAVIEST) + 1), n)
    first = rng.choice("LR")
    if mode == 2:
        record = "".join(first if i % 2 == 0 else "LR".replace(first, "") for i in range(n))
    elif mode == 3:
        record = first * n
    else:
        record = "".join(rng.choice("LR") for _ in range(n))
    print(n)
    print(" ".join(map(str, weights)))
    print(record)


main()
