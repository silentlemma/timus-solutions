"""Cars from a seed and a mode: mode 1 a few cars close by, 2 the most
cars spread out, 3 the most cars bumper to bumper on both sides, 4 the
most cars with gaps that Egor can just slip through, 5 one car on each
side far away. Distances in a row grow by at least 5 metres."""

import random
import sys

MOST = 300
FEW = 4
FAR = 10000
CAR = 5
SLIP = 16


def row(rng, mode):
    if mode == 1:
        count, gap = rng.randint(1, FEW), (CAR, CAR + SLIP)
    elif mode == 2:
        count, gap = MOST, (CAR, FAR // MOST)
    elif mode == 3:
        count, gap = MOST, (CAR, CAR)
    elif mode == 4:
        count, gap = MOST, (CAR + SLIP - 1, CAR + SLIP + 1)
    else:
        return [rng.randint(FAR // 2, FAR)]
    d = rng.randint(1, CAR * FEW)
    out = [d]
    for _ in range(count - 1):
        d += rng.randint(*gap)
        out.append(d)
    return [x for x in out if x <= FAR] or [1]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    for _ in range(2):
        cars = row(rng, mode)
        print(len(cars))
        print(*cars)


main()
