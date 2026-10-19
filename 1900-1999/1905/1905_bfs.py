from array import array
from bisect import bisect_left
import sys

TIME_BASE = 1_000_001


def find_route(origins, destinations, start, target):
    keys = list(origins)
    keys.extend(destinations)
    keys.extend((start, target))
    keys.sort()
    unique = 0
    for key in keys:
        if unique == 0 or key != keys[unique - 1]:
            keys[unique] = key
            unique += 1
    del keys[unique:]
    head = array("i", [-1]) * unique
    arrival, following = array("i"), array("i")
    for flight in range(len(origins)):
        departure = bisect_left(keys, origins[flight])
        arrival.append(bisect_left(keys, destinations[flight]))
        following.append(head[departure])
        head[departure] = flight
    source, destination = bisect_left(keys, start), bisect_left(keys, target)
    previous = array("i", [-1]) * unique
    used_flight = array("i", [0]) * unique
    previous[source] = source
    queue = array("i", [source])
    cursor = 0
    while cursor < len(queue) and previous[destination] == -1:
        node = queue[cursor]
        cursor += 1
        neighbor = node + 1
        if neighbor < unique and keys[node] // TIME_BASE == keys[neighbor] // TIME_BASE:
            if previous[neighbor] == -1:
                previous[neighbor] = node
                queue.append(neighbor)
        flight = head[node]
        while flight != -1:
            neighbor = arrival[flight]
            if previous[neighbor] == -1:
                previous[neighbor] = node
                used_flight[neighbor] = flight + 1
                queue.append(neighbor)
            flight = following[flight]
    if previous[destination] == -1:
        return None
    route = []
    node = destination
    while node != source:
        if used_flight[node]:
            route.append(used_flight[node])
        node = previous[node]
    route.reverse()
    return route


def main():
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    _, count = next(tokens), next(tokens)
    origins, destinations = array("Q"), array("Q")
    for _ in range(count):
        departure, arrival, leave, enter = (
            next(tokens),
            next(tokens),
            next(tokens),
            next(tokens),
        )
        origins.append(departure * TIME_BASE + leave)
        destinations.append(arrival * TIME_BASE + enter)
    source, target, start, deadline = (
        next(tokens),
        next(tokens),
        next(tokens),
        next(tokens),
    )
    del tokens
    route = find_route(
        origins, destinations, source * TIME_BASE + start, target * TIME_BASE + deadline
    )
    if route is None:
        print("Impossible")
    else:
        print(len(route))
        print(" ".join(map(str, route)))


if __name__ == "__main__":
    main()
