"""One test from a seed and a mode: mode 1 a short random route, mode 2 the
longest route with the largest delays and flight times, mode 3 flights
bunched around midnight so that delays carry them into the next day,
mode 4 all 100 cities and ten distinct unsorted flights per airport,
mode 5 the longest possible trip with a 1439-minute wait at every connection."""

import random
import sys

DAY = 1440
MOST_CITIES = 100
MOST_FLIGHTS = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = MOST_CITIES if mode in (2, 4, 5) else rng.randint(2, 8)
    lines = [str(n)]
    for i in range(n - 1):
        q = MOST_FLIGHTS if mode == 4 else 1 if mode == 5 else rng.randint(1, MOST_FLIGHTS)
        if mode == 5:
            delay, flight = DAY - 1, DAY - 1
        elif mode == 2:
            delay, flight = rng.randint(DAY - 60, DAY - 1), rng.randint(DAY - 60, DAY - 1)
        else:
            delay, flight = rng.randint(0, DAY - 1), rng.randint(0, DAY - 1)
        if mode == 5:
            # The first arrival is 4317; each further leg takes 2878 minutes.
            times = [DAY - 1 - 2 * i]
        elif mode == 4:
            times = rng.sample(range(DAY), MOST_FLIGHTS)
        elif mode == 3:
            times = [(rng.choice([-1, 1]) * rng.randint(0, 90)) % DAY for _ in range(q)]
        else:
            times = [rng.randint(0, DAY - 1) for _ in range(q)]
        lines.append("%d %d %d" % (q, delay, flight))
        lines.append(" ".join("%02d:%02d" % divmod(t, 60) for t in times))
    print("\n".join(lines))


main()
