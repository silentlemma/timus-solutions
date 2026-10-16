"""One test from a seed and a mode: a random seating of fans in buses,
then some fans asked; mode 1 up to 5 small buses, mode 2 100 000 fans
with many of them asked, mode 3 the same with one answer changed,
mode 4 100 000 fans and only a few asked."""

import random
import sys

FEW_BUSES = 5
SMALL = 5
MOST = 100000
MANY_BUSES = 1000
FEW_ASKED = 5
TRUTH = 0.9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
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
