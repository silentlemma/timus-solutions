"""One test from a seed and a mode: mode 1 a few demons nearby, mode 2 a
hundred demons over the whole field, mode 3 demons at the corners."""

import random
import sys

FIELD = 1000
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        demons = {(sx * FIELD, sy * FIELD) for sx in (-1, 1) for sy in (-1, 1)}
        demons |= {(rng.randint(-FIELD, FIELD), rng.randint(-FIELD, FIELD)) for _ in range(10)}
    else:
        n = MOST if mode == 2 else rng.randint(1, 10)
        span = FIELD if mode == 2 else 10
        demons = set()
        while len(demons) < n:
            demons.add((rng.randint(-span, span), rng.randint(-span, span)))
    demons.discard((0, 0))
    if not demons:
        demons.add((1, 0))
    demons = list(demons)
    rng.shuffle(demons)
    print(len(demons))
    for x, y in demons:
        print(x, y)


main()
