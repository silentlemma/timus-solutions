"""Events at a cemetery: a seed, N, M, the number of arrivals and of
visits. Days run from 0 to 7600 in order; each visit goes to a random
earlier client, and some visits come in bursts of five on one day, never
past 15000 events in all."""

import random
import sys

LAST = 7600
BURST = 5
TOTAL = 15000


def main():
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
