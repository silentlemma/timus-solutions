"""Modes:

SEED N M ARRIVALS VISITS: random events on days 0 through 7600, with
visits to earlier clients and occasional same-day bursts of five visits,
never past 15000 events in all.
burst: 100 initial burials, 5000 visits to one client on day 1000, then
9900 arrivals on day 1001 in a single row of 100 graves.
"""

import random
import sys

LAST = 7600
BURST = 5
TOTAL = 15000


def main():
    if sys.argv[1:] == ["burst"]:
        events = ["0 d"] * 100 + ["1000 v 50"] * 5000 + ["1001 d"] * 9900
        sys.stdout.write("\n".join(["1 100"] + events) + "\n")
        return
    seed, n, m, arrivals, visits = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    kinds = ["d"] * arrivals + ["v"] * visits
    rng.shuffle(kinds)
    days = sorted(rng.randint(0, LAST) for _ in kinds)
    events, clients = [], 0
    room = TOTAL - len(kinds)
    for day, kind in zip(days, kinds):
        if kind == "v" and clients:
            extra = BURST - 1 if room >= BURST and rng.random() < 0.2 else 0
            room -= extra
            for _ in range(1 + extra):
                events.append("%d v %d" % (day, rng.randint(1, clients)))
        else:
            clients += 1
            events.append("%d d" % day)
    sys.stdout.write("\n".join(["%d %d" % (n, m)] + events) + "\n")


if __name__ == "__main__":
    main()
