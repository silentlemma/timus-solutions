"""One test from a seed and a mode: a random seating of fans in buses,
then some fans asked; mode 1 up to 5 small buses, mode 2 up to 100 000 fans
with many of them asked, mode 3 the same with one answer changed,
mode 4 up to 100 000 fans and only a few asked, mode 5 exactly 100 000
fans and buses with everyone except the target asked and b = n,
mode 6 exactly 100 000 fans with 50 000 possible buses, mode 7 exactly
100 000 fans in random buses of size 2 to 6 with n - 1 shuffled reports.
Usage: gen.py SEED MODE; every mode is deterministic."""

import random
import sys

FEW_BUSES = 5
SMALL = 5
MOST = 100000
MANY_BUSES = 1000
FEW_ASKED = 5
TRUTH = 0.9


def maximum_case(rng, mode):
    if mode == 6:
        print(MOST, MOST // 2, 1, MOST)
        print(MOST // 2)
        print(1)
        print(MOST, MOST // 2)
        return
    if mode == 5:
        sizes = [1] * MOST
        a, b = 1, MOST
    else:
        sizes = []
        for _ in range(MOST // 8):
            size = rng.randint(2, 6)
            sizes.extend((size, 8 - size))
        rng.shuffle(sizes)
        a, b = 2, 6
    bus_of = [bus for bus, size in enumerate(sizes, 1) for _ in range(size)]
    r = rng.randint(2, MOST - 1)
    asked = [fan for fan in range(1, MOST + 1) if fan != r]
    rng.shuffle(asked)
    print(MOST, len(sizes), a, b)
    print(r)
    print(len(asked))
    for fan in asked:
        print(fan, bus_of[fan - 1])


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        maximum_case(rng, mode)
        return
    if mode == 1:
        m = rng.randint(2, FEW_BUSES)
        a = rng.randint(1, SMALL - 2)
        b = rng.randint(a, SMALL)
        sizes = [rng.randint(a, b) for _ in range(m)]
    else:
        m = rng.randint(2, MANY_BUSES)
        a = rng.randint(1, MOST // m)
        b = rng.randint(a, MOST // m)
        sizes = [rng.randint(a, b) for _ in range(m)]
    n = sum(sizes)
    if n < 2:
        sizes[0] += 1
        n += 1
        b = max(b, sizes[0])
    borders = [0]
    for size in sizes:
        borders.append(borders[-1] + size)
    bus_of = {}
    for k in range(m):
        for fan in range(borders[k] + 1, borders[k + 1] + 1):
            bus_of[fan] = k + 1
    r = rng.randint(1, n)
    if mode == 1:
        s = rng.randint(1, min(4, n - 1))
    elif mode == 4:
        s = rng.randint(1, FEW_ASKED)
    else:
        s = rng.randint(1, n - 1)
    asked = rng.sample([x for x in range(1, n + 1) if x != r], s)
    answers = []
    for fan in asked:
        bus = bus_of[fan]
        if mode == 1 and rng.random() > TRUTH:
            bus = rng.randint(1, m)
        answers.append((fan, bus))
    if mode == 3:
        i = rng.randrange(s)
        fan, bus = answers[i]
        answers[i] = (fan, bus % m + 1)
    print(n, m, a, b)
    print(r)
    print(s)
    for fan, bus in answers:
        print(fan, bus)


main()
