import heapq
import sys

INFINITY = 10**9
DOT = ord(".")
PADDING = 2


def bfs(cells, offsets, start):
    distance = [-1] * len(cells)
    parent = [-1] * len(cells)
    distance[start] = 0
    order = [start]
    for vertex in order:
        for offset in offsets:
            other = vertex + offset
            if cells[other] == DOT and distance[other] < 0:
                distance[other] = distance[vertex] + 1
                parent[other] = vertex
                order.append(other)
    return distance, parent, order


def solve(grid, start_row, start_col, target_row, target_col):
    rows, cols = len(grid), len(grid[0])
    stride = cols + PADDING
    cells = bytearray((rows + PADDING) * stride)
    for row, content in enumerate(grid):
        at = (row + 1) * stride + 1
        cells[at : at + cols] = content
    start = (start_row + 1) * stride + start_col + 1
    target = (target_row + 1) * stride + target_col + 1
    offsets = (-stride, 1, stride, -1)
    ds, parent, order = bfs(cells, offsets, start)
    if ds[target] == 1:
        vertex = next(v for v, ch in enumerate(cells) if ch == DOT and v not in (start, target))
        return vertex // stride - 1, vertex % stride - 1
    dt, unused_parent, unused_order = bfs(cells, offsets, target)
    del unused_parent, unused_order
    path = []
    vertex = target
    while vertex != -1:
        path.append(vertex)
        vertex = parent[vertex]
    path.reverse()
    length = len(path) - 1
    position = [-1] * len(cells)
    for at, vertex in enumerate(path):
        position[vertex] = at
    level = [-1] * len(cells)
    for vertex in order:
        level[vertex] = position[vertex] if position[vertex] >= 0 else level[parent[vertex]]
    edges = []
    detour = [INFINITY] * len(cells)
    for vertex in order:
        for offset in offsets:
            other = vertex + offset
            if level[vertex] < level[other]:
                edges.append((vertex, other))
                if position[other] < 0:
                    detour[other] = min(detour[other], ds[vertex] + 1)
    heap = [(detour[v], v) for v in order if detour[v] < INFINITY]
    heapq.heapify(heap)
    while heap:
        distance, vertex = heapq.heappop(heap)
        if distance != detour[vertex]:
            continue
        for offset in offsets:
            other = vertex + offset
            if (
                level[other] == level[vertex]
                and position[other] < 0
                and distance + 1 < detour[other]
            ):
                detour[other] = distance + 1
                heapq.heappush(heap, (distance + 1, other))
    answer = [INFINITY] * (length + 1)
    intervals = []
    for first, second in edges:
        left, right = level[first], level[second]
        if left + 1 < right:
            intervals.append((left + 1, right - 1, ds[first] + 1 + dt[second]))
        if position[first] < 0 and 1 <= left < length:
            answer[left] = min(answer[left], detour[first] + 1 + dt[second])
    intervals.sort()
    at = 0
    best = 1
    for failed in range(1, length):
        while at < len(intervals) and intervals[at][0] <= failed:
            _, right, cost = intervals[at]
            heapq.heappush(heap, (cost, right))
            at += 1
        while heap and heap[0][1] < failed:
            heapq.heappop(heap)
        if heap:
            answer[failed] = min(answer[failed], heap[0][0])
        if answer[failed] > answer[best]:
            best = failed
    vertex = path[best]
    return vertex // stride - 1, vertex % stride - 1


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    rows, cols = int(next(tokens)), int(next(tokens))
    sr, sc = int(next(tokens)) - 1, int(next(tokens)) - 1
    tr, tc = int(next(tokens)) - 1, int(next(tokens)) - 1
    grid = [next(tokens) for _ in range(rows)]
    row, col = solve(grid, sr, sc, tr, tc)
    print(row + 1, col + 1)
