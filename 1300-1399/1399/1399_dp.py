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
WORD_BITS = 32
WORD_MASK = (1 << WORD_BITS) - 1
MAX_ITEMS = 50
SMALL_TOUR = 14
TREE_SCALE = 128
TREE_ROUNDS = 120
TREE_PATIENCE = 15
INFINITY = 1 << 60
MAX_CACHE = 1 << 15
MAX_TOUR_WORK = 3840
MAX_TREE_NODES = 10000


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


def solve_tsp(dist, members, warm=None, work=None):
    k = len(members)
    vertices = [0] + [j + 1 for j in members]
    d = [[dist[i][j] for j in vertices] for i in vertices]
    full = (1 << k) - 1
    bits = [1 << i for i in range(k)]
    index = {bit: i for i, bit in enumerate(bits)}
    order = [sorted(range(k), key=lambda j: (d[i][j + 1], j)) for i in range(k + 1)]
    if warm is not None and warm[1]:
        remap = {j: i for i, j in enumerate(members)}
        route = [remap[j] for j in warm[1] if j in remap]
        present = set(route)
        for j in range(k):
            if j in present:
                continue
            v = j + 1
            stops = [0] + [x + 1 for x in route] + [0]
            at = min(range(len(stops) - 1),
                     key=lambda i: d[stops[i]][v] + d[v][stops[i + 1]]
                     - d[stops[i]][stops[i + 1]])
            route.insert(at, j)
    else:
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
    pi = [0] + [warm[0][j] for j in members] if warm is not None else [0] * (k + 1)
    best_pi = pi[:]
    best_bound = -INFINITY
    factor = 2
    stale = 0
    iterations = 0
    for _ in range(TREE_ROUNDS):
        iterations += 1
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
    if warm is not None:
        for i, j in enumerate(members):
            warm[0][j] = best_pi[i + 1]
        warm[1] = [members[j] for j in best_route]
    if best_bound > (best - 1) * scale:
        if work is not None:
            work[0] += iterations
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
        return

    try:
        dfs(full, 0, 0)
    finally:
        dfs = None
    if warm is not None:
        warm[1] = [members[j] for j in best_route]
    if work is not None:
        work[0] += iterations + nodes
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


