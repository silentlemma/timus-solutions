from array import array
from collections import deque
from sys import stdin

MAX_ROUTE = 2000


def main():
    values = iter(map(int, stdin.buffer.read().split()))
    count = next(values)
    first = array("H", [0]) * (MAX_ROUTE + 1)
    following = array("H", [0]) * (count + 1)
    back = array("H", [0]) * (count + 1)
    front = array("H", [0]) * (count + 1)
    for bus in range(1, count + 1):
        route = next(values)
        front[bus], back[bus] = route, next(values)
        following[bus], first[route] = first[route], bus
    target, left, right = next(values), next(values), next(values)
    previous = array("h", [-1]) * (MAX_ROUTE + 1)
    previous[left] = previous[right] = 0
    queue = deque((left, right) if left != right else (left,))
    # The front route stays available after a swap, and the back route is new.
    while queue and previous[target] < 0:
        route = queue.popleft()
        bus = first[route]
        while bus:
            destination = back[bus]
            if previous[destination] < 0:
                previous[destination] = bus
                queue.append(destination)
            bus = following[bus]
    if previous[target] < 0:
        print("IMPOSSIBLE")
        return
    path = []
    while bus := previous[target]:
        path.append(str(bus))
        target = front[bus]
    print(len(path))
    print("\n".join(reversed(path)))


if __name__ == "__main__":
    main()
