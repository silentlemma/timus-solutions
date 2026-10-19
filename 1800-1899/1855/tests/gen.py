"""Events from a seed and a mode: mode 1 a few cities and events, 2 the
most cities and events at random, 3 every toll at its largest, then
guilds over long stretches, 4 the most events, almost all of them
changes, 5 guilds only, while every toll is still zero, 6 changes over
single segments and guilds over pairs of cities. Modes 1-6 keep tolls
between 0 and 10000 by undoing changes, with at most 40 pending at once.
Mode 7 alternates full raises and removals on two cities, querying each
state, for the most events. Mode 8 makes random overlapping changes on
31 cities, choosing deltas within the current toll bounds, for the most
events; optional n and m after the mode override those sizes. Arguments
are seed mode [n m], with the optional sizes supported only by mode 8."""

import random
import sys

MOST = 100000
TOLL = 10000
PENDING = 40
STEP = 100


def boundary_events(seed, mode):
    rng = random.Random(seed)
    n, m = (2, MOST) if mode == 7 else (31, MOST)
    if mode == 8 and len(sys.argv) > 3:
        n, m = map(int, sys.argv[3:5])
    tolls = [0] * (n - 1)
    events = []
    for j in range(m):
        if mode == 7:
            if j % 2:
                events.append("establish 1 2")
            else:
                d = TOLL if j % 4 == 0 else -TOLL
                events.append("change 1 2 %d" % d)
            continue
        a, b = sorted(rng.sample(range(1, n + 1), 2))
        if j == m - 1 or rng.random() < 0.45:
            events.append("establish %d %d" % (a, b))
        else:
            low = -min(tolls[a - 1 : b - 1])
            high = TOLL - max(tolls[a - 1 : b - 1])
            d = rng.choice((low, high, 0, rng.randint(low, high)))
            for i in range(a - 1, b - 1):
                tolls[i] += d
            events.append("change %d %d %d" % (a, b, d))
    sys.stdout.buffer.write(("%d %d\n%s\n" % (n, m, "\n".join(events))).encode("ascii"))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    if mode in (7, 8):
        boundary_events(seed, mode)
        return
    rng = random.Random(seed)
    n = rng.randint(2, 8) if mode == 1 else MOST
    m = rng.randint(1, 12) if mode == 1 else MOST
    events, pending = [], []
    if mode == 3:
        events.append("change 1 %d %d" % (n, TOLL))
    elif mode != 5:
        events.append("change 1 %d %d" % (n, TOLL // 2))

    def stretch():
        if mode == 6:
            a = rng.randint(1, n - 1)
            return a, a + 1
        if mode == 3:
            a = rng.randint(1, n // 10)
            return a, rng.randint(n - n // 10, n)
        a, b = sorted(rng.sample(range(1, n + 1), 2))
        return a, b

    while len(events) < m:
        change = mode in (1, 2, 4, 6) and rng.random() < (0.9 if mode == 4 else 0.5)
        if change and (pending and (len(pending) >= PENDING or rng.random() < 0.5)):
            a, b, d = pending.pop(rng.randrange(len(pending)))
            events.append("change %d %d %d" % (a, b, -d))
        elif change:
            a, b = stretch()
            d = rng.randint(-STEP, STEP)
            pending.append((a, b, d))
            events.append("change %d %d %d" % (a, b, d))
        else:
            events.append("establish %d %d" % stretch())
    print(n, len(events))
    print("\n".join(events))


main()
