import sys


RANK_GAP = 2
ROLES = (b"statements", b"testdata", b"anything")
WRITER, TESTER, _ = ROLES
RECURSION_MARGIN = 20


def writes_with(writer, tester):
    return writer != TESTER and tester != WRITER


def plan(groups, count):
    source, sink = 0, len(groups) + 1
    graph = [[] for _ in range(sink + 1)]
    targets, capacities = [], []

    def add(first, second, capacity):
        edge = len(targets)
        graph[first].append(edge)
        graph[second].append(edge ^ 1)
        targets.extend((second, first))
        capacities.extend((capacity, 0))

    ids = {group: index for index, group in enumerate(groups, 1)}
    records = [None, *groups.items()]
    left = []
    for group, node in ids.items():
        rank, role = group
        capacity = len(groups[group])
        if rank // RANK_GAP % 2:
            add(node, sink, capacity)
            continue
        left.append(node)
        add(source, node, capacity)
        # One edge carries every feasible pair between these two groups.
        for other_rank in (rank - RANK_GAP, rank + RANK_GAP):
            for other_role in ROLES:
                partner = ids.get((other_rank, other_role))
                if partner and (writes_with(role, other_role) or writes_with(other_role, role)):
                    add(node, partner, capacity)

    def send(node, amount):
        if node == sink:
            return amount
        edges = graph[node]
        while next_edge[node] < len(edges):
            edge = edges[next_edge[node]]
            other = targets[edge]
            if capacities[edge] and level[other] == level[node] + 1:
                sent = send(other, min(amount, capacities[edge]))
                if sent:
                    capacities[edge] -= sent
                    capacities[edge ^ 1] += sent
                    return sent
            next_edge[node] += 1
        return 0

    # The levels increase along a path, whose length is bounded by the node count.
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(graph) + RECURSION_MARGIN))
    total = 0
    while True:
        level = [-1] * len(graph)
        level[source] = 0
        queue = [source]
        for node in queue:
            for edge in graph[node]:
                other = targets[edge]
                if capacities[edge] and level[other] < 0:
                    level[other] = level[node] + 1
                    queue.append(other)
        if level[sink] < 0:
            break
        next_edge = [0] * len(graph)
        while sent := send(source, count):
            total += sent

    output = [str(total).encode()]
    for node in left:
        (_, role), names = records[node]
        for edge in graph[node]:
            other = targets[edge]
            if other == source:
                continue
            (_, other_role), other_names = records[other]
            for _ in range(capacities[edge ^ 1]):
                a, b = names.pop(), other_names.pop()
                if not writes_with(role, other_role):
                    a, b = b, a
                output.append(a + b" " + b)
    return b"\n".join(output) + b"\n"


def main():
    count, *tokens = sys.stdin.buffer.read().split()
    fields = iter(tokens)
    groups = {}
    for name, role, rank in zip(fields, fields, fields, strict=True):
        groups.setdefault((int(rank), role), []).append(name)
    sys.stdout.buffer.write(plan(groups, int(count)))


if __name__ == "__main__":
    main()
