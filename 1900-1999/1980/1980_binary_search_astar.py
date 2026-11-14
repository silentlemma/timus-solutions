from heapq import heappop, heappush
from math import fsum
import sys

TOLERANCE = 1e-9
OUTPUT_GUARD = 1e-8
OUTPUT_DIGITS = 12
INFINITY = float("inf")


def solve(n, roads, deadline):
    target = n - 1
    graph = [[] for _ in range(n)]
    speeds, lengths = [], []
    for index, (a, b, speed, length) in enumerate(roads):
        graph[a].append((b, index))
        graph[b].append((a, index))
        speeds.append(speed)
        lengths.append(length)
    fastest, slowest = max(speeds), min(speeds)

    # The shortest physical distance gives a consistent A* heuristic
    # after dividing by the largest speed possible at this allowance.
    remaining = [INFINITY] * n
    physical_parent = [-1] * n
    remaining[target] = 0
    queue = [(0, target)]
    while queue:
        distance, vertex = heappop(queue)
        if distance != remaining[vertex]:
            continue
        for neighbor, index in graph[vertex]:
            candidate = distance + lengths[index]
            if candidate < remaining[neighbor]:
                remaining[neighbor] = candidate
                physical_parent[neighbor] = index
                heappush(queue, (candidate, neighbor))

    def physical_path():
        vertex = 0
        while vertex != target:
            index = physical_parent[vertex]
            yield index
            a, b, _, _ = roads[index]
            vertex = a ^ b ^ vertex

    def allowance_for(path, low, high):
        grouped = [0] * (fastest + 1)
        for index in path:
            grouped[speeds[index]] += lengths[index]
        parts = [(speed, length) for speed, length in enumerate(grouped) if length]

        def time(extra):
            return fsum(length / (speed + extra) for speed, length in parts)

        if time(0.0) <= deadline:
            return 0.0
        while high - low > TOLERANCE * max(1.0, high):
            middle = (low + high) / 2
            if time(middle) <= deadline:
                high = middle
            else:
                low = middle
        return high

    physical_speed = remaining[0] / deadline
    low = max(0.0, physical_speed - fastest)
    high = max(low, physical_speed - slowest)
    if fastest == slowest or (len(roads) == target and all(d < INFINITY for d in remaining)):
        path = list(physical_path())
        high = allowance_for(path, low, high)
        return high + OUTPUT_GUARD * max(1.0, high), [index + 1 for index in path]

    def route(extra, parent=None):
        inverse = [0.0] + [1.0 / (speed + extra) for speed in range(1, fastest + 1)]
        costs = [length * inverse[speed] for speed, length in zip(speeds, lengths)]
        fastest_inverse = inverse[fastest]
        estimate = [distance * fastest_inverse for distance in remaining]
        best = [INFINITY] * n
        best[0] = 0.0
        queue = [(estimate[0], -0.0, 0)]
        while queue:
            _, negative_time, vertex = heappop(queue)
            time = -negative_time
            if time != best[vertex]:
                continue
            if vertex == target:
                return True
            for neighbor, index in graph[vertex]:
                arrival = time + costs[index]
                if arrival < best[neighbor]:
                    bound = arrival + estimate[neighbor]
                    if bound <= deadline:
                        best[neighbor] = arrival
                        if parent is not None:
                            parent[neighbor] = index
                        heappush(queue, (bound, -arrival, neighbor))
        return False

    parent = [-1] * n
    if not route(0.0, parent):
        high = allowance_for(physical_path(), low, high)
        while high - low > TOLERANCE * max(1.0, high):
            middle = (low + high) / 2
            if route(middle):
                high = middle
            else:
                low = middle
        high += OUTPUT_GUARD * max(1.0, high)
        assert route(high, parent)
    else:
        high = OUTPUT_GUARD
    path = []
    vertex = target
    while vertex:
        index = parent[vertex]
        path.append(index + 1)
        a, b, _, _ = roads[index]
        vertex = a ^ b ^ vertex
    return high, path[::-1]


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(tokens), next(tokens)
    roads = [(next(tokens) - 1, next(tokens) - 1, next(tokens), next(tokens)) for _ in range(m)]
    allowance, path = solve(n, roads, next(tokens))
    print(f"{allowance:.{OUTPUT_DIGITS}f} {len(path)}")
    print(*path)


if __name__ == "__main__":
    main()