# Interchangeable clients leave only the number of visits to each group relevant.
# Mixed-radix states avoid solving the same path for every labelled subset.
class GroupedPaths:
    @staticmethod
    def create(dist):
        m = len(dist) - 1
        groups = []
        for v in range(m):
            for group in groups:
                u = group[0]
                if all(dist[u + 1][j] == dist[v + 1][j]
                       for j in range(m + 1) if j != u + 1 and j != v + 1):
                    group.append(v)
                    break
            else:
                groups.append([v])
        size = 1
        for group in groups:
            size *= len(group) + 1
        if size * len(groups) >= m * (1 << (m - 1)):
            return None
        return GroupedPaths(dist, groups, size)

    def __init__(self, dist, groups, size):
        m = len(dist) - 1
        self.width = width = len(groups)
        self.strides = strides = []
        self.masks = []
        self.which = [0] * m
        stride = 1
        for g, group in enumerate(groups):
            strides.append(stride)
            stride *= len(group) + 1
            self.masks.append(sum(1 << j for j in group))
            for j in group:
                self.which[j] = g
        self.groups = groups
        self.home = [dist[0][group[0] + 1] for group in groups]
        self.edge = [[dist[a[0] + 1][b[0] + 1] for b in groups] for a in groups]
        for g, group in enumerate(groups):
            if len(group) > 1:
                self.edge[g][g] = dist[group[0] + 1][group[1] + 1]
        self.values = array("H", [UNREACHED]) * (size * width)
        self.cycles = array("H", [UNREACHED]) * size
        self.cycles[0] = 0

    def ensure(self, state):
        if self.cycles[state] != UNREACHED:
            return
        width = self.width
        counts = [(state // self.strides[g]) % (len(self.groups[g]) + 1)
                  for g in range(width)]
        best = UNREACHED
        for last in range(width):
            if not counts[last]:
                continue
            rest = state - self.strides[last]
            self.ensure(rest)
            value = UNREACHED
            if not rest:
                value = self.home[last]
            else:
                base = rest * width
                for prev in range(width):
                    if counts[prev] > (prev == last):
                        candidate = self.values[base + prev] + self.edge[last][prev]
                        if candidate < value:
                            value = candidate
            self.values[state * width + last] = value
            best = min(best, value + self.home[last])
        self.cycles[state] = best

    def state(self, s):
        return sum((s & mask).bit_count() * stride
                   for mask, stride in zip(self.masks, self.strides))

    def cycle(self, s):
        state = self.state(s)
        self.ensure(state)
        return self.cycles[state]

    def path(self, s, last):
        state = self.state(s)
        self.ensure(state)
        return self.values[state * self.width + self.which[last]]


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
    full = 1 << m
    tour = array("H", [UNREACHED]) * full
    tour[0] = 0
    depot = dist[0][1:]
    into = [row[1:] for row in dist[1:]]
    grouped = GroupedPaths.create(dist)
    offsets = bytearray(full) if grouped is not None else array("I", [0]) * full
    paths = array("H", [0])
    vertex_bits = [1 << j for j in range(m)]

    half = 10
    low_members = [bytes(j for j in range(half) if s >> j & 1)
                   for s in range(1 << half)]
    high_members = [bytes(j + half for j in range(max(0, m - half)) if s >> j & 1)
                    for s in range(1 << max(0, m - half))]
    low_mask = (1 << half) - 1

    # Evaluate only missing submasks, with predecessors before their supersets.
    def ensure(s):
        if grouped is not None:
            offsets[s] = 1
            tour[s] = grouped.cycle(s)
            return 1
        if offsets[s]:
            return offsets[s]
        pending = []
        sub = s
        while sub:
            if not offsets[sub]:
                pending.append(sub)
            sub = (sub - 1) & s
        for sub in reversed(pending):
            inside = low_members[sub & low_mask] + high_members[sub >> half]
            at = len(paths)
            offsets[sub] = at
            best = UNREACHED
            for last in inside:
                rest = sub ^ vertex_bits[last]
                if not rest:
                    value = depot[last]
                else:
                    offset = offsets[rest]
                    row = into[last]
                    value = UNREACHED
                    for prev in inside:
                        if prev == last:
                            continue
                        candidate = paths[offset] + row[prev]
                        if candidate < value:
                            value = candidate
                        offset += 1
                paths.append(value)
                if value + depot[last] < best:
                    best = value + depot[last]
            tour[sub] = best
        return offsets[s]

    def path_cost(s, last):
        if grouped is not None:
            return grouped.path(s, last)
        return paths[ensure(s) + (s & (vertex_bits[last] - 1)).bit_count()]

    # Many overlapping large requests are cheaper in one compact Held-Karp pass.
    def fill_all():
        nonlocal paths, offsets
        offsets = array("I", [0]) * full
        size = 1
        for sub in range(1, full):
            offsets[sub] = size
            size += sub.bit_count()
        paths = array("H", [0]) * size
        for sub in range(1, full):
            inside = low_members[sub & low_mask] + high_members[sub >> half]
            at = offsets[sub]
            best = UNREACHED
            for last in inside:
                rest = sub ^ vertex_bits[last]
                if not rest:
                    value = depot[last]
                else:
                    offset = offsets[rest]
                    row = into[last]
                    value = UNREACHED
                    for prev in inside:
                        if prev == last:
                            continue
                        candidate = paths[offset] + row[prev]
                        if candidate < value:
                            value = candidate
                        offset += 1
                paths[at] = value
                candidate = value + depot[last]
                if candidate < best:
                    best = candidate
                at += 1
            tour[sub] = best

    saved_routes = {}
    warm = [[0] * m, []]

    large_work = [0]
    total_mass = sum(weight)
    use_work_budget = total_mass - min(weight) <= cap < total_mass

    def tour_cost(s):
        value = tour[s]
        if value != UNREACHED:
            return value
        if grouped is not None:
            ensure(s)
            return tour[s]
        if s.bit_count() > SMALL_TOUR and large_work[0] < MAX_TOUR_WORK:
            try:
                value, route = solve_tsp(dist, [j for j in range(m) if s >> j & 1],
                                     warm=warm, work=large_work if use_work_budget else None)
                if not use_work_budget:
                    large_work[0] += TREE_ROUNDS
            except DenseTourNeeded:
                large_work[0] = MAX_TOUR_WORK
                fill_all()
                return tour[s]
            saved_routes[s] = route
            tour[s] = value
            return value
        if large_work[0] >= MAX_TOUR_WORK:
            fill_all()
        else:
            ensure(s)
        return tour[s]

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
    for j in range(m):
        ensure(1 << j)
    cost = trips = 0


    # a first plan by cheapest insertion; then rounds of removing some items
    # and putting them back in the cheapest places, undone when the cost grows
    # by more than a threshold that falls to zero
    if sum(weight) <= cap:
        trip[:] = [0] * n
        load[0] = sum(weight)
        clients[0] = full - 1
        trip_items[0] = (1 << n) - 1
        cost = trip_cost[0] = tour_cost(full - 1)
        trips = 1
    else:
        for i in range(n):
            fresh = best = trips
            bit = bits[i]
            extra = tour[bit]
            allowed = cap - weight[i]
            for t in range(fresh):
                if load[t] > allowed:
                    continue
                subset = clients[t] | bit
                value = tour[subset]
                if value == UNREACHED:
                    value = tour_cost(subset)
                delta = value - trip_cost[t]
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
    rng = Random()
    backup = [0] * n
    best_trip, best_cost, start = trip[:], cost, cost
    lower = 0
    client_mass = [0] * m
    for w, c in zip(weight, client):
        client_mass[c] += w
    for c in range(m):
        lower = max(lower, 2 * depot[c] * ((client_mass[c] + cap - 1) // cap))
    if trips == 1:
        lower = cost
    if n == 1 or sum(sorted(weight)[:2]) > cap:
        lower = cost
    lower = max(lower, cut_bound(dist, weight, client, cap))
    rounds = 0 if cost == lower else ROUNDS
    for rnd in range(rounds):
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
            t = trip[i]
            backup[i] = t
            load[t] -= weight[i]
            trip_items[t] ^= item_bits[i]
            if not trip_items[t] & client_items[client[i]]:
                clients[t] ^= bits[i]
                value = tour[clients[t]]
                if value == UNREACHED:
                    value = tour_cost(clients[t])
                cost += value - trip_cost[t]
                trip_cost[t] = value
            trip[i] = -1
        for k in range(len(removed) - 1, 0, -1):
            r = rng.below(k + 1)
            removed[k], removed[r] = removed[r], removed[k]
        for i in removed:
            fresh = best = trips
            bit = bits[i]
            extra = tour[bit]
            allowed = cap - weight[i]
            for t in range(fresh):
                if load[t] > allowed:
                    continue
                subset = clients[t] | bit
                value = tour[subset]
                if value == UNREACHED:
                    value = tour_cost(subset)
                delta = value - trip_cost[t]
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
        threshold = start * (ROUNDS - rnd) // ROUNDS // SHARE
        if cost > before + threshold:
            for i in removed:
                t = trip[i]
                load[t] -= weight[i]
                trip_items[t] ^= item_bits[i]
                if not trip_items[t] & client_items[client[i]]:
                    clients[t] ^= bits[i]
                    value = tour[clients[t]]
                    if value == UNREACHED:
                        value = tour_cost(clients[t])
                    cost += value - trip_cost[t]
                    trip_cost[t] = value
                trip[i] = -1
            for i in removed:
                t = backup[i]
                if t == trips:
                    trips += 1
                trip[i] = t
                load[t] += weight[i]
                trip_items[t] |= item_bits[i]
                if not clients[t] & bits[i]:
                    clients[t] |= bits[i]
                    value = tour[clients[t]]
                    if value == UNREACHED:
                        value = tour_cost(clients[t])
                    cost += value - trip_cost[t]
                    trip_cost[t] = value
        if cost < best_cost:
            best_cost, best_trip = cost, trip[:]
            if best_cost == lower:
                break

    # Rebuild the best plan, retaining routes already found by branch and bound.
    trips = max(best_trip) + 1
    load = [0] * trips
    clients = [0] * trips
    trip = best_trip
    for i in range(n):
        t = trip[i]
        load[t] += weight[i]
        clients[t] |= bits[i]
    used = [t for t in range(trips) if clients[t]]
    out = [str(len(used)), ""]
    total = 0
    for t in used:
        out.append(" ".join(str(i + 1) for i in range(n) if trip[i] == t))
        out.append(str(load[t]))
        s = clients[t]
        length = tour_cost(s)
        if not offsets[s]:
            route = [original[j] + 1 for j in saved_routes[s]][::-1]
        else:
            last = next(
                j for j in range(m) if s >> j & 1 and path_cost(s, j) + dist[j + 1][0] == length
            )
            route = []
            while s:
                route.append(original[last] + 1)
                rest = s & ~(1 << last)
                prev = -1
                for j in range(m):
                    if (
                        rest >> j & 1
                        and path_cost(rest, j) + dist[j + 1][last + 1] == path_cost(s, last)
                    ):
                        prev = j
                        break
                s, last = rest, prev

        out.append(" ".join(map(str, [0] + route[::-1] + [0])))
        out.append(str(length))
        out.append("")
        total += length
    out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
