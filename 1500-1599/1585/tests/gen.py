"""One test from a seed and a mode: penguin records with a single most
frequent kind. Mode 1 is 1000 random records, mode 2 a winner ahead by
one, mode 3 a few records."""

import random
import sys

KINDS = ["Emperor", "Little", "Macaroni"]
MOST = 1000
FEW = 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 2:
            base = rng.randint(1, MOST // 3 - 1)
            counts = [base, base, base]
            counts[rng.randrange(3)] += 1
        else:
            n = rng.randint(1, FEW) if mode == 3 else MOST
            records = [rng.choice(KINDS) for _ in range(n)]
            counts = [records.count(k) for k in KINDS]
        if sorted(counts)[-1] > sorted(counts)[-2]:
            break
    records = [k for k, c in zip(KINDS, counts) for _ in range(c)]
    rng.shuffle(records)
    print(len(records))
    print("\n".join(k + " Penguin" for k in records))


main()
