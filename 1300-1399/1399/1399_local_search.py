import sys
import time

ROUNDS = 300000  # large neighbourhood search rounds at most
BUDGET = 1.4  # seconds of processor time for the whole program
CHECK = 256  # rounds between looks at the clock
SHARE = 50  # the first threshold is the first cost over this
MOST = 8  # at most this many random items removed at once
KINDS = 3  # removal kinds: random items, a whole trip, one client
UNREACHED = 0xFFFF  # an edge that must not be used

# xorshift64 from a fixed seed: the same numbers in every language
SEED = 88172645463325252
SHIFTS = (13, 7, 17)
WORD_BITS = 32
WORD_MASK = (1 << WORD_BITS) - 1
MAX_ITEMS = 50

# the exact round through all clients: one-tree bounds, then branch and bound
TREE_SCALE = 128
TREE_ROUNDS = 120
TREE_PATIENCE = 15
INFINITY = 1 << 60
MAX_CACHE = 1 << 15
MAX_TREE_NODES = 10000

# rounds through a set of clients found by local search
KICKS = 80  # double-bridge restarts of the local search
TOUR_SEED = 2463534242


# At every distance level, each component needs enough truck visits for its load.
# Counting both ends of crossing edges gives a lower bound on the total distance.
def cut_bound(dist, weights, client, cap):
    size = len(dist)
    mass = [0] * size
    for w, c in zip(weights, client):
        mass[c + 1] += w
    edges = sorted((dist[i][j], i, j) for i in range(size) for j in range(i))
    parent = list(range(size))

    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v

    bound = at = 0
    for level in range(1, edges[-1][0] + 1):
        while at < len(edges) and edges[at][0] < level:
            _, i, j = edges[at]
            a, b = find(i), find(j)
            if a != b:
                parent[b] = a
                mass[a] += mass[b]
            at += 1
        root = find(0)
        outside = visits = 0
        for v in range(size):
            if parent[v] == v and v != root:
                outside += mass[v]
                visits += (mass[v] + cap - 1) // cap
        bound += visits + (outside + cap - 1) // cap
    return bound


class DenseTourNeeded(Exception):
    pass


