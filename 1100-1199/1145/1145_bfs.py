import sys
from collections import deque


def main():
    lines = sys.stdin.buffer.read().split()
    width, height = int(lines[0]), int(lines[1])
    # a border of walls around the maze keeps every neighbour in range
    cols = width + 2
    free = bytearray((height + 2) * cols)
    for r in range(height):
        row = lines[2 + r]
        base = (r + 1) * cols + 1
        for c in range(width):
            if row[c] == ord("."):
                free[base + c] = 1
    steps = (1, -1, cols, -cols)

    def farthest(start):
        # breadth-first search; the free cells form a tree, so distances
        # along it are the only paths
        dist = [-1] * len(free)
        dist[start] = 0
        queue = deque([start])
        last = start
        while queue:
            last = queue.popleft()
            d = dist[last] + 1
            for s in steps:
                nxt = last + s
                if free[nxt] and dist[nxt] < 0:
                    dist[nxt] = d
                    queue.append(nxt)
        return last, dist[last]

    # the farthest cell from any cell is an end of a longest path
    end, _ = farthest(free.index(1))
    _, length = farthest(end)
    print(length)


main()
