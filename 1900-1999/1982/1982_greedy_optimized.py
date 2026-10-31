import sys
from array import array

MAX_COST = 100000


def main():
    # read one line at a time instead of retaining every token of the matrix.
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n, k = next(tokens), next(tokens)
    # every cost is at most MAX_COST, so MAX_COST + 1 works as infinity
    best = [MAX_COST + 1] * n
    used = [False] * n
    for _ in range(k):
        best[next(tokens) - 1] = 0
    # costs <= 100000 fit the judge's 32-bit unsigned array elements.
    cost = [array("I", (next(tokens) for _ in range(n))) for _ in range(n)]
    answer = 0
    for _ in range(n):
        vertex = -1
        for v in range(n):
            if not used[v] and (vertex < 0 or best[v] < best[vertex]):
                vertex = v
        answer += best[vertex]
        used[vertex] = True
        for v, price in enumerate(cost[vertex]):
            if not used[v] and price < best[v]:
                best[v] = price
    print(answer)


main()
