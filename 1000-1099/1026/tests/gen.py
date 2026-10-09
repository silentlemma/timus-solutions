"""Deterministic database modes:

SEED N TOP K: random values in 1..TOP and random ranks (original mode).
skew SEED: 100000 values, a run of 70000, and boundary plus random ranks.
exhaustive SEED: 100 random sparse values and every rank in shuffled order.
"""

import random
import sys

SEPARATOR = "###"


def main():
    if sys.argv[1] in ("skew", "exhaustive"):
        mode = sys.argv[1]
        rng = random.Random(int(sys.argv[2]))
        if mode == "skew":
            values = [1] + [2] * 70000 + [4096] * 29997 + [4999, 5000]
            queries = [1, 2, 70000, 70001, 70002, 99997, 99998, 99999, 100000]
            queries += [rng.randint(1, len(values)) for _ in range(100 - len(queries))]
            rng.shuffle(values)
        else:
            palette = [1, 2, 9, 10, 99, 100, 999, 1000, 4096, 4999, 5000]
            values = [rng.choice(palette) for _ in range(100)]
            queries = list(range(1, len(values) + 1))
        rng.shuffle(queries)
        lines = [str(len(values))] + [str(value) for value in values]
        lines += [SEPARATOR, str(len(queries))] + [str(rank) for rank in queries]
        print("\n".join(lines))
        return

    seed, n, top, k = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = [str(n)] + [str(rng.randint(1, top)) for _ in range(n)]
    lines += [SEPARATOR, str(k)] + [str(rng.randint(1, n)) for _ in range(k)]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
