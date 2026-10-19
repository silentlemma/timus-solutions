"""Cards and uses from a seed.

Mode 1: a few cards and uses. Mode 2: 10^5 cards and 10^5 random uses.
Mode 3: 10^5 cards, uses among ten of them. Mode 4: every card used once,
in a random order. Mode 5: a single card used 10^5 times.
Mode 6: 10^5 cards and one use of the highest-numbered card.
Mode 7: a card returns after 99998 distinct cards, with one card unused.
Mode 8: two cards alternate in random runs over 10^5 uses.
Mode 9: 10^5 uses in random phases with changing, overlapping active groups.
"""

import random
import sys

SMALL = 8
MAX = 10 ** 5
FEW = 10


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n, k = rng.randint(1, SMALL), rng.randint(1, SMALL)
        uses = [rng.randint(1, n) for _ in range(k)]
    elif mode == 2:
        n = k = MAX
        uses = [rng.randint(1, n) for _ in range(k)]
    elif mode == 3:
        n = k = MAX
        few = rng.sample(range(1, n + 1), FEW)
        uses = [rng.choice(few) for _ in range(k)]
    elif mode == 4:
        n = k = MAX
        uses = rng.sample(range(1, n + 1), n)
    elif mode == 6:
        n, k = MAX, 1
        uses = [n]
    elif mode == 7:
        n = k = MAX
        middle = list(range(2, n))
        rng.shuffle(middle)
        uses = [1] + middle + [1]
    elif mode == 8:
        n, k = 2, MAX
        uses = []
        card = rng.randint(1, n)
        while len(uses) < k:
            uses.extend([card] * rng.choice([1, 2, 3, 31, 511, 512, 513, 4096]))
            card = 3 - card
        uses = uses[:k]
    elif mode == 9:
        n = k = MAX
        pool = [1, n] + rng.sample(range(2, n), 62)
        groups = [pool[:16], pool[8:32], pool[24:48], pool[:8] + pool[48:]]
        uses = [rng.choice(groups[phase % len(groups)])
                for phase in range(8) for _ in range(k // 8)]
    else:
        n, k = 1, MAX
        uses = [1] * k
    print(n, k)
    print(*uses)


main()
