import sys
from array import array

MAX_COST = 100000


def main():
    # read one line at a time instead of retaining every token of the matrix.
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n, k = next(tokens), next(tokens)
    # every cost is at most MAX_COST, so MAX_COST + 1 works as infinity
    best = [MAX_COST + 1] * n
    remaining = list(range(n))
    for _ in range(k):
        best[next(tokens) - 1] = 0
    # costs <= 100000 fit the judge's 32-bit unsigned array elements.
    cost = [array("I", (next(tokens) for _ in range(n))) for _ in range(n)]
    answer = 0
    for _ in range(n):
        vertex = min(remaining, key=best.__getitem__)
        answer += best[vertex]
        remaining.remove(vertex)
        row = cost[vertex]
        for v in remaining:
            price = row[v]
            if price < best[v]:
                best[v] = price
    print(answer)


main()
