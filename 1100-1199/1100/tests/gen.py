"""Deterministic results tables.

SEED N MOST: random unique IDs and scores from 0 through MOST (legacy mode).
chunks SEED: shuffled teams with 4095, 4096 and 4097 entries at scores 0, 50, 100.
constant SEED N SCORE: random unique IDs, all with the given score.
"""

import random
import sys

TOP_ID = 10**7


def main():
    if sys.argv[1] == "chunks":
        rng = random.Random(int(sys.argv[2]))
        scores = [0] * 4095 + [50] * 4096 + [100] * 4097
        rng.shuffle(scores)
        ids = rng.sample(range(1, TOP_ID + 1), len(scores))
        lines = [str(len(scores))] + ["%d %d" % pair for pair in zip(ids, scores)]
        sys.stdout.write("\n".join(lines) + "\n")
        return
    if sys.argv[1] == "constant":
        seed, n, score = (int(x) for x in sys.argv[2:5])
        rng = random.Random(seed)
        ids = rng.sample(range(1, TOP_ID + 1), n)
        lines = [str(n)] + ["%d %d" % (i, score) for i in ids]
        sys.stdout.write("\n".join(lines) + "\n")
        return
    seed, n, most = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    ids = rng.sample(range(1, TOP_ID + 1), n)
    lines = [str(n)] + ["%d %d" % (i, rng.randint(0, most)) for i in ids]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
