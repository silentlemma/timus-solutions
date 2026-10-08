import heapq
import sys

SIZE = 8
FACES = 6
BOTTOM = 4
# faces in the input order near, far, top, right, bottom, left; a roll in
# direction d puts the face from position SOURCE[d][i] to position i
STEPS = ((0, 1), (0, -1), (1, 0), (-1, 0))
SOURCE = ((4, 2, 0, 3, 1, 5), (2, 4, 1, 3, 0, 5), (0, 1, 5, 2, 3, 4), (0, 1, 3, 4, 5, 2))


def cell(name):
    return ord(name[0]) - ord("a"), int(name[1]) - 1


def main():
    data = sys.stdin.read().split()
    start, end = cell(data[0]), cell(data[1])
    value = list(map(int, data[2 : 2 + FACES]))
    # Dijkstra over (cell, orientation); an orientation tells which original
    # face is at each position, and a state costs its bottom face
    first = (start, tuple(range(FACES)))
    dist, prev = {first: value[BOTTOM]}, {first: None}
    heap = [(value[BOTTOM], first)]
    while heap:
        d, state = heapq.heappop(heap)
        if d > dist[state]:
            continue
        (x, y), faces = state
        if (x, y) == end:
            break
        for (dx, dy), source in zip(STEPS, SOURCE):
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                rolled = tuple(faces[i] for i in source)
                nxt = ((nx, ny), rolled)
                nd = d + value[rolled[BOTTOM]]
                if nd < dist.get(nxt, nd + 1):
                    dist[nxt], prev[nxt] = nd, state
                    heapq.heappush(heap, (nd, nxt))
    # the first end state taken from the heap is optimal
    route = []
    while state is not None:
        (x, y), _ = state
        route.append(chr(ord("a") + x) + str(y + 1))
        state = prev[state]
    print(d, " ".join(reversed(route)))


main()
