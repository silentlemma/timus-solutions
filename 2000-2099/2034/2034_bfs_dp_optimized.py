from array import array
import sys

TERMINALS = 3


def main():
    tokens = (word for line in sys.stdin.buffer for word in line.split())
    n, m = int(next(tokens)), int(next(tokens))
    head = array("i", [-1]) * n
    to = array("i", [0]) * (2 * m)
    link = array("i", [0]) * (2 * m)
    for edge in range(m):
        a, b = int(next(tokens)) - 1, int(next(tokens)) - 1
        j = 2 * edge
        to[j], link[j], head[a] = b, head[a], j
        to[j + 1], link[j + 1], head[b] = a, head[b], j + 1
    start, finish, origin = (int(next(tokens)) - 1 for _ in range(TERMINALS))
    queue = array("i", [0]) * n
    clearance = array("i", [-1]) * n
    clearance[origin] = 0
    queue[0] = origin
    end = 1
    position = 0
    while position < end:
        v = queue[position]
        position += 1
        edge = head[v]
        while edge != -1:
            u = to[edge]
            if clearance[u] < 0:
                clearance[u] = clearance[v] + 1
                queue[end] = u
                end += 1
            edge = link[edge]

    depth = array("i", [-1]) * n
    best = array("i", [0]) * n
    depth[start] = 0
    best[start] = clearance[start]
    queue[0] = start
    position, end = 0, 1
    while position < end:
        v = queue[position]
        position += 1
        # All previous-layer vertices have been processed before v is popped.
        if v == finish:
            print(best[v])
            return
        following_depth = depth[v] + 1
        score = best[v]
        edge = head[v]
        while edge != -1:
            u = to[edge]
            if depth[u] < 0:
                depth[u] = following_depth
                queue[end] = u
                end += 1
            if depth[u] == following_depth:
                value = clearance[u]
                if score < value:
                    value = score
                if value > best[u]:
                    best[u] = value
            edge = link[edge]


main()