def solve_tsp(dist, members):
    k = len(members)
    vertices = [0] + [j + 1 for j in members]
    d = [[dist[i][j] for j in vertices] for i in vertices]
    full = (1 << k) - 1
    bits = [1 << i for i in range(k)]
    index = {bit: i for i, bit in enumerate(bits)}
    order = [sorted(range(k), key=lambda j: (d[i][j + 1], j)) for i in range(k + 1)]
    route = []
    left = full
    last = 0
    while left:
        nxt = next(j for j in order[last] if left & bits[j])
        route.append(nxt)
        left ^= bits[nxt]
        last = nxt + 1
    best = sum(d[i][j] for i, j in zip([0] + [x + 1 for x in route],
                                      [x + 1 for x in route] + [0]))
    improving = True
    while improving:
        improving = False
        for i in range(k - 1):
            a = route[i - 1] + 1 if i else 0
            b = route[i] + 1
            for j in range(i + 1, k):
                c = route[j] + 1
                e = route[j + 1] + 1 if j + 1 < k else 0
                delta = d[a][c] + d[b][e] - d[a][b] - d[c][e]
                if delta < 0:
                    route[i:j + 1] = route[i:j + 1][::-1]
                    best += delta
                    improving = True
                    break
            if improving:
                break
    # Penalized minimum one-trees give lower bounds for every Hamiltonian cycle.
    best_route = route[:]
    scale = TREE_SCALE
    raw = d
    pi = [0] * (k + 1)
    best_pi = pi[:]
    best_bound = -INFINITY
    factor = 2
    stale = 0
    for _ in range(TREE_ROUNDS):
        adjusted = [[raw[i][j] * scale + pi[i] + pi[j] for j in range(k + 1)]
                    for i in range(k + 1)]
        degree = [0] * (k + 1)
        rest = list(range(2, k + 1))
        costs = adjusted[1][:]
        parent = [1] * (k + 1)
        value = 0
        while rest:
            at = min(rest, key=lambda j: costs[j])
            value += costs[at]
            degree[at] += 1
            degree[parent[at]] += 1
            rest.remove(at)
            row = adjusted[at]
            for j in rest:
                if row[j] < costs[j]:
                    costs[j] = row[j]
                    parent[j] = at
        a, b = sorted(range(1, k + 1), key=lambda j: adjusted[0][j])[:2]
        value += adjusted[0][a] + adjusted[0][b]
        degree[0] = 2
        degree[a] += 1
        degree[b] += 1
        bound = value - 2 * sum(pi)
        if bound > best_bound:
            best_bound, best_pi = bound, pi[:]
            stale = 0
        else:
            stale += 1
        norm = sum((x - 2) ** 2 for x in degree)
        if norm == 0 or best * scale - bound < scale:
            break
        if stale == TREE_PATIENCE:
            factor /= 2
            stale = 0
        step = factor * (best * scale - bound) / norm
        for i in range(1, k + 1):
            pi[i] += int(step * (degree[i] - 2))
    if best_bound > (best - 1) * scale:
        return best, [members[j] for j in best_route]
    pi = best_pi
    d = [[raw[i][j] * scale + pi[i] + pi[j] for j in range(k + 1)]
         for i in range(k + 1)]
    adjustment = 2 * sum(pi)
    best = best * scale + adjustment
    order = [sorted(range(k), key=lambda j: (d[i][j + 1], j)) for i in range(k + 1)]
    # Equivalent clients can be visited in their original order without changing the optimum.
    earlier_twins = [0] * k
    for j in range(k):
        for i in range(j):
            if all(raw[i + 1][v] == raw[j + 1][v]
                   for v in range(k + 1) if v != i + 1 and v != j + 1):
                earlier_twins[j] |= bits[i]
    nearest_order = [sorted(range(k), key=lambda j: d[i][j + 1])
                     for i in range(k + 1)]
    mst_cache = {0: 0}
    seen = {}
    nodes = 0

    def mst(s):
        value = mst_cache.get(s)
        if value is not None:
            return value
        rest = s & (s - 1)
        first = index[s ^ rest] + 1
        costs = d[first][:]
        value = 0
        while rest:
            scan = rest
            low = INFINITY
            at = 0
            while scan:
                bit = scan & -scan
                j = index[bit] + 1
                if costs[j] < low:
                    low, at = costs[j], j
                scan ^= bit
            value += low
            rest ^= bits[at - 1]
            scan = rest
            row = d[at]
            while scan:
                bit = scan & -scan
                j = index[bit] + 1
                if row[j] < costs[j]:
                    costs[j] = row[j]
                scan ^= bit
        if len(mst_cache) == MAX_CACHE:
            mst_cache.clear()
        mst_cache[s] = value
        return value

    stack = []

    def dfs(s, last, cost):
        nonlocal best, best_route, nodes
        nodes += 1
        if nodes > MAX_TREE_NODES:
            raise DenseTourNeeded
        if not s:
            value = cost + d[last][0]
            if value < best:
                best = value
                best_route = stack[:]
            return
        key = s * (k + 1) + last
        old = seen.get(key)
        if old is not None and old <= cost:
            return
        if len(seen) == MAX_CACHE:
            seen.clear()
        seen[key] = cost
        near = next(d[last][j + 1] for j in nearest_order[last] if s & bits[j])
        home = min(d[0][j + 1] for j in range(k) if s & bits[j])
        if cost + mst(s) + near + home >= best:
            return
        row = d[last]
        for j in order[last]:
            bit = bits[j]
            if s & bit and not s & earlier_twins[j]:
                stack.append(j)
                dfs(s ^ bit, j + 1, cost + row[j + 1])
                stack.pop()

    try:
        dfs(full, 0, 0)
    finally:
        dfs = None
    return (best - adjustment) // scale, [members[j] for j in best_route]


