def partition(n, edges):
    total = 2 * n
    neighbors = [[] for _ in range(total)]
    for a, b in edges:
        neighbors[a - 1].append(b - 1)
        neighbors[b - 1].append(a - 1)

    color = [-1] * total
    components = []
    reach = [1]
    for root in range(total):
        if color[root] >= 0:
            continue
        color[root] = 0
        sides = ([root], [])
        queue = [root]
        for v in queue:
            opposite = 1 - color[v]
            for u in neighbors[v]:
                if color[u] == -1:
                    color[u] = opposite
                    sides[opposite].append(u)
                    queue.append(u)
                elif color[u] != opposite:
                    return None
        a, b = map(len, sides)
        reach.append((reach[-1] << a) | (reach[-1] << b))
        components.append(sides)

    if not (reach[-1] >> n) & 1:
        return None
    first = []
    remaining = n
    for i in range(len(components) - 1, -1, -1):
        a, b = components[i]
        if remaining >= len(a) and (reach[i] >> (remaining - len(a))) & 1:
            chosen = a
        else:
            chosen = b
        first.extend(chosen)
        remaining -= len(chosen)
    return first


def main():
    numbers = map(int, open(0, "rb").read().split())
    n, m = next(numbers), next(numbers)
    first = partition(n, ((next(numbers), next(numbers)) for _ in range(m)))
    if first is None:
        print("IMPOSSIBLE")
    else:
        selected = set(first)
        print(*(v + 1 for v in sorted(first)))
        print(*(v + 1 for v in range(2 * n) if v not in selected))


main()
