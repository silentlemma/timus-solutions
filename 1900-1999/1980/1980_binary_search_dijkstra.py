from heapq import heappop, heappush
import sys

SEARCH_STEPS = 60
SEARCH_TOLERANCE = 1e-9
SAFETY_MARGIN = 1e-8
OUTPUT_DIGITS = 12


def solve(n, edges, deadline):
    graph = [[] for _ in range(n)]
    total_length = 0
    for index, (a, b, speed, length) in enumerate(edges):
        graph[a].append((b, index))
        graph[b].append((a, index))
        total_length += length

    def shortest(extra):
        costs = [length / (speed + extra) for _, _, speed, length in edges]
        distance = [float("inf")] * n
        parent = [-1] * n
        distance[0] = 0.0
        queue = [(0.0, 0)]
        while queue:
            time, vertex = heappop(queue)
            if time != distance[vertex]:
                continue
            if vertex == n - 1:
                return True, parent
            for neighbor, index in graph[vertex]:
                candidate = time + costs[index]
                if candidate <= deadline and candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    parent[neighbor] = index
                    heappush(queue, (candidate, neighbor))
        return False, parent

    feasible, parent = shortest(0.0)
    low = high = 0.0
    if not feasible:
        high = total_length / deadline
        for _ in range(SEARCH_STEPS):
            if high - low <= SEARCH_TOLERANCE * max(1.0, high):
                break
            middle = (low + high) / 2
            if middle == low or middle == high:
                break
            feasible, _ = shortest(middle)
            if feasible:
                high = middle
            else:
                low = middle
        _, parent = shortest(high)
    extra = high + SAFETY_MARGIN * max(1.0, high)
    path = []
    vertex = n - 1
    while vertex:
        index = parent[vertex]
        path.append(index + 1)
        a, b, _, _ = edges[index]
        vertex = a ^ b ^ vertex
    path.reverse()
    return extra, path


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(tokens), next(tokens)
    edges = [(next(tokens) - 1, next(tokens) - 1, next(tokens), next(tokens)) for _ in range(m)]
    extra, path = solve(n, edges, next(tokens))
    print(f"{extra:.{OUTPUT_DIGITS}f} {len(path)}")
    print(*path)


if __name__ == "__main__":
    main()
