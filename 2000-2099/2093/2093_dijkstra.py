import heapq
import sys
from array import array

SNOW_SCALE = 100
MAX_MULTIPLIER = 100_500
SNOW_LIMIT = (MAX_MULTIPLIER - 1) * SNOW_SCALE
INFINITY = 10**18


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    head = array("i", [-1]) * n
    neighbor = array("i", [0]) * (2 * m)
    road = array("i", [0]) * (2 * m)
    following = array("i", [0]) * (2 * m)
    weight = array("i", [0]) * m
    for edge in range(m):
        left, right, weight[edge] = map(int, read().split())
        left -= 1
        right -= 1
        arc = 2 * edge
        neighbor[arc] = right
        road[arc] = edge
        following[arc] = head[left]
        head[left] = arc
        arc += 1
        neighbor[arc] = left
        road[arc] = edge
        following[arc] = head[right]
        head[right] = arc

    count = int(read())
    events = [tuple(map(int, read().split())) for _ in range(count)]
    events.sort()
    first = array("i", [0]) * (m + 1)
    starts = array("i", [0]) * count
    finishes = array("i", [0]) * count
    for index, (edge, start, finish) in enumerate(events):
        first[edge] += 1
        starts[index] = start
        finishes[index] = finish
    for edge in range(m):
        first[edge + 1] += first[edge]
    del events

    def arrival(edge, time):
        base = weight[edge]
        previous = 0
        # Only the first possible departure in each open gap can be optimal.
        for index in range(first[edge], first[edge + 1]):
            departure = max(time, previous)
            if departure < starts[index]:
                elapsed = min(departure - previous, SNOW_LIMIT)
                duration = base + (elapsed * base + SNOW_SCALE - 1) // SNOW_SCALE
                candidate = departure + duration
                if candidate <= starts[index]:
                    return candidate
            previous = finishes[index]
        departure = max(time, previous)
        elapsed = min(departure - previous, SNOW_LIMIT)
        duration = base + (elapsed * base + SNOW_SCALE - 1) // SNOW_SCALE
        return departure + duration

    distance = array("q", [INFINITY]) * n
    distance[0] = 0
    queue = [(0, 0)]
    while queue:
        time, vertex = heapq.heappop(queue)
        if time != distance[vertex]:
            continue
        if vertex == n - 1:
            print(time)
            return
        arc = head[vertex]
        while arc != -1:
            target = neighbor[arc]
            if distance[target] > time:
                candidate = arrival(road[arc], time)
                if candidate < distance[target]:
                    distance[target] = candidate
                    heapq.heappush(queue, (candidate, target))
            arc = following[arc]


if __name__ == "__main__":
    main()
