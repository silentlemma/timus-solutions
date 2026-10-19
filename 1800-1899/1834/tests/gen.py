"""One train from a seed and a mode: mode 1 a few random cars, mode 2
the longest random train, mode 3 a long train made of a given number of
runs that rise and fall in turn, mode 4 a long train made of runs that
fall and rise in turn, mode 5 a sorted long train with a few swaps,
mode 6 a sorted longest train, mode 7 adjacent pairs swapped (optional
third argument n, default 10000), mode 8 a random longest train sortable
in one pass, mode 9 all odd cars followed by all even cars at maximum n."""

import random
import sys

LIMIT = 10000
SMALL = 8


def from_runs(rng, n, count, rising):
    # cut 1 .. n into count runs of consecutive values and lay them out so
    # that the positions inside each run rise or fall as asked
    cuts = sorted(rng.sample(range(1, n), count - 1))
    bounds = [0] + cuts + [n]
    slots = list(range(n))
    rng.shuffle(slots)
    train = [0] * n
    at = 0
    for i in range(count):
        values = list(range(bounds[i] + 1, bounds[i + 1] + 1))
        places = sorted(slots[at:at + len(values)], reverse=not rising)
        at += len(values)
        for v, p in zip(values, places):
            train[p] = v
        rising = not rising
    return train


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 1 else LIMIT
    if mode == 7 and len(sys.argv) > 3:
        n = int(sys.argv[3])
        assert 2 <= n <= LIMIT
    if mode in (3, 4):
        train = from_runs(rng, n, rng.randint(1, 600), mode == 3)
    elif mode == 5:
        train = list(range(1, n + 1))
        for _ in range(rng.randint(1, 5)):
            i, j = rng.sample(range(n), 2)
            train[i], train[j] = train[j], train[i]
    elif mode == 6:
        train = list(range(1, n + 1))
    elif mode == 7:
        train = list(range(1, n + 1))
        for i in range(0, n - 1, 2):
            train[i], train[i + 1] = train[i + 1], train[i]
    elif mode == 8:
        # Inverse of one pass: interleave a prefix and a reversed suffix
        # of the sorted train, preserving the order inside both lists.
        pivot = rng.randint(n // 3, 2 * n // 3)
        places = set(rng.sample(range(n), pivot))
        low, high = 1, n
        train = []
        for i in range(n):
            if i in places:
                train.append(low)
                low += 1
            else:
                train.append(high)
                high -= 1
    elif mode == 9:
        train = list(range(1, n + 1, 2)) + list(range(2, n + 1, 2))
    else:
        train = list(range(1, n + 1))
        rng.shuffle(train)
    print(n)
    print(*train)


main()
