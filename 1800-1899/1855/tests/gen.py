"""Events from a seed and a mode: mode 1 a few cities and events, 2 the
most cities and events at random, 3 every toll at its largest, then
guilds over long stretches, 4 the most events, almost all of them
changes, 5 guilds only, while every toll is still zero, 6 changes over
single segments and guilds over pairs of cities. Tolls always stay
between 0 and 10000: after one change of every toll to 5000, every
change is later undone, with at most 40 of them pending at once."""

import random
import sys

MOST = 100000
TOLL = 10000
PENDING = 40
STEP = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
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
