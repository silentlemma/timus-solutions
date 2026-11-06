from sys import stdin


def root(parents, vertex):
    while parents[vertex] != vertex:
        parents[vertex] = parents[parents[vertex]]
        vertex = parents[vertex]
    return vertex


def possible(size, road_count, target, tokens):
    if target == 0:
        return True
    components = list(range(size + 1))
    roads = [[] for _ in components]
    for _ in range(road_count):
        left, right, length = next(tokens), next(tokens), next(tokens)
        a, b = root(components, left), root(components, right)
        if a == b:
            return True
        components[a] = b
        roads[left].append((right, length))
        roads[right].append((left, length))

    parent = [-1] * (size + 1)
    weight = [0] * (size + 1)
    deepest = [0] * (size + 1)
    for city in range(1, size + 1):
        if parent[city] >= 0:
            continue
        parent[city] = 0
        order = [city]
        for vertex in order:
            for neighbor, length in roads[vertex]:
                if neighbor != parent[vertex]:
                    parent[neighbor] = vertex
                    weight[neighbor] = length
                    order.append(neighbor)
        for vertex in reversed(order):
            ancestor = parent[vertex]
            if ancestor:
                branch = deepest[vertex] + weight[vertex]
                # The best processed branch at the parent is from another child.
                if branch + deepest[ancestor] >= target:
                    return True
                deepest[ancestor] = max(deepest[ancestor], branch)
    return False


numbers = (int(token) for line in stdin.buffer for token in line.split())
cities, roads, target = next(numbers), next(numbers), next(numbers)
print("YES" if possible(cities, roads, target, numbers) else "NO")