# Keep the same unsigned sequence using arithmetic that fits in signed machine words.
class Random:
    def __init__(self):
        self.low = SEED & WORD_MASK
        self.high = SEED >> WORD_BITS
        self.remainder = [(1 << WORD_BITS) % k for k in range(1, MAX_ITEMS + 1)]

    def below(self, k):
        low, high = self.low, self.high
        high = (high ^ (high << SHIFTS[0]) ^ (low >> (WORD_BITS - SHIFTS[0]))) & WORD_MASK
        low = (low ^ (low << SHIFTS[0])) & WORD_MASK
        low ^= ((high << (WORD_BITS - SHIFTS[1])) | (low >> SHIFTS[1])) & WORD_MASK
        high ^= high >> SHIFTS[1]
        high = (high ^ (high << SHIFTS[2]) ^ (low >> (WORD_BITS - SHIFTS[2]))) & WORD_MASK
        low = (low ^ (low << SHIFTS[2])) & WORD_MASK
        self.low, self.high = low, high
        return (high * self.remainder[k - 1] + low) % k


def direct_plan(dist, weights, client, cap):
    m = len(dist) - 1
    mass = [0] * m
    for w, c in zip(weights, client):
        mass[c] += w
    total = sum(weights)
    if total <= cap:
        if m == 1:
            return [[0]]
        _, route = solve_tsp(dist, list(range(m)))
        return [route]
    if m < 2 or total - min(mass) > cap:
        return None
    # Every proper client subset fits. Two depot copies encode two nonempty tours.
    # Shortcuts and merging reduce any feasible plan to such a pair without extra distance.
    extended = [row + [row[0]] for row in dist]
    extended.append(dist[0] + [0])
    extended[0][-1] = extended[-1][0] = UNREACHED
    _, route = solve_tsp(extended, list(range(m + 1)))
    at = route.index(m)
    return [route[:at], route[at + 1:]]


def write_plan(routes, dist, weights, client, original):
    out = [str(len(routes)), ""]
    total = 0
    for stops in routes:
        members = set(stops)
        items = [i for i, c in enumerate(client) if c in members]
        walk = [0] + [j + 1 for j in stops] + [0]
        length = sum(dist[i][j] for i, j in zip(walk, walk[1:]))
        out.extend([" ".join(str(i + 1) for i in items),
                    str(sum(weights[i] for i in items)),
                    " ".join(map(str, [0] + [original[j] + 1 for j in stops] + [0])),
                    str(length), ""])
        total += length
    out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


def improve(dist, route):
    """2-opt and moves of segments of up to three clients until neither helps;
    route starts and ends at the depot 0."""
    size = len(route)
    improved = True
    while improved:
        improved = False
        for i in range(1, size - 2):
            a, b = route[i - 1], route[i]
            for k in range(i + 1, size - 1):
                c, d = route[k], route[k + 1]
                if dist[a][c] + dist[b][d] < dist[a][b] + dist[c][d]:
                    route[i : k + 1] = route[i : k + 1][::-1]
                    improved = True
                    b = route[i]
        for length in (1, 2, 3):
            i = 1
            while i + length < size:
                a, first, last, b = route[i - 1], route[i], route[i + length - 1], route[i + length]
                gain = dist[a][first] + dist[last][b] - dist[a][b]
                best, at, flip = 0, -1, False
                for k in range(size - 1):
                    if i - 1 <= k < i + length:
                        continue
                    p, q = route[k], route[k + 1]
                    plain = dist[p][first] + dist[last][q] - dist[p][q]
                    turned = dist[p][last] + dist[first][q] - dist[p][q]
                    if gain - plain > best:
                        best, at, flip = gain - plain, k, False
                    if gain - turned > best:
                        best, at, flip = gain - turned, k, True
                if at >= 0:
                    segment = route[i : i + length]
                    if flip:
                        segment.reverse()
                    rest = route[:i] + route[i + length :]
                    at = at if at < i else at - length
                    route[:] = rest[: at + 1] + segment + rest[at + 1 :]
                    improved = True
                i += 1
    return sum(dist[route[k]][route[k + 1]] for k in range(size - 1))


