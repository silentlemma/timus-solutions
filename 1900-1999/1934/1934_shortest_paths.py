from array import array
from collections import deque
import math
import sys

PERCENT_SCALE = 100
PROBABILITY_DIGITS = 12
EDGE_LOG_COSTS = tuple(
    -math.log1p(-probability / PERCENT_SCALE) for probability in range(PERCENT_SCALE)
)


def safest_shortest_path(adjacency, start, target):
    count = len(adjacency)
    distance = array("i", [-1]) * count
    parent = array("i", [-1]) * count
    best_cost = array("d", [math.inf]) * count
    distance[start] = 0
    best_cost[start] = 0.0
    queue = deque([start])
    while queue:
        city = queue.popleft()
        if city == target:
            break
        next_distance = distance[city] + 1
        current_cost = best_cost[city]
        for edge in adjacency[city]:
            neighbor, probability = divmod(edge, PERCENT_SCALE)
            if distance[neighbor] < 0:
                distance[neighbor] = next_distance
                queue.append(neighbor)
            if distance[neighbor] == next_distance:
                candidate = current_cost + EDGE_LOG_COSTS[probability]
                if candidate < best_cost[neighbor]:
                    best_cost[neighbor] = candidate
                    parent[neighbor] = city
    path = []
    city = target
    while city >= 0:
        path.append(city)
        city = parent[city]
    path.reverse()
    return path, -math.expm1(-best_cost[target])


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    count, roads = next(values), next(values)
    start, target = next(values) - 1, next(values) - 1
    adjacency = [[] for _ in range(count)]
    for _ in range(roads):
        first, second, probability = next(values) - 1, next(values) - 1, next(values)
        adjacency[first].append(PERCENT_SCALE * second + probability)
        adjacency[second].append(PERCENT_SCALE * first + probability)
    del values
    path, probability = safest_shortest_path(adjacency, start, target)
    print(len(path), f"{probability:.{PROBABILITY_DIGITS}f}")
    print(" ".join(str(city + 1) for city in path))


if __name__ == "__main__":
    main()
