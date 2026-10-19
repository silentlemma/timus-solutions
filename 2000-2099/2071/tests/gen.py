"""Orders from a seed.

Mode 1: up to 7 glasses. Mode 2: 10^5 glasses of all cocktails. Mode 3:
10^5 glasses of a random set of cocktails. Mode 4: 10^5 glasses, all ABP
except one randomly placed P. Mode 5: 10^5 shuffled two-juice cocktails,
with all three pairs guaranteed to occur.
"""

import random
import sys

COCKTAILS = ["A", "B", "P", "AB", "AP", "BP", "ABP"]
SMALL = 7
MAX_N = 10 ** 5


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 4:
        rare = rng.randrange(MAX_N)
        print(MAX_N)
        for i in range(MAX_N):
            print("P" if i == rare else "ABP")
        return
    if mode == 5:
        pairs = ["AB", "AP", "BP"]
        orders = pairs + [rng.choice(pairs) for _ in range(MAX_N - len(pairs))]
        rng.shuffle(orders)
        print(MAX_N)
        print("\n".join(orders))
        return
    kinds = COCKTAILS
    if mode == 1:
        n = rng.randint(1, SMALL)
    else:
        n = MAX_N
        if mode == 3:
            kinds = rng.sample(COCKTAILS, rng.randint(1, len(COCKTAILS)))
    print(n)
    for _ in range(n):
        print(rng.choice(kinds))


main()
