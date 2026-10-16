"""One test from a seed and a mode: mode 1 a few buses with any times,
mode 2 many buses built around a working plan, so the answer is YES,
mode 3 a plan with no spare minutes and one bus given a minute less,
mode 4 many buses with random times, dense or spread up to 10^8, mode 5
the largest plan moved to the largest times, mode 6 a maximum queue sharing
one tight window with a single urgent bus, mode 7 two maximum queues with
unit patience and alternating widely spaced arrivals, mode 8 independent
random rushes with tight deadlines and long idle gaps."""

import random
import sys

LIMIT = 100000
TOP = 10 ** 8
FEW = 6
LAG = 5
SLACK = 2


def planned(rng, total, gap, slack):
    """Buses on two sides with an entry minute for each that works."""
    sides = [[], []]
    minute = 0
    for _ in range(total):
        minute += rng.randint(1, gap)
        pick = rng.randint(0, 1)
        if len(sides[pick]) == LIMIT:
            pick = 1 - pick
        side = sides[pick]
        earliest = side[-1][0] if side else 1
        t = max(earliest, minute - rng.randint(0, LAG))
        side.append((t, minute - t + 1 + rng.randint(0, slack)))
    for side in sides:
        if not side:
            side.append((minute + 1, 1))
    return sides


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        sides = []
        for _ in range(2):
            ts = sorted(rng.randint(1, FEW * 2) for _ in range(rng.randint(1, FEW)))
            sides.append([(t, rng.randint(1, FEW)) for t in ts])
    elif mode == 2:
        sides = planned(rng, rng.randint(2, LIMIT), rng.randint(1, LAG), SLACK)
    elif mode == 3:
        # every minute from 1 on is used and no bus has a spare minute, so
        # a bus that loses one leaves too many buses before its new end
        sides = planned(rng, rng.randint(2, LIMIT), 1, 0)
        choices = [(s, k) for s in (0, 1) for k, bus in enumerate(sides[s]) if bus[1] > 1]
        if choices:
            s, k = rng.choice(choices)
            t, p = sides[s][k]
            sides[s][k] = (t, p - 1)
    elif mode == 4:
        sides = []
        span, wait = rng.choice([(2 * LIMIT, FEW), (2 * LIMIT, LIMIT), (TOP, TOP)])
        for _ in range(2):
            ts = sorted(rng.randint(1, span) for _ in range(LIMIT))
            sides.append([(t, rng.randint(1, wait)) for t in ts])
    elif mode == 6:
        sides = [[(1, LIMIT + 1)] * LIMIT, [(rng.randint(2, LIMIT - 1), 1)]]
    elif mode == 7:
        sides = [[(1 + 1000 * k + 500 * s, 1) for k in range(LIMIT)] for s in (0, 1)]
    elif mode == 8:
        sides = [[], []]
        for block in range(2000):
            counts = [rng.randint(2, FEW), rng.randint(2, FEW)]
            order = [s for s in (0, 1) for _ in range(counts[s])]
            rng.shuffle(order)
            minute = block * 1000 + 1
            previous = [minute, minute]
            for s in order:
                minute += rng.randint(1, 2)
                arrival = rng.randint(max(previous[s], minute - LAG), minute)
                sides[s].append((arrival, minute - arrival + 1 + rng.randint(0, SLACK)))
                previous[s] = arrival
    else:
        sides = planned(rng, 2 * LIMIT - 1, 1, SLACK)
        shift = TOP - max(t + p for side in sides for t, p in side)
        sides = [[(t + shift, p) for t, p in side] for side in sides]
    out = []
    for side in sides:
        out.append(str(len(side)))
        out.extend("%d %d" % bus for bus in side)
    print("\n".join(out))


main()
