"""Numbers from "MODE SEED": mode 1 a few small numbers, mode 2 10^5 random
numbers below 2^20, mode 3 10^5 numbers next to a few fixed points, among them the
prime gap of 114 after 492113 and the top of the range,
mode 4 10^5 copies of one number."""

import random
import sys

MAX_T = 10 ** 5
TOP = (1 << 20) - 1
SMALL = 64
SMALL_T = 20
GAP_STARTS = [492113, 1048343, 1046861, 370261, 155921, 360653]
GAP = 114


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(0, SMALL) for _ in range(rng.randint(1, SMALL_T))]
    elif mode == 2:
        values = [rng.randint(0, TOP) for _ in range(MAX_T)]
    elif mode == 3:
        values = []
        for _ in range(MAX_T):
            start = rng.choice(GAP_STARTS)
            values.append(min(TOP, start + rng.randint(0, GAP)))
    else:
        values = [rng.randint(0, TOP)] * MAX_T
    print(len(values))
    print("\n".join(map(str, values)))


main()
