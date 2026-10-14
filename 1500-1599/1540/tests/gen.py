"""One test from a seed and a mode. Mode 1 takes 50 chains of 100 random
contents, mode 2 contents from 1 to 3, mode 3 a few short chains with
contents up to 4, mode 4 increasing chains, mode 5 one chain of 100,
mode 6 50 chains of 100 distinct contents arranged as a zigzag."""

import random
import sys

MOST_CHAINS = 50
LONGEST = 100
TOP = 100
FEW = 3
SHORT = 4


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        chains = [
            [rng.randint(1, SHORT) for _ in range(rng.randint(1, SHORT))]
            for _ in range(rng.randint(1, FEW))
        ]
    else:
        k = 1 if mode == 5 else MOST_CHAINS
        top = FEW if mode == 2 else TOP
        chains = []
        for _ in range(k):
            chain = [rng.randint(1, top) for _ in range(LONGEST)]
            if mode == 4:
                chain.sort()
            elif mode == 6:
                order = list(range(1, TOP + 1))
                chain = order[::2] + order[1::2][::-1]
            chains.append(chain)
    print(len(chains))
    for chain in chains:
        print(len(chain), *chain)


main()
