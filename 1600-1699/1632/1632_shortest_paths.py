import sys

FIELDS = 5  # X, Y, u, v, w
LIMIT = 10**6
TIGHT = 1e-7  # a smaller slack counts as an equality


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lasers = [[int(w) for w in data[1 + FIELDS * i : 1 + FIELDS * (i + 1)]] for i in range(n)]
    pos = 1 + FIELDS * n
    m = int(data[pos])
    # z[hi] - z[lo] must exceed lift: the gap of the beams where they cross
    edges = []
    out = [[] for _ in range(n)]
    for k in range(m):
        hi, lo = int(data[pos + 1 + 2 * k]) - 1, int(data[pos + 2 + 2 * k]) - 1
        xa, ya, ua, va, wa = lasers[hi]
        xb, yb, ub, vb, wb = lasers[lo]
        det = ua * vb - va * ub
        dx, dy = xb - xa, yb - ya
        lift = (wb * (va * dx - ua * dy) - wa * (dx * vb - dy * ub)) / det
        edges.append((lo, hi, lift))
        out[lo].append((hi, lift))
    # longest paths from an imaginary source tied to every laser by 0.
    # Only lasers raised in the last round can raise others.
    z = [0.0] * n
    active = list(range(n))
    for _ in range(n):
        raised = []
        for lo in active:
            base = z[lo]
            for hi, lift in out[lo]:
                if base + lift > z[hi]:
                    z[hi] = base + lift
                    raised.append(hi)
        if not raised:
            break
        active = list(set(raised))
    # equalities form an acyclic graph; a step per level of it makes them
    # strict, small enough to keep the other constraints and the bounds
    tight = [[] for _ in range(n)]
    indegree = [0] * n
    slack_min = None
    for lo, hi, lift in edges:
        slack = z[hi] - z[lo] - lift
        if slack < TIGHT:
            tight[lo].append(hi)
            indegree[hi] += 1
        elif slack_min is None or slack < slack_min:
            slack_min = slack
    level = [0] * n
    queue = [v for v in range(n) if indegree[v] == 0]
    for v in queue:
        for to in tight[v]:
            level[to] = max(level[to], level[v] + 1)
            indegree[to] -= 1
            if indegree[to] == 0:
                queue.append(to)
    levels = max(level)
    step = 0.0
    if levels:
        room = 2 * LIMIT - (max(z) - min(z))
        if slack_min is not None:
            room = min(room, slack_min)
        step = room / (2 * levels + 2)
    z = [z[v] + step * level[v] for v in range(n)]
    middle = (max(z) + min(z)) / 2
    sys.stdout.write("".join("%.10f\n" % (h - middle) for h in z))


main()
