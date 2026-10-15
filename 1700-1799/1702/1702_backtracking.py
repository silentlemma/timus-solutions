import sys
from functools import lru_cache

FLOWS = 12
MINUTES = 10
# the flows each flow crosses or merges with, read off the crossing: 1-3
# come from the south, 4-6 from the east, 7-9 from the north and 10-12 from
# the west, each turning right, going straight on and turning left
CROSSES = {1: (9, 11), 2: (4, 5, 6, 9, 11, 12), 3: (5, 6, 7, 8, 11, 12),
           4: (2, 12), 5: (2, 3, 7, 8, 9, 12), 6: (2, 3, 8, 9, 10, 11),
           7: (3, 5), 8: (3, 5, 6, 10, 11, 12), 9: (1, 2, 5, 6, 11, 12),
           10: (6, 8), 11: (1, 2, 3, 6, 8, 9), 12: (2, 3, 4, 5, 8, 9)}


def main():
    data = [int(w) for w in sys.stdin.read().split()]
    cars, speed = data[:FLOWS], data[FLOWS:2 * FLOWS]
    conflict = [0] * FLOWS
    for flow, others in CROSSES.items():
        for other in others:
            conflict[flow - 1] |= 1 << (other - 1)
    # a minute lets through a set of flows that cross nowhere; it never hurts
    # to open more, so only the maximal such sets matter
    sets = []
    for mask in range(1, 1 << FLOWS):
        flows = [i for i in range(FLOWS) if mask >> i & 1]
        if any(conflict[i] & mask for i in flows):
            continue
        if all(conflict[i] & mask for i in range(FLOWS) if not mask >> i & 1):
            sets.append(flows)
    widest = max(len(s) for s in sets)

    @lru_cache(maxsize=None)
    def fits(need, minutes):
        """Whether minutes green phases can serve every flow its need."""
        if max(need) > minutes or sum(need) > widest * minutes:
            return False
        if not any(need):
            return True
        # some minute must open the flow that still needs the most
        top = need.index(max(need))
        for flows in sets:
            if top in flows:
                rest = list(need)
                for i in flows:
                    rest[i] = max(rest[i] - 1, 0)
                if fits(tuple(rest), minutes - 1):
                    return True
        return False

    def can_leave(limit):
        need = tuple(max(0, -(-(n - limit) // v)) for n, v in zip(cars, speed))
        return fits(need, MINUTES)

    lo, hi = 0, max(cars)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_leave(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)


main()
