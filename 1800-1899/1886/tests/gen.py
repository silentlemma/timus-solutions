"""Flights from a seed and a mode: mode 1 a few airports and flights,
2 the most airports and flights at random, 3 a long line of airports
with several flights between neighbours at growing times, 4 many direct
flights from airport 1 to the last one, 5 a few airports linked by the
most flights, 6 like 5 with times, durations and delays up to 10^9,
7 an intermediate airport with strictly improving earlier departures,
8 the longest chain with every delayed connection exactly catchable,
9 dense random schedules across branching layers with a fallback chain.
Modes 7-9 accept an optional third argument: flight count for 7 and 9,
airport count for 8 (defaults: 100000, 100000, 500 respectively)."""

import random
import sys

MOST = 100000
FEW = 6
SOME = 50
LINE = 2000
BIG = 10 ** 9


def flight(rng, a, b, t, scale):
    return (a, b, t, rng.randint(1, scale), rng.randint(1, 99), rng.randint(1, scale))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    out = []
    if mode == 1:
        n = rng.randint(2, FEW)
        for _ in range(rng.randint(1, FEW * 2)):
            a, b = rng.sample(range(1, n + 1), 2)
            out.append(flight(rng, a, b, rng.randint(1, SOME), FEW))
    elif mode == 2:
        n = MOST
        for _ in range(MOST):
            a, b = rng.sample(range(1, n + 1), 2)
            out.append(flight(rng, a, b, rng.randint(1, BIG), BIG))
    elif mode == 3:
        n = LINE
        per = MOST // n
        for a in range(1, n):
            for k in range(per):
                t = a * SOME * per + k * SOME + rng.randint(0, SOME)
                out.append(flight(rng, a, a + 1, t, SOME * per // 2))
    elif mode == 4:
        n = rng.randint(2, MOST)
        for _ in range(MOST):
            out.append(flight(rng, 1, n, rng.randint(1, BIG), BIG))
    elif mode == 7:
        count = int(sys.argv[3]) if len(sys.argv) > 3 else MOST
        assert 4 <= count <= MOST
        n = 3
        out.append((1, 2, 1, 1, 99, count - 2))
        for t in range(2, count + 1):
            out.append((2, 3, t, 1, 1, 1))
        rng.shuffle(out)
    elif mode == 8:
        n = int(sys.argv[3]) if len(sys.argv) > 3 else MOST
        assert 2 <= n <= MOST
        for a in range(1, n):
            out.append((a, a + 1, 2 * a - 1, 1, rng.randint(1, 99), 1))
        out.append((n, 1, BIG, 1, 99, 1))
        rng.shuffle(out)
    elif mode == 9:
        count = int(sys.argv[3]) if len(sys.argv) > 3 else 500
        assert 4 <= count <= MOST
        n = 11
        layers = [(1,), (2, 3, 4), (5, 6, 7), (8, 9, 10), (n,)]
        for leg in range(4):
            out.append(flight(rng, layers[leg][0], layers[leg + 1][0],
                              20 * (leg + 1), FEW))
        for _ in range(count - len(out)):
            leg = rng.randrange(4)
            a = rng.choice(layers[leg])
            b = rng.choice(layers[leg + 1])
            out.append(flight(rng, a, b, rng.randint(1 + 5 * leg, 20 + 15 * leg), FEW))
        rng.shuffle(out)
    else:
        n = rng.randint(2, FEW * 2)
        scale = BIG if mode == 6 else SOME * SOME
        for _ in range(MOST):
            a, b = rng.sample(range(1, n + 1), 2)
            t = rng.randint(1, BIG) if mode == 6 else rng.randint(1, scale * SOME)
            out.append(flight(rng, a, b, t, scale))
    print(n, len(out))
    print("\n".join(" ".join(map(str, f)) for f in out))


main()
