"""One test from a seed and a mode: mode 1 any tray up to 1000 with
plates up to half its width, mode 2 the same with values up to 12, mode
3 plates that, with high borders, fit exactly along the diagonal 3-4-5,
with the tray then made one larger, one smaller or left as it is."""

import random
import sys

LIMIT = 1000
SMALL = 12


def plate(rng, top):
    edge = rng.randint(2, top)
    return rng.randint(1, edge - 1), edge


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (1, 2):
        top = LIMIT if mode == 1 else SMALL
        a, b, d = (rng.randint(1, top) for _ in range(3))
        edge = max(2, min(a, b) // 2)
        plates = [plate(rng, edge), plate(rng, edge)]
        h = rng.randint(1, top)
    else:
        k = rng.randint(1, LIMIT // SMALL)
        first = rng.randint(k + 1, 4 * k - 1)
        second = 5 * k - first
        plates = [(rng.randint(1, first - 1), first), (rng.randint(1, second - 1), second)]
        a, b = 8 * k + rng.randint(-1, 1), 9 * k
        h = rng.randint(1, LIMIT)
        d = rng.randint(h, LIMIT)
        if rng.random() < 0.5:
            a, b = b, a
    print(a, b, d)
    for bottom, edge in plates:
        print(bottom, edge)
    print(h)


main()
