from collections import deque
import sys
from array import array


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


INPUT_BUFFER = 4096


def numbers():
    # carry only an unfinished token across refills, even when a line is huge.
    pending = b""
    for chunk in iter(lambda: sys.stdin.buffer.read(INPUT_BUFFER), b""):
        data = pending + chunk
        tokens = data.split()
        pending = tokens.pop() if data[-1] > ord(" ") else b""
        for token in tokens:
            yield int(token)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    count, roads = next(values), next(values)
    # a destination is 2 * city + gear <= 19999, which fits an unsigned short.
    adjacency = [array("H") for _ in range(count)]
    for _ in range(roads):
        lower, upper = next(values), next(values)
        lower -= 1
        upper -= 1
        adjacency[lower].append(2 * upper)
        adjacency[upper].append(2 * lower + 1)
    start, target = next(values), next(values)
    start -= 1
    target -= 1
    print(minimum_changes(adjacency, start, target))


if __name__ == "__main__":
    main()
