"""One test from a seed and a mode: mode 1 up to 8 dominoes with small
numbers, mode 2 100000 dominoes forming two nested families around
overlapping cores, so that the answer is YES, mode 3 the same with one
domino replaced by a range off to the side, mode 4 100000 random
dominoes."""

import random
import sys

FEW = 8
SMALL = 9
MOST = 100000
LIMIT = 10 ** 6
MIDDLE = LIMIT // 2
CORES = ((MIDDLE - 10, MIDDLE + 10), (MIDDLE + 5, MIDDLE + 30))
ASIDE = (MIDDLE + 40, MIDDLE + 50)


def family(rng, low, high, count):
    # ranges that all contain [low, high], nested inside one another
    lows = sorted(rng.randint(0, low) for _ in range(count))
    highs = sorted((rng.randint(high, LIMIT) for _ in range(count)), reverse=True)
    return list(zip(lows, highs))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        pieces = [(rng.randint(0, SMALL), rng.randint(0, SMALL))
                  for _ in range(rng.randint(1, FEW))]
    elif mode == 4:
        pieces = [(rng.randint(0, LIMIT), rng.randint(0, LIMIT)) for _ in range(MOST)]
    else:
        pieces = []
        for low, high in CORES:
            pieces += family(rng, low, high, MOST // len(CORES))
        if mode == 3:
            pieces[rng.randrange(len(pieces))] = ASIDE
        pieces = [p if rng.random() < 0.5 else p[::-1] for p in pieces]
        rng.shuffle(pieces)
    print(len(pieces))
    print("\n".join("%d %d" % p for p in pieces))


main()
