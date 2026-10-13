import heapq
import sys

# weights in grams, times in minutes
TRUCK = 3_000_000
CUP = 100
ORDER = 10_000_000
DAY = 24 * 60
ROAD = 4


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    if n == 1:
        print(ORDER)  # the cups are already there
        return
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + ROAD * m, ROAD):
        a, b, t, limit = data[i : i + ROAD]
        adj[a].append((b, t, limit))
        adj[b].append((a, t, limit))

    def in_time(weight):
        """Can a truck of this weight reach n within a day?"""
        dist = [DAY + 1] * (n + 1)
        dist[1] = 0
        heap = [(0, 1)]
        while heap:
            d, v = heapq.heappop(heap)
            if v == n:
                return True
            if d > dist[v]:
                continue
            for u, t, limit in adj[v]:
                if limit >= weight and d + t < dist[u]:
                    dist[u] = d + t
                    heapq.heappush(heap, (d + t, u))
        return False

    # the heaviest possible truck weighs as much as some road allows, and
    # fewer roads are open to a heavier one, so search the road limits
    ends = (data[i + ROAD - 1] for i in range(2, 2 + ROAD * m, ROAD))
    limits = sorted({x for x in ends if x >= TRUCK})
    lo, hi = 0, len(limits) - 1
    best = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if in_time(limits[mid]):
            best, lo = limits[mid], mid + 1
        else:
            hi = mid - 1
    print(0 if best < 0 else min(ORDER, (best - TRUCK) // CUP))


main()
