import sys
from array import array

INDEX_BITS = 16
UNVISITED = (1 << INDEX_BITS) - 1


def main():
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n, q = next(tokens), next(tokens)

    def zeros(size):
        return array("H", [0]) * size

    # Vertex<=20000, edge<=39998, query<=50000. Zero is the list sentinel.
    # every valid ID and depth fits an unsigned 16-bit cell.
    head, to, following = zeros(n + 1), zeros(2 * n), zeros(2 * n)
    edge = 0
    for _ in range(n - 1):
        a, b = next(tokens), next(tokens)
        edge += 1
        to[edge], following[edge], head[a] = b, head[a], edge
        edge += 1
        to[edge], following[edge], head[b] = a, head[b], edge
    ask_head, ask_next = zeros(n + 1), zeros(q + 1)
    distance, answer = zeros(q + 1), zeros(q + 1)
    for i in range(1, q + 1):
        vertex, distance[i] = next(tokens), next(tokens)
        ask_next[i], ask_head[vertex] = ask_head[vertex], i
    del tokens
    path, stack = zeros(n + 1), zeros(n + 1)

    def walk(root):
        depth = array("H", [UNVISITED]) * (n + 1)
        depth[root] = 0
        stack[0], top, deepest = root, 1, root
        while top:
            top -= 1
            vertex = stack[top]
            dv = depth[vertex]
            path[dv] = vertex
            if dv > depth[deepest]:
                deepest = vertex
            query = ask_head[vertex]
            while query:
                if answer[query] == 0 and distance[query] <= dv:
                    answer[query] = path[dv - distance[query]]
                query = ask_next[query]
            edge = head[vertex]
            while edge:
                child = to[edge]
                if depth[child] == UNVISITED:
                    depth[child] = dv + 1
                    stack[top] = child
                    top += 1
                edge = following[edge]
        return deepest

    # A path towards one of the diameter ends reaches every feasible distance.
    a = walk(1)
    b = walk(a)
    walk(b)
    sys.stdout.write("\n".join(map(str, answer[1:])) + "\n")


main()
