import sys

FIELDS = 3
HEADER = 4
INFINITY = 10**10


def find(parent, v):
    while parent[v] >= 0:
        if parent[parent[v]] >= 0:
            parent[v] = parent[parent[v]]
        v = parent[v]
    return v


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[2:HEADER]
    count = n + m
    x = data[HEADER::FIELDS]
    y = data[HEADER + 1 :: FIELDS]
    amounts = data[HEADER + 2 :: FIELDS]
    target = min(sum(amounts[:n]), sum(amounts[n:]))
    parent = [-1] * count
    sweeps = []
    ys = sorted(set(y))
    ranks = {value: i + 1 for i, value in enumerate(ys)}
    span = len(ys)
    queries = [[] for _ in range(span + 1)]
    updates = [[] for _ in range(span + 1)]
    for rank in range(1, span + 1):
        k = rank
        while k:
            queries[rank].append(k)
            k -= k & -k
        k = rank
        while k <= span:
            updates[rank].append(k)
            k += k & -k
    for sx in (1, -1):
        for sy in (1, -1):
            order = sorted(range(count), key=lambda i: (sx * x[i], sy * y[i]))
            rank = [ranks[v] if sy == 1 else span + 1 - ranks[v] for v in y]
            values = [sx * a + sy * b for a, b in zip(x, y)]
            values.append(-INFINITY)
            sweeps.append((order, rank, values))

    edges = []
    components = count
    while components > 1:
        roots = [find(parent, i) for i in range(count)] + [-1]
        best = [INFINITY] * count
        ends = [None] * count
        for order, rank, values in sweeps:
            first = [[count] * (span + 1) for _ in range(2)]
            second = [[count] * (span + 1) for _ in range(2)]
            for i in order:
                color = i >= n
                r = roots[i]
                a, b = first[1 - color], second[1 - color]
                candidate = count
                threshold = values[i] - best[r]
                for k in queries[rank[i]]:
                    v = a[k]
                    if values[v] <= threshold:
                        continue
                    if roots[v] == r:
                        v = b[k]
                    if values[v] > threshold:
                        candidate = v
                        threshold = values[v]
                if candidate != count:
                    best[r] = values[i] - threshold
                    ends[r] = (i, candidate)
                a, b = first[color], second[color]
                value = values[i]
                # Keep two maxima belonging to different frozen components.
                for k in updates[rank[i]]:
                    v = a[k]
                    if value > values[v]:
                        if roots[v] != r:
                            b[k] = v
                        a[k] = i
                    elif roots[v] != r and value > values[b[k]]:
                        b[k] = i
        for r, edge in enumerate(ends):
            if edge is None:
                continue
            u, v = edge
            a, b = find(parent, u), find(parent, v)
            if a != b:
                if parent[a] > parent[b]:
                    a, b = b, a
                parent[a] += parent[b]
                parent[b] = a
                edges.append((best[r], u, v))
                components -= 1

    parent = [-1] * count
    people = amounts[:n] + [0] * m
    jobs = [0] * n + amounts[n:]
    score = 0
    for distance, u, v in sorted(edges):
        a, b = find(parent, u), find(parent, v)
        if parent[a] > parent[b]:
            a, b = b, a
        score -= min(people[a], jobs[a]) + min(people[b], jobs[b])
        parent[a] += parent[b]
        parent[b] = a
        people[a] += people[b]
        jobs[a] += jobs[b]
        score += min(people[a], jobs[a])
        if score == target:
            print(target, distance)
            return


if __name__ == "__main__":
    main()
