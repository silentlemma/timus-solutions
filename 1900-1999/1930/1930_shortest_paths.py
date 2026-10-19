from collections import deque
import sys


def minimum_changes(adjacency, start, target):
    state_count = 2 * len(adjacency)
    distance = [state_count] * state_count
    settled = bytearray(state_count)
    first = 2 * start
    distance[first] = distance[first + 1] = 0
    queue = deque((first, first + 1))
    while queue:
        state = queue.popleft()
        if settled[state]:
            continue
        settled[state] = 1
        city, gear = state // 2, state & 1
        if city == target:
            return distance[state]
        for next_state in adjacency[city]:
            cost = (next_state & 1) != gear
            candidate = distance[state] + cost
            if candidate < distance[next_state]:
                distance[next_state] = candidate
                if cost:
                    queue.append(next_state)
                else:
                    queue.appendleft(next_state)
    return -1


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    count, roads = next(values), next(values)
    adjacency = [[] for _ in range(count)]
    for _ in range(roads):
        lower, upper = next(values) - 1, next(values) - 1
        adjacency[lower].append(2 * upper)
        adjacency[upper].append(2 * lower + 1)
    start, target = next(values) - 1, next(values) - 1
    print(minimum_changes(adjacency, start, target))


if __name__ == "__main__":
    main()
