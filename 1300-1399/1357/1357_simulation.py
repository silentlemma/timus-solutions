import sys
from collections import deque

SPECIFIC_HEAT = 4190  # J/(kg K)
PORTION_GRAMS = 200
COLD = 20  # degrees
BOILING = 100
POWER = 400  # W

# heating one portion takes C m dT / P seconds; with m in grams this is
# exactly the number of milliseconds, 167 600
PORTION_MS = SPECIFIC_HEAT * PORTION_GRAMS * (BOILING - COLD) // POWER
CAPACITY = 5  # portions in a full teakettle
MS = 1000
MINUTE = 60
HOUR = MINUTE * MINUTE
DAY = 24 * HOUR


def main():
    data = sys.stdin.read().split()
    n = int(data[0]) if data else 0
    wake = []
    for t in data[1 : n + 1]:
        h, m, s = map(int, t.split(":"))
        wake.append(((h * MINUTE + m) * MINUTE + s) * MS)
    ready = [0] * n
    kettle, waiting = [], deque()
    boil = 0  # the moment the water in the kettle boils, in milliseconds
    i = 0
    while i < n or kettle:
        # water that boils exactly when someone wakes up is poured out first
        if kettle and (i == n or wake[i] >= boil):
            for j in kettle:
                ready[j] = boil
            kettle = [waiting.popleft() for _ in range(min(CAPACITY, len(waiting)))]
            boil += PORTION_MS * len(kettle)
            continue
        if not kettle:
            kettle, boil = [i], wake[i] + PORTION_MS
        elif len(kettle) < CAPACITY:
            # the heat still missing grows by one portion's worth
            kettle.append(i)
            boil += PORTION_MS
        else:
            waiting.append(i)
        i += 1
    out = []
    for t in ready:
        sec = -(-t // MS) % DAY  # rounded up, past midnight from 00:00:00
        out.append("%02d:%02d:%02d" % (sec // HOUR, sec // MINUTE % MINUTE, sec % MINUTE))
    print("\n".join(out))


main()
