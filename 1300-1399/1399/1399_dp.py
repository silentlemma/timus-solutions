import sys
from array import array

ROUNDS = 300000  # large neighbourhood search rounds
SHARE = 50  # the first threshold is the first cost over this
MOST = 8  # at most this many random items removed at once

KINDS = 3  # removal kinds: random items, a whole trip, one client
UNREACHED = 0xFFFF  # no path yet in the subset table

# xorshift64 from a fixed seed: the same numbers in every language
SEED = 88172645463325252
SHIFTS = (13, 7, 17)
MASK = (1 << 64) - 1


class Random:
    def __init__(self):
        self.state = SEED

    def below(self, k):
        x = self.state
        x ^= (x << SHIFTS[0]) & MASK
        x ^= x >> SHIFTS[1]
        x ^= (x << SHIFTS[2]) & MASK
        self.state = x
        return x % k


def main():
    m, n, cap, *data = map(int, sys.stdin.read().split())
    pos = 0
    dist = []
    for _ in range(m + 1):
        dist.append(data[pos : pos + m + 1])
        pos += m + 1
    weight = data[pos : pos + 2 * n : 2]
    client = [c - 1 for c in data[pos + 1 : pos + 2 * n : 2]]
    # Held-Karp over the clients: shortest walks from the depot through every subset
    full = 1 << m
    path = array("H", [UNREACHED]) * (full * m)
    tour = [0] * full
    for j in range(m):
        path[(1 << j) * m + j] = dist[0][j + 1]
    # step[k]: the offset of client k joining a walk that ends there
    step = [(1 << k) * m + k for k in range(m)]
    for s in range(1, full):
        best = UNREACHED
        base = s * m
        # only the clients in s can end the walk, only the others can come next
        inside = [j for j in range(m) if s >> j & 1]
        outside = [k for k in range(m) if not s >> k & 1]
        for j in inside:
            here = path[base + j]
            row = dist[j + 1]
            if here + row[0] < best:
                best = here + row[0]
            for k in outside:
                at = base + step[k]
                v = here + row[k + 1]
                if v < path[at]:
                    path[at] = v
        tour[s] = best

    trip = [-1] * n
    load, clients, per_client = [], [], []
    cost = [0]

    def put(i, t):
        if t == len(load):
            load.append(0)
            clients.append(0)
            per_client.append([0] * m)
        cost[0] -= tour[clients[t]]
        trip[i] = t
        load[t] += weight[i]
        per_client[t][client[i]] += 1
        if per_client[t][client[i]] == 1:
            clients[t] |= 1 << client[i]
        cost[0] += tour[clients[t]]

    def take(i):
        t = trip[i]
        cost[0] -= tour[clients[t]]
        load[t] -= weight[i]
        per_client[t][client[i]] -= 1
        if per_client[t][client[i]] == 0:
            clients[t] &= ~(1 << client[i])
        cost[0] += tour[clients[t]]
        trip[i] = -1

    def insert_best(i):
        """The cheapest place for item i: an existing trip or a new one, the
        first trip that costs no more than a new one, so empty trips return."""
        fresh = best = len(load)
        bit = 1 << client[i]
        extra = tour[bit]
        for t in range(fresh):
            if load[t] + weight[i] > cap:
                continue
            d = tour[clients[t] | bit] - tour[clients[t]]
            if d < extra or (d == extra and best == fresh):
                extra, best = d, t
        put(i, best)

    # a first plan by cheapest insertion; then rounds of removing some items
    # and putting them back in the cheapest places, undone when the cost grows
    # by more than a threshold that falls to zero
    for i in range(n):
        insert_best(i)
    rng = Random()
    best_trip, best_cost, start = trip[:], cost[0], cost[0]
    for rnd in range(ROUNDS):
        before = cost[0]
        kind = rng.below(KINDS)
        count = 1 + rng.below(min(n, MOST))
        pick = rng.below(n)
        target = trip[pick] if kind == 1 else client[pick]
        if kind == 1:
            removed = [i for i in range(n) if trip[i] == target]
        elif kind == 2:
            removed = [i for i in range(n) if client[i] == target]
        else:
            removed = []
            for _ in range(count):
                i = rng.below(n)
                if i not in removed:
                    removed.append(i)
        old = [trip[i] for i in removed]
        for i in removed:
            take(i)
        for k in range(len(removed) - 1, 0, -1):
            r = rng.below(k + 1)
            removed[k], removed[r] = removed[r], removed[k]
            old[k], old[r] = old[r], old[k]
        for i in removed:
            insert_best(i)
        threshold = start * (ROUNDS - rnd) // ROUNDS // SHARE
        if cost[0] > before + threshold:
            for i in removed:
                take(i)
            for i, t in zip(removed, old):
                put(i, t)
        if cost[0] < best_cost:
            best_cost, best_trip = cost[0], trip[:]

    # rebuild the best plan and print its non-empty trips, each route
    # recovered from the subset table
    trips = max(best_trip) + 1
    load[:] = [0] * trips
    clients[:] = [0] * trips
    per_client[:] = [[0] * m for _ in range(trips)]
    cost[0] = 0
    for i in range(n):
        put(i, best_trip[i])
    used = [t for t in range(trips) if clients[t]]
    out = [str(len(used)), ""]
    total = 0
    for t in used:
        out.append(" ".join(str(i + 1) for i in range(n) if trip[i] == t))
        out.append(str(load[t]))
        s = clients[t]
        length = tour[s]
        last = next(
            j for j in range(m) if s >> j & 1 and path[s * m + j] + dist[j + 1][0] == length
        )
        route = []
        while s:
            route.append(last + 1)
            rest = s & ~(1 << last)
            prev = -1
            for j in range(m):
                if (
                    rest >> j & 1
                    and path[rest * m + j] + dist[j + 1][last + 1] == path[s * m + last]
                ):
                    prev = j
                    break
            s, last = rest, prev
        out.append(" ".join(map(str, [0] + route[::-1] + [0])))
        out.append(str(length))
        out.append("")
        total += length
    out.append(str(total))
    print("\n".join(out))


main()
