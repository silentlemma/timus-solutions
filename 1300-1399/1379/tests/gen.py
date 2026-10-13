"""Road maps: arguments are a seed and a mode.

Mode 1: 500 junctions, a complete graph of short roads.
Mode 2: 500 junctions, a short chain inside complete day-long roads.
Mode 3: 500 junctions, a sparse random graph.
Mode 4: 500 junctions, a shuffled chain taking exactly a day, with an
interior weight bottleneck and randomly reversed road endpoints.
Mode 5: 40 junctions, random roads with near-empty weight limits and
zero, short, half-day and day-long travel times.
"""

import random
import sys

COUNT = 500
TRUCK = 3_000_000
TOP = 10**9
DAY = 1440


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        times = [3] * 442 + [2] * 57
        rng.shuffle(times)
        bottleneck = rng.randint(COUNT // 3, 2 * COUNT // 3)
        roads = []
        for a, time in enumerate(times, 1):
            weight = TRUCK + 499 if a == bottleneck else rng.randint(TRUCK + 1000, TOP)
            ends = (a, a + 1) if rng.randrange(2) else (a + 1, a)
            roads.append((*ends, time, weight))
        rng.shuffle(roads)
        print(COUNT, len(roads))
        for road in roads:
            print(*road)
        return
    if mode == 5:
        n = 40
        weights = [0, TRUCK - 1, TRUCK, TRUCK + 1, TRUCK + 99,
                   TRUCK + 100, TRUCK + 199, TRUCK + 200, TRUCK + 999, TOP]
        times = [0, 0, 1, 2, 719, 720, 721, DAY]
        roads = []
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if rng.random() < 0.24:
                    ends = (a, b) if rng.randrange(2) else (b, a)
                    roads.append((*ends, rng.choice(times), rng.choice(weights)))
        rng.shuffle(roads)
        print(n, len(roads))
        for road in roads:
            print(*road)
        return
    n = COUNT
    roads = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if mode == 1:
                roads.append((a, b, rng.randint(0, 20), rng.randint(TRUCK, TOP)))
            elif mode == 2:
                t = 2 if b == a + 1 else DAY
                roads.append((a, b, t, rng.randint(TRUCK, TOP)))
            elif rng.random() < 0.01:
                roads.append((a, b, rng.randint(0, 300), rng.randint(0, TOP)))
    rng.shuffle(roads)
    print(n, len(roads))
    for r in roads:
        print(*r)


main()
