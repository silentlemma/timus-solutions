import sys

OUTPUT_BATCH = 1024


INPUT_BUFFER = 4096


def numbers():
    # carry only an unfinished token across refills, even when a line is huge.
    pending = b""
    for chunk in iter(lambda: sys.stdin.buffer.read(INPUT_BUFFER), b""):
        data = pending + chunk
        tokens = data.split()
        pending = tokens.pop() if data[-1] > ord(" ") else b""
        for token in tokens:
            yield int(token)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    n = next(values)
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, weight = next(values), next(values), next(values)
        edges[u].append((v, weight))
        edges[v].append((u, weight))
    parent, depth, distance = [-1] * n, [0] * n, [0] * n
    size, heavy, top = [1] * n, [-1] * n, [0] * n
    order = [0]
    for v in order:
        for u, weight in edges[v]:
            if u != parent[v]:
                parent[u] = v
                depth[u] = depth[v] + 1
                distance[u] = distance[v] + weight
                order.append(u)
    for v in reversed(order[1:]):
        p = parent[v]
        size[p] += size[v]
        if heavy[p] < 0 or size[v] > size[heavy[p]]:
            heavy[p] = v
    # each light-edge jump at least doubles the subtree size, limiting query work.
    for v in order[1:]:
        top[v] = top[parent[v]] if heavy[parent[v]] == v else v
    del edges, order, size, heavy
    output = []
    for _ in range(next(values)):
        a, b = next(values), next(values)
        answer = distance[a] + distance[b]
        while top[a] != top[b]:
            if depth[top[a]] < depth[top[b]]:
                a, b = b, a
            a = parent[top[a]]
        if depth[a] > depth[b]:
            a = b
        output.append(str(answer - 2 * distance[a]))
        # bounded output batches avoid retaining all 75000 answers.
        if len(output) == OUTPUT_BATCH:
            sys.stdout.write("\n".join(output) + "\n")
            output.clear()
    if output:
        sys.stdout.write("\n".join(output) + "\n")


main()
