"""One test from a seed and a mode.

1: random size, weights and record; 2: change the pan at every step;
3: never change the pan; 4: close weights and a random record;
5: two extreme weight clusters and runs of length two;
6: random weights and successive winner runs of lengths 1, 2, 3, ... .
"""

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
    if mode == 5:
        half = LARGEST // 2
        weights = list(range(1, half + 1)) + list(range(HEAVIEST - half + 1, HEAVIEST + 1))
        rng.shuffle(weights)
    first = rng.choice("LR")
    if mode == 2:
        record = "".join(first if i % 2 == 0 else "LR".replace(first, "") for i in range(n))
    elif mode == 3:
        record = first * n
    elif mode == 5:
        other = "R" if first == "L" else "L"
        record = "".join(first if i // 2 % 2 == 0 else other for i in range(n))
    elif mode == 6:
        record = ""
        pan = first
        length = 1
        while len(record) < n:
            record += pan * min(length, n - len(record))
            pan = "R" if pan == "L" else "L"
            length += 1
    else:
        record = "".join(rng.choice("LR") for _ in range(n))
    print(n)
    print(" ".join(map(str, weights)))
    print(record)


main()
