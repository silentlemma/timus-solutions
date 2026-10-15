"""One test from a seed and a mode: mode 1 a few towns, mode 2 a thousand
towns of any size, mode 3 a thousand towns with only a few sizes, mode 4 a
thousand large towns, where many tolls coincide, mode 5 nine towns sampled
around integer-division boundaries, mode 6 a thousand shuffled towns of
sizes 500 and 501 with a one-unit penalty per extra pair of crossings."""

import random
import sys

MOST = 1000
TOP = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, 12)
        people = [rng.randint(1, rng.choice((5, TOP))) for _ in range(n)]
    elif mode == 3:
        sizes = [rng.randint(1, TOP) for _ in range(rng.randint(2, 6))]
        people = [rng.choice(sizes) for _ in range(MOST)]
    elif mode == 5:
        sizes = sorted({TOP // k + delta for k in range(2, 21)
                        for delta in (-1, 0, 1)})
        people = rng.sample(sizes, 9)
    elif mode == 6:
        count = rng.randint(MOST // 4, 3 * MOST // 4)
        people = [500] * count + [501] * (MOST - count)
        rng.shuffle(people)
    else:
        low = TOP // 3 if mode == 4 else 1
        people = [rng.randint(low, TOP) for _ in range(MOST)]
    print(len(people))
    print(" ".join(map(str, people)))


main()
