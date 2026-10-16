import sys
from heapq import heappop, heappush

DIGITS = 10


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cost = list(map(int, data[1:1 + DIGITS]))
    numbers = [int(s) for s in data[1 + DIGITS:1 + DIGITS + n]]
    index = {v: i for i, v in enumerate(numbers)}
    # place[p]: the value of a unit in digit p, counted from the left
    place = [10 ** (DIGITS - 1 - p) for p in range(DIGITS)]
    best = [None] * n
    before = [-1] * n
    best[0] = 0
    heap = [(0, 0)]
    while heap:
        d, u = heappop(heap)
        if d > best[u]:
            continue
        if u == n - 1:
            break
        value = numbers[u]
        digit = [value // place[p] % 10 for p in range(DIGITS)]
        # neighbours with the first change at digit p share a prefix of p
        for p in range(DIGITS):
            step = d + cost[p]
            unit = place[p]
            low = value - digit[p] * unit
            for other in range(10):
                if other != digit[p]:
                    v = index.get(low + other * unit)
                    if v is not None and (best[v] is None or step < best[v]):
                        best[v] = step
                        before[v] = u
                        heappush(heap, (step, v))
            for q in range(p + 1, DIGITS):
                if digit[q] != digit[p]:
                    diff = (digit[q] - digit[p]) * (unit - place[q])
                    v = index.get(value + diff)
                    if v is not None and (best[v] is None or step < best[v]):
                        best[v] = step
                        before[v] = u
                        heappush(heap, (step, v))
    if best[n - 1] is None:
        print(-1)
        return
    path = [n - 1]
    while path[-1] != 0:
        path.append(before[path[-1]])
    path.reverse()
    print(best[n - 1])
    print(len(path))
    print(" ".join(str(v + 1) for v in path))


main()
