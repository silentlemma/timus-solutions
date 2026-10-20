"""Queries from "MODE SEED":
1: a small n with every box asked.
2: n = 60 with 10^5 random boxes.
3: n = 60 with the small boxes and the largest ones.
4: n = 1 with 10^5 queries of its sole box.
5: n = 60 with 10^5 shuffled queries cycling through boxes 1..61.
6: n = 37 with 10^5 random queries mixing small boxes, arbitrary boxes,
   and neighbors of powers of two.
"""

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
    elif mode == 4:
        n = 1
        boxes = [1] * MAX_Q
    elif mode == 5:
        n = MAX_N
        boxes = [1 + i % (MAX_N + 1) for i in range(MAX_Q)]
        rng.shuffle(boxes)
    elif mode == 6:
        n = 37
        top = (1 << n) - 1
        boundaries = sorted({a for bit in range(n + 1)
                             for a in ((1 << bit) - 1, 1 << bit, (1 << bit) + 1)
                             if 1 <= a <= top})
        boxes = []
        for _ in range(MAX_Q):
            kind = rng.randrange(3)
            if kind == 0:
                boxes.append(rng.randint(1, n + 2))
            elif kind == 1:
                boxes.append(rng.randint(1, top))
            else:
                boxes.append(rng.choice(boundaries))
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
