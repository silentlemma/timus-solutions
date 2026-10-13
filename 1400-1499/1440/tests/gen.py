"""Training calendars: SEED MODE. Mode random chooses any valid match date
and bounds; mode feasible chooses a late match and an exact count obtained
from a seeded random nonempty weekday set. Both modes use seeded randomness.
"""

from datetime import date, timedelta
import random
import sys

DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
MONTHS = {9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def main():
    seed, mode = sys.argv[1:]
    rng = random.Random(int(seed))
    first = rng.randrange(7)
    if mode == 'random':
        match = date(2001, 9, 2) + timedelta(days=rng.randrange(114))
        lower = rng.randint(1, 200)
        upper = rng.randint(lower, 200)
    elif mode == 'feasible':
        match = date(2001, 11, 2) + timedelta(days=rng.randrange(53))
        chosen = rng.sample(range(7), rng.randint(2, 6))
        lower = sum((first + offset) % 7 in chosen
                    for offset in range(1, (match - date(2001, 9, 1)).days))
        upper = lower
    else:
        raise SystemExit('mode must be random or feasible')
    print(DAYS[first])
    print(MONTHS[match.month], match.day)
    print(lower, upper)


main()
