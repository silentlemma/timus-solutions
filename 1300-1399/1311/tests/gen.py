"""A brick wall from the top layer down: a seed and a mode. Mode 1 gives a
few small layers, mode 2 a tower of 10000 one-brick layers, mode 3 100
layers of 1000 bricks that sit almost straight on each other, mode 4 the
same with one brick missing in the middle of the wall."""

import random
import sys

TOWER = 10000
ROWS, PER_ROW, PITCH = 100, 1000, 10


def small(rng):
    layers = []
    bottom, x = [], rng.randint(0, 3)
    for _ in range(rng.randint(1, 4)):
        length = rng.randint(1, 8)
        bottom.append((x, x + length))
        x += length + rng.randint(1, 4)
    layers.append(bottom)
    for _ in range(rng.randint(0, 5)):
        below, row = layers[-1], []
        for i, (left, right) in enumerate(below):
            if rng.random() < 0.2:
                continue
            # stay clear of the neighbours below and of the brick before
            lo = max(below[i - 1][1] if i else 0, row[-1][1] + 1 if row else 0, left - 4)
            hi = below[i + 1][0] if i + 1 < len(below) else right + 6
            a = rng.randint(lo, right - 1) if lo <= right - 1 else None
            if a is None:
                continue
            b = rng.randint(max(a + 1, left + 1), max(a + 1, left + 1, hi))
            if b <= hi and min(b, right) > max(a, left):
                row.append((a, b))
        if not row:
            break
        layers.append(row)
    return layers[::-1]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        layers = small(rng)
    elif mode == 2:
        width = rng.randint(2, 20)
        layers = [[(0, width)] for _ in range(TOWER)]
    else:
        layers = []
        for _ in range(ROWS):
            shift = [rng.randint(-1, 1) for _ in range(PER_ROW)]
            layers.append([(PITCH * i + 1 + s, PITCH * i + 8 + s) for i, s in enumerate(shift)])
        if mode == 4:
            row = layers[ROWS // 2]
            del row[rng.randrange(len(row))]
    print(len(layers))
    for row in layers:
        print(len(row))
        for left, right in row:
            print(left, right)


main()
