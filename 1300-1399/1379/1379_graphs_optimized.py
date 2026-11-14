import sys

DAY = 24 * 60
TRUCK = 3_000_000
CUP = 100
ORDER = 10_000_000
VERTEX_BITS = 9
TIME_BITS = 11
LOAD_SHIFT = VERTEX_BITS + TIME_BITS
VERTEX_MASK = (1 << VERTEX_BITS) - 1
TIME_MASK = (1 << TIME_BITS) - 1


def can_deliver(graph, load, destination):
    threshold = load << LOAD_SHIFT
    distance = [DAY + 1] * len(graph)
    distance[0] = 0
    buckets = [[] for _ in range(DAY + 1)]
    buckets[0].append(0)
    for minute, bucket in enumerate(buckets):
        for vertex in bucket:
            if distance[vertex] != minute:
                continue
            if vertex == destination:
                return True
            for edge in graph[vertex]:
                if edge < threshold:
                    break
                to = edge & VERTEX_MASK
                arrival = minute + ((edge >> VERTEX_BITS) & TIME_MASK)
                if arrival < distance[to]:
                    distance[to] = arrival
                    buckets[arrival].append(to)
    return False


def main():
    read = sys.stdin.buffer.readline
    vertices, roads = map(int, read().split())
    if vertices == 1:
        print(ORDER)
        return
    destination = vertices - 1
    graph = [[] for _ in range(vertices)]
    limits = set()
    for _ in range(roads):
        a, b, minutes, weight = map(int, read().split())
        load = (weight - TRUCK) // CUP
        if load <= 0:
            continue
        a -= 1
        b -= 1
        edge = (load << LOAD_SHIFT) | (minutes << VERTEX_BITS)
        graph[a].append(edge | b)
        graph[b].append(edge | a)
        limits.add(load)

    if not graph[0] or not graph[destination]:
        print(0)
        return
    for edges in graph:
        edges.sort(reverse=True)
    upper = min(graph[0][0], graph[destination][0]) >> LOAD_SHIFT
    choices = sorted(load for load in limits if load <= upper)
    left, right = 0, len(choices)
    while left < right:
        middle = (left + right) // 2
        if can_deliver(graph, choices[middle], destination):
            left = middle + 1
        else:
            right = middle
    print(choices[left - 1] if left else 0)


if __name__ == "__main__":
    main()