def nearby_tour(dist, order, add):
    """A round through order (client numbers) with the client add inserted
    where it costs least, or add < 0 for none, then improved locally."""
    route = [0] + [j + 1 for j in order] + [0]
    if add >= 0:
        v = add + 1
        best, at = None, 1
        for k in range(1, len(route)):
            delta = dist[route[k - 1]][v] + dist[v][route[k]] - dist[route[k - 1]][route[k]]
            if best is None or delta < best:
                best, at = delta, k
        route.insert(at, v)
    total = improve(dist, route)
    return total, [v - 1 for v in route[1:-1]]


def local_tour(dist, members):
    """A short round from the depot through the members (client numbers,
    vertex j + 1): cheapest insertion, local search, then restarts from
    double-bridge kicks of the best round."""
    order = []
    for j in sorted(members, key=lambda j: -dist[0][j + 1]):
        v = j + 1
        best, at, prev = None, 0, 0
        for k in range(len(order) + 1):
            nxt = order[k] if k < len(order) else 0
            delta = dist[prev][v] + dist[v][nxt] - dist[prev][nxt]
            if best is None or delta < best:
                best, at = delta, k
            prev = nxt
        order.insert(at, v)
    route = [0] + order + [0]
    total = improve(dist, route)
    inner = len(route) - 2
    if inner >= 5:
        state = TOUR_SEED
        for _ in range(KICKS):
            cuts = []
            while len(cuts) < 3:
                state ^= (state << 13) & WORD_MASK
                state ^= state >> 17
                state ^= (state << 5) & WORD_MASK
                cut = 2 + state % (inner - 1)
                if cut not in cuts:
                    cuts.append(cut)
            p, q, r = sorted(cuts)
            trial = route[:p] + route[q:r] + route[p:q] + route[r:]
            value = improve(dist, trial)
            if value < total:
                total, route = value, trial
    return total, [v - 1 for v in route[1:-1]]


