from sys import implementation, stdin, stdout

# These short bounded scans trade JIT code-cache memory for interpreter work.
if implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("off")


def main():
    data = map(int, stdin.read().split())
    n, keep = next(data), next(data)
    graph = [[] for _ in range(n + 1)]
    total = 0
    for _ in range(n - 1):
        a, b, weight = next(data), next(data), next(data)
        graph[a].append((b, weight))
        graph[b].append((a, weight))
        total += weight
    del data
    if keep == n - 1:
        stdout.write(str(total))
        return
    weights, after = [], []

    def visit(vertex, parent, weight):
        position = len(weights)
        weights.append(weight)
        after.append(0)
        for child, edge in graph[vertex]:
            if child != parent:
                visit(child, vertex, edge)
        after[position] = len(weights)

    visit(1, 0, 0)
    removed = n - 1 - keep
    limit = min(keep, removed)
    stride = limit + 1
    minimize = removed < keep
    unreachable = total + 1 if minimize else -1
    best = [unreachable] * ((n + 1) * stride)
    for position in range(n + 1):
        best[position * stride] = 0
    prefix = [0]
    for weight in weights:
        prefix.append(prefix[-1] + weight)
    for position in range(n - 1, 0, -1):
        here, following, skipped = (
            position * stride,
            (position + 1) * stride,
            after[position] * stride,
        )
        size = after[position] - position
        cost = prefix[after[position]] - prefix[position]
        for amount in range(1, min(limit, n - position) + 1):
            if minimize:
                answer = best[following + amount]
                # Cutting this edge removes exactly its complete preorder interval.
                if amount >= size:
                    rest = best[skipped + amount - size]
                    if rest < unreachable and rest + cost < answer:
                        answer = rest + cost
            else:
                answer = best[skipped + amount]
                rest = best[following + amount - 1]
                if rest >= 0 and rest + weights[position] > answer:
                    answer = rest + weights[position]
            best[here + amount] = answer
    answer = best[stride + limit]
    stdout.write(str(total - answer if minimize else answer))


main()
