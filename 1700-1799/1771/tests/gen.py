"""One test from a seed and a mode: random routes over a few stops, with
the buses Leonid wrote down packed into a few minutes so that buses meet
often; mode 1 up to 6 stops and routes, mode 2 up to 12, mode 3 100
stops and routes with up to 100 buses. Lists in which nobody could have
chosen Leonid's bus, against the statement, are drawn again."""

import random
import sys

SIZES = {1: 6, 2: 12, 3: 100}
SPREAD = {1: 6, 2: 10, 3: 40}
SHORT = 6
FEW_BUSES = 8
MOST_BUSES = 100
HOUR = 60
FIRST_HOUR = 7


def stamp(minute):
    return "%02d:%02d" % (FIRST_HOUR + minute // HOUR, minute % HOUR)


def possible(routes, records):
    """Whether someone getting on at stop 1 and someone already inside can
    both have chosen the last bus, as the statement promises."""
    place = [{s: i for i, s in enumerate(r)} for r in routes]
    buses = [(t - place[r][1], r) for t, r in records]
    start, chosen = buses[-1]
    here = place[chosen]

    def picked(src, dst):
        mine = (start + here[src], start + here[dst], chosen)
        for b, r in buses:
            there = place[r]
            if src in there and dst in there and there[src] < there[dst]:
                if (b + there[src], b + there[dst], r) < mine:
                    return False
        return True

    stops = routes[chosen]
    one = here[1]
    after = stops[one + 1:]
    return (any(picked(1, d) for d in after)
            and any(picked(s, d) for s in stops[:one] for d in after))


def attempt(rng, mode):
    top = SIZES[mode]
    n, m = rng.randint(3, top), rng.randint(3, top)
    routes = []
    for _ in range(m):
        length = rng.randint(2, min(n, SHORT if mode < 3 else n))
        routes.append(rng.sample(range(1, n + 1), length))
    # one route must pass stop 1, not first, and then stop 2
    rest = list(range(3, n + 1))
    rng.shuffle(rest)
    head = rest[:rng.randint(1, len(rest))]
    mid = rest[len(head):len(head) + rng.randint(0, len(rest) - len(head))]
    tail = rest[len(head) + len(mid):]
    chosen = rng.randrange(m)
    routes[chosen] = head + [1] + mid + [2] + tail[:rng.randint(0, len(tail))]
    through = [r for r in range(m) if 1 in routes[r]]
    k = rng.randint(1, MOST_BUSES if mode == 3 else FEW_BUSES)
    last = routes[chosen].index(1) + rng.randint(0, SPREAD[mode])
    used = {(chosen, last - routes[chosen].index(1))}
    records = []
    for _ in range(k - 1):
        r = rng.choice(through)
        early = routes[r].index(1)
        if early > last:
            continue
        t = rng.randint(early, last)
        if (r, t - early) not in used:
            used.add((r, t - early))
            records.append((t, r))
    records.sort()
    records.append((last, chosen))
    return n, routes, records


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        n, routes, records = attempt(rng, mode)
        if possible(routes, records):
            break
    print(n, len(routes))
    for r in routes:
        print(" ".join(map(str, r + [-1])))
    print(len(records))
    for t, r in records:
        print(stamp(t), r + 1)


main()
