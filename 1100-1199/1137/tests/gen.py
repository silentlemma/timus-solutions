"""Cyclic routes over connected stops with no segment used twice: a seed,
the number of routes, the stops per route, the number of stop ids and a
mode. Mode 0 draws random routes that join a stop already used, mode 1
makes every route a self-crossing loop through few stops, mode 2 chains
the routes in a long line through one shared stop each."""

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
