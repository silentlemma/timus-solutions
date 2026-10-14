import heapq
import sys

FIELDS = 5  # u, v, toll, time and height of a road


def main():
    data = map(int, sys.stdin.buffer.read().split())
    n, m, s, f = next(data), next(data), next(data), next(data)
    budget, limit = next(data), next(data)
    roads = [tuple(next(data) for _ in range(FIELDS)) for _ in range(m)]
    if s == f:
        print("0\n0\n")
        return
    # a cheapest route repeats no city, so it pays at most n - 1 tolls
    budget = min(budget, n - 1)
    out = [[] for _ in range(n + 1)]
    for idx, (u, v, c, t, h) in enumerate(roads):
        out[u].append((v, c, t, h, idx))
    # shorter parallel roads first, to avoid obsolete heap entries
    for edges in out:
        edges.sort(key=lambda r: r[2])

    def route(height):
        """A route from s to f within the limits using roads no higher than
        height, as road numbers, or None."""
        # best[v]: the least time to v with each number of tolls paid
        best = [[None] * (budget + 1) for _ in range(n + 1)]
        came = {}
        best[s][0] = 0
        heap = [(0, 0, s)]
        while heap:
            time, paid, v = heapq.heappop(heap)
            if best[v][paid] != time:
                continue
            # a state is useless if fewer tolls already reach v as fast
            if any(x is not None and x <= time for x in best[v][:paid]):
                continue
            if v == f:
                path = []
                while (v, paid) in came:
                    idx, v, paid = came[(v, paid)]
                    path.append(idx + 1)
                return path[::-1]
            for w, c, t, h, idx in out[v]:
                nt, np = time + t, paid + c
                if h <= height and np <= budget and nt <= limit:
                    if best[w][np] is None or nt < best[w][np]:
                        best[w][np] = nt
                        came[(w, np)] = (idx, v, paid)
                        heapq.heappush(heap, (nt, np, w))
        return None

    heights = sorted({h for _, _, _, _, h in roads})
    if route(heights[-1]) is None:
        print(-1)
        return
    lo, hi = 0, len(heights) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if route(heights[mid]) is not None:
            hi = mid
        else:
            lo = mid + 1
    path = route(heights[lo])
    print(heights[lo])
    print(len(path))
    print(" ".join(map(str, path)))


main()
