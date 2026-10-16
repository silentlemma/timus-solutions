import sys
from collections import deque


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = [data[1 + i * n:1 + (i + 1) * n] for i in range(n)]
    # renumbering contests and rooms together, room j must be free of every
    # later contest, so a contest that uses room b must come no later than
    # contest b: an order of the graph with an edge a -> b for each such use
    after = [[b for b in range(n) if b != a and grid[a][b] == "1"] for a in range(n)]
    waiting = [0] * n
    for a in range(n):
        for b in after[a]:
            waiting[b] += 1
    ready = deque(v for v in range(n) if waiting[v] == 0)
    order = []
    while ready:
        a = ready.popleft()
        order.append(a)
        for b in after[a]:
            waiting[b] -= 1
            if waiting[b] == 0:
                ready.append(b)
    if len(order) < n:
        print(-1)
        return
    # each swap puts the next contest of the order in its place, so at most
    # n - 1 swaps are needed
    where = list(range(n))
    here = list(range(n))
    swaps = []
    for i, v in enumerate(order):
        j = where[v]
        if j != i:
            swaps.append((i + 1, j + 1))
            here[i], here[j] = here[j], here[i]
            where[here[i]], where[here[j]] = i, j
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


main()
