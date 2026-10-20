"""Queries from "MODE SEED": mode 1 a small n with every box asked, mode 2
n = 60 with 10^5 random boxes, mode 3 n = 60 with the small boxes and the
largest ones."""

import random
import sys

MAX_N = 60
MAX_Q = 10 ** 5
SMALL_N = 8


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        boxes = list(range(1, (1 << n)))
        rng.shuffle(boxes)
    else:
        n = MAX_N
        top = (1 << n) - 1
        if mode == 2:
            boxes = [rng.randint(1, top) for _ in range(MAX_Q)]
        else:
            boxes = list(range(1, MAX_N + 2)) + [top - i for i in range(MAX_N)]
    print(n)
    print(len(boxes))
    print(*boxes)


main()
