from array import array
import sys


def solve(size, edges, start, finish, origin):
    neighbors = [[] for _ in range(size)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    def bfs(source):
        distance = [-1] * size
        distance[source] = 0
        order = [source]
        for vertex in order:
            for following in neighbors[vertex]:
                if distance[following] < 0:
                    distance[following] = distance[vertex] + 1
                    order.append(following)
        return distance, order

    depth, order = bfs(start)
    clearance = bfs(origin)[0]
    best = [-1] * size
    best[start] = clearance[start]
    for vertex in order:
        for following in neighbors[vertex]:
            if depth[following] == depth[vertex] + 1:
                candidate = min(best[vertex], clearance[following])
                if candidate > best[following]:
                    best[following] = candidate
    return best[finish]


def main():
    read = sys.stdin.buffer.readline
    first = read()
    if not first:
        return
    size, count = map(int, first.split())
    endpoints = array("i")
    for _ in range(count):
        a, b = map(int, read().split())
        endpoints.extend((a - 1, b - 1))
    start, finish, origin = (int(word) - 1 for word in read().split())
    values = iter(endpoints)
    print(solve(size, zip(values, values), start, finish, origin))


if __name__ == "__main__":
    main()
