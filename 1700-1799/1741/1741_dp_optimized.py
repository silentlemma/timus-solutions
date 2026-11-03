from array import array
import sys

INF = 10**18
PIRATED = ord("P")
CRACKED = ord("C")


def main():
    tokens = (word for line in sys.stdin.buffer for word in line.split())
    n, m = int(next(tokens)), int(next(tokens))
    head = array("i", [-1]) * n
    to = array("i", [0]) * m
    link = array("i", [0]) * m
    weight = array("i", [0]) * m
    kind = bytearray(m)
    for edge in range(m):
        x, y, cost = int(next(tokens)) - 1, int(next(tokens)) - 1, int(next(tokens))
        kind[edge] = next(tokens)[0]
        to[edge], weight[edge], link[edge], head[x] = y, cost, head[x], edge
    clean = array("q", [INF]) * n
    dirty = array("q", [INF]) * n
    clean[0] = 0
    for v in range(n):
        licensed, pirated = clean[v], dirty[v]
        edge = head[v]
        while edge != -1:
            y, cost = to[edge], weight[edge]
            if kind[edge] == PIRATED:
                value = min(licensed, pirated) + cost
                if value < dirty[y]:
                    dirty[y] = value
            else:
                value = licensed + cost
                if value < clean[y]:
                    clean[y] = value
                if kind[edge] == CRACKED:
                    value = pirated + cost
                    if value < dirty[y]:
                        dirty[y] = value
            edge = link[edge]
    answer = min(clean[n - 1], dirty[n - 1])
    print("Offline" if answer == INF else "Online\n" + str(answer))


main()
