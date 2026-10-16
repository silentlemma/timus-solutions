"""One test from a seed and a mode: mode 1 a list of up to 5 people,
mode 2 a list of 100, mode 3 a list of 100 where several people share
the longest life, mode 4 lives that cross the days around the end of
February in years like 1900 and 2000."""

import datetime
import random
import sys

FEW = 5
MOST = 100
FIRST = datetime.date(1800, 1, 1)
LAST = datetime.date(2009, 12, 31)
CENTURY_YEARS = (1800, 1900, 2000)
TIES = 4


def fmt(day):
    return day.strftime("%d.%m.%Y")


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 1 else MOST
    span = (LAST - FIRST).days
    # the dates of becoming the oldest and of dying form one rising chain
    chain = sorted(rng.sample(range(span // 2, span + 1), n + 1))
    if mode == 4:
        marks = sorted({(datetime.date(y, 2, 27) - FIRST).days + rng.randint(0, 3)
                        for y in CENTURY_YEARS for _ in range(2)})
        chain = sorted(set(chain[:n + 1 - len(marks)]) | set(marks))
        while len(chain) < n + 1:
            extra = rng.randint(span // 2, span)
            if extra not in chain:
                chain = sorted(chain + [extra])
    used = set()
    rows = []
    longest = 0
    for i in range(n):
        start, death = chain[i], chain[i + 1]
        while True:
            if mode == 3 and longest and rng.randint(1, TIES) == 1 and death - longest >= 0:
                birth = death - longest
            else:
                birth = rng.randint(0, start - 1)
            if birth < start and birth not in used:
                break
        used.add(birth)
        longest = max(longest, death - birth)
        rows.append((birth, start, death))
    print(n)
    for row in rows:
        print(" ".join(fmt(FIRST + datetime.timedelta(days=d)) for d in row))


main()
