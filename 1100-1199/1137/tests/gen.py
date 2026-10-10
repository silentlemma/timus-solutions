"""Cyclic routes over connected stops with no segment used twice: a seed,
the number of routes, the stops per route, the number of stop ids and a
mode. Mode 0 draws random routes that join a stop already used, mode 1
makes every route a self-crossing loop through few stops, mode 2 chains
the routes in a long line through one shared stop each. Mode 3 makes n
routes of exactly m segments over a common pool of m stops, with random
labels and distinct modular steps. For mode 3, m must be even and at
least 4, idcount >= m, and n cannot exceed the number of integers from
1 to m - 2 coprime to m - 1."""

import math
import random
import sys

TRIES = 1000


def route(rng, m, ids, used, joint, taken):
    # a closed walk of m stops through joint whose segments are all new
    for _ in range(TRIES):
        stops = [joint]
        for _ in range(m - 1):
            stops.append(rng.choice(ids))
        stops.append(joint)
        segs = list(zip(stops, stops[1:]))
        if all(a != b for a, b in segs) and len(set(segs)) == m and not taken & set(segs):
            taken.update(segs)
            used.update(stops)
            return stops
    return None


def main():
    seed, n, m, idcount, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    ids = rng.sample(range(1, 1001), idcount)
    used, taken, routes = set(), set(), []
    if mode == 3:
        assert 4 <= m <= 200 and m % 2 == 0 and idcount >= m
        size = m - 1
        steps = [s for s in range(1, size) if math.gcd(s, size) == 1]
        assert 1 <= n <= min(100, len(steps))
        for step in rng.sample(steps, n):
            # Distinct steps give distinct internal edges. The hub edges
            # also differ: their other endpoints are 2*step and step.
            stops = [ids[size]]
            stops += [ids[((k + 2) * step) % size] for k in range(size)]
            routes.append(stops + [stops[0]])
    while len(routes) < n:
        if mode == 2 and routes:
            joint = routes[-1][rng.randrange(len(routes[-1]) - 1)]
        else:
            joint = rng.choice(sorted(used)) if used else rng.choice(ids)
        pool = ids if mode != 1 else rng.sample(ids, min(len(ids), 4)) + [joint]
        r = route(rng, rng.randint(2, m), pool, used, joint, taken)
        if r:
            routes.append(r)
    lines = [str(n)] + ["%d %s" % (len(r) - 1, " ".join(map(str, r))) for r in routes]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
