"""Random distinct multisets: a seed, N, K, M, the largest set size and a
mode. Mode 0 draws independent sets, mode 1 grows families of similar sets
by removing, adding and replacing items of a few base sets, mode 2 draws
sets of the largest size only. When fewer than K distinct sets turn up,
all of them are written."""

import random
import sys

PATIENCE = 100


def main():
    seed, n, k, m, top, mode = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    seen = set()
    sets = []

    def add(items):
        key = tuple(sorted(items))
        if 0 < len(items) <= top and key not in seen:
            seen.add(key)
            sets.append(items)

    # few distinct sets may exist for small N, so give up after many tries
    for _ in range(PATIENCE * k):
        if len(sets) >= k:
            break
        size = top if mode == 2 else rng.randint(1, top)
        items = [rng.randint(1, n) for _ in range(size)]
        add(items)
        if mode == 1:
            for _ in range(rng.randint(1, top)):
                if len(sets) >= k:
                    break
                variant = list(rng.choice(sets))
                change = rng.randrange(3)
                if change == 0 and len(variant) > 1:
                    variant.pop(rng.randrange(len(variant)))
                elif change == 1:
                    variant.insert(rng.randrange(len(variant) + 1), rng.randint(1, n))
                else:
                    variant[rng.randrange(len(variant))] = rng.randint(1, n)
                add(variant)
    lines = ["%d %d %d" % (n, len(sets), m)]
    for items in sets:
        rng.shuffle(items)
        lines.append(" ".join(map(str, [len(items)] + items)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