def main():
    m, n, cap, *data = map(int, sys.stdin.buffer.read().split())
    pos = 0
    dist = []
    for _ in range(m + 1):
        dist.append(data[pos : pos + m + 1])
        pos += m + 1
    weight = data[pos : pos + 2 * n : 2]
    client = [c - 1 for c in data[pos + 1 : pos + 2 * n : 2]]
    # Ignore clients without goods, retaining the original labels for output.
    original = sorted(set(client))
    remap = {c: j for j, c in enumerate(original)}
    client = [remap[c] for c in client]
    vertices = [0] + [c + 1 for c in original]
    dist = [[dist[i][j] for j in vertices] for i in vertices]
    m = len(original)
    try:
        routes = direct_plan(dist, weight, client, cap)
    except DenseTourNeeded:
        routes = None
    if routes is not None:
        write_plan(routes, dist, weight, client, original)
        return
    vertex_bits = [1 << j for j in range(m)]
    depot = dist[0][1:]

    # the round through a set of clients starts from the saved round of a set
    # one client away and is improved locally; every set is solved once
    tours = {0: 0}
    orders = {0: []}

    def tour_cost(s):
        value = tours.get(s)
        if value is not None:
            return value
        for j in range(m):
            near = orders.get(s ^ vertex_bits[j])
            if near is not None:
                if s >> j & 1:
                    value, order = nearby_tour(dist, near, j)
                else:
                    value, order = nearby_tour(dist, [c for c in near if c != j], -1)
                break
        else:
            value, order = local_tour(dist, [j for j in range(m) if s >> j & 1])
        tours[s] = value
        orders[s] = order
        return value

    trip = [-1] * n
    load = [0] * n
    clients = [0] * n
    trip_cost = [0] * n
    trip_items = [0] * n
    item_bits = [1 << i for i in range(n)]
    item_index = {bit: i for i, bit in enumerate(item_bits)}
    client_items = [0] * m
    client_groups = [[] for _ in range(m)]
    for i, c in enumerate(client):
        client_items[c] |= item_bits[i]
        client_groups[c].append(i)
    bits = [1 << c for c in client]
    cost = trips = 0

    def insert(i):
        # the trip whose round grows the least, or a new trip
        nonlocal cost, trips
        fresh = best = trips
        bit = bits[i]
        extra = tour_cost(bit)
        allowed = cap - weight[i]
        for t in range(fresh):
            if load[t] > allowed:
                continue
            delta = tour_cost(clients[t] | bit) - trip_cost[t]
            if delta < extra or (delta == extra and best == fresh):
                extra, best = delta, t
                if extra == 0:
                    break
        if best == trips:
            trips += 1
        trip[i] = best
        load[best] += weight[i]
        trip_items[best] |= item_bits[i]
        clients[best] |= bit
        cost += extra
        trip_cost[best] += extra

    def take_out(i):
        nonlocal cost
        t = trip[i]
        load[t] -= weight[i]
        trip_items[t] ^= item_bits[i]
        if not trip_items[t] & client_items[client[i]]:
            clients[t] ^= bits[i]
            value = tour_cost(clients[t])
            cost += value - trip_cost[t]
            trip_cost[t] = value
        trip[i] = -1

    # a first plan by cheapest insertion; then rounds of removing some items
    # and putting them back in the cheapest places, undone when the cost grows
    # by more than a threshold that falls to zero with the rounds or the time
    for i in range(n):
        insert(i)
    rng = Random()
    backup = [0] * n
    best_trip, best_cost, start = trip[:], cost, cost
    lower = 0
    client_mass = [0] * m
    for w, c in zip(weight, client):
        client_mass[c] += w
    for c in range(m):
        lower = max(lower, 2 * depot[c] * ((client_mass[c] + cap - 1) // cap))
    if trips == 1 or n == 1 or sum(sorted(weight)[:2]) > cap:
        lower = cost
    lower = max(lower, cut_bound(dist, weight, client, cap))
    rounds = 0 if cost == lower else ROUNDS
    began = time.process_time()
    left = 1.0
    for rnd in range(rounds):
        if rnd % CHECK == 0:
            spent = (time.process_time() - began) / (BUDGET - began)
            left = min(1.0 - rnd / ROUNDS, 1.0 - spent)
            if left <= 0:
                break
        before = cost
        kind = rng.below(KINDS)
        count = 1 + rng.below(min(n, MOST))
        pick = rng.below(n)
        target = trip[pick] if kind == 1 else client[pick]
        if kind == 1:
            removed = []
            chosen = trip_items[target]
            while chosen:
                bit = chosen & -chosen
                removed.append(item_index[bit])
                chosen ^= bit
        elif kind == 2:
            removed = client_groups[target][:]
        else:
            removed = []
            for _ in range(count):
                i = rng.below(n)
                if i not in removed:
                    removed.append(i)
        for i in removed:
            backup[i] = trip[i]
            take_out(i)
        for k in range(len(removed) - 1, 0, -1):
            r = rng.below(k + 1)
            removed[k], removed[r] = removed[r], removed[k]
        for i in removed:
            insert(i)
        threshold = int(start * left) // SHARE
        if cost > before + threshold:
            for i in removed:
                take_out(i)
            for i in removed:
                t = backup[i]
                if t == trips:
                    trips += 1
                trip[i] = t
                load[t] += weight[i]
                trip_items[t] |= item_bits[i]
                if not clients[t] & bits[i]:
                    clients[t] |= bits[i]
                    value = tour_cost(clients[t])
                    cost += value - trip_cost[t]
                    trip_cost[t] = value
        if cost < best_cost:
            best_cost, best_trip = cost, trip[:]
            if best_cost == lower:
                break

    # the best plan, its rounds polished by local search with restarts
    trips = max(best_trip) + 1
    load = [0] * trips
    clients = [0] * trips
    for i in range(n):
        t = best_trip[i]
        load[t] += weight[i]
        clients[t] |= bits[i]
    out = [str(sum(1 for s in clients if s)), ""]
    total = 0
    for t in range(trips):
        s = clients[t]
        if not s:
            continue
        length = tour_cost(s)
        order = orders[s]
        if s.bit_count() > 1:
            value, polished = local_tour(dist, [j for j in range(m) if s >> j & 1])
            if value < length:
                length, order = value, polished
        out.append(" ".join(str(i + 1) for i in range(n) if best_trip[i] == t))
        out.append(str(load[t]))
        out.append(" ".join(map(str, [0] + [original[j] + 1 for j in order] + [0])))
        out.append(str(length))
        out.append("")
        total += length
    out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
