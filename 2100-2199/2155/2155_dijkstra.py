import heapq
import sys


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    height, width = int(next(tokens)), int(next(tokens))
    stride = width + 2
    size = (height + 2) * stride
    row, column = int(next(tokens)), int(next(tokens))
    start = row * stride + column
    row, column = int(next(tokens)), int(next(tokens))
    drone = row * stride + column

    cost = [0] * size
    for row in range(1, height + 1):
        base = row * stride + 1
        cost[base : base + width] = [int(next(tokens)) for _ in range(width)]
    successor = [0] * size
    offsets = {ord("U"): -stride, ord("D"): stride, ord("L"): -1, ord("R"): 1}
    for row in range(1, height + 1):
        for column, wind in enumerate(next(tokens), 1):
            cell = row * stride + column
            successor[cell] = cell + offsets[wind]

    infinity = sum(cost) + 1
    distance = [infinity] * size
    distance[start] = 0
    heap = [(0, start)]
    push, pop = heapq.heappush, heapq.heappop
    neighbors = (-stride, stride, -1, 1)
    while heap:
        time, cell = pop(heap)
        if time != distance[cell]:
            continue
        for offset in neighbors:
            target = cell + offset
            if cost[target] == 0:
                continue
            arrival = time + cost[target]
            if arrival < distance[target]:
                distance[target] = arrival
                push(heap, (arrival, target))

    first = [-1] * size
    path = []
    while cost[drone] and first[drone] == -1:
        first[drone] = len(path)
        path.append(drone)
        drone = successor[drone]
    cycle_start = first[drone] if cost[drone] else len(path)
    period = len(path) - cycle_start
    answer = infinity
    for time, cell in enumerate(path):
        arrival = distance[cell]
        catch_time = time
        if arrival > time:
            if time < cycle_start:
                continue
            # Wait for the first cycle visit at or after the shortest arrival.
            catch_time += ((arrival - time + period - 1) // period) * period
        answer = min(answer, catch_time)
    print(-1 if answer == infinity else answer)


if __name__ == "__main__":
    main()
